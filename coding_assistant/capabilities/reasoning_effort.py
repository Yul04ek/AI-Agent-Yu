from collections.abc import Callable
from dataclasses import dataclass
from typing import Any

from pydantic_ai import RunContext
from pydantic_ai.capabilities import AbstractCapability
from pydantic_ai.settings import ModelSettings


@dataclass
class ReasoningEffort(AbstractCapability[Any]):
    def get_model_settings(
        self,
    ) -> Callable[[RunContext[Any]], ModelSettings]:
        def _set_reasoning_effort(ctx: RunContext[Any]) -> ModelSettings:
            prompt = str(ctx.prompt).lower()

            # Manual tag is the real control — it wins and skips the tip.
            if "@low" in prompt:
                return ModelSettings(thinking="low")
            if "@high" in prompt:
                return ModelSettings(thinking="high")

            # No tag: only recommend a level, the user decides next time.
            hard = ("refactor", "debug", "architecture", "design", "optimize")
            easy = ("rename", "format", "typo", "comment")
            if any(w in prompt for w in hard):
                ctx.deps.console.log(
                    "Tip: this looks complex — add @high for deeper reasoning."
                )
            elif any(w in prompt for w in easy):
                ctx.deps.console.log(
                    "Tip: this looks simple — add @low for faster, cheaper output."
                )

            return ModelSettings()

        return _set_reasoning_effort