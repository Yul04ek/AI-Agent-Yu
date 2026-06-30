from collections.abc import Callable
from dataclasses import dataclass
from typing import Any
from pathlib import Path

import frontmatter
from pydantic_ai import RunContext
from pydantic_ai.capabilities import AbstractCapability
from pydantic_ai.settings import ModelSettings

def _load_skill_keywords() -> list[str]:
    keywords = []
    for f in Path("skills").glob("*.md"):
        skill = frontmatter.load(str(f))
        name = skill.metadata.get("name", "")
        keywords.extend(name.split("-"))
    return keywords

@dataclass
class ReasoningEffort(AbstractCapability[Any]):
    skill_keywords: list[str] 
    def get_model_settings(
        self,
    ) -> Callable[[RunContext[Any]], ModelSettings]:
        def _set_reasoning_effort(ctx: RunContext[Any]) -> ModelSettings:
            prompt = str(ctx.prompt).lower()

            # Manual tag wins — useralready decided.
            if "@low" in prompt:
                return ModelSettings(thinking="low")
            if "@high" in prompt:
                return ModelSettings(thinking="high")

            # No tag: detect automatically and apply.
            easy = ("rename", "format", "typo", "comment","print result", "simple plot",)
            if any(w in prompt for w in self.skill_keywords):
                ctx.deps.console.log("Detected complex task — using deep reasoning.")
                return ModelSettings(thinking="high")
            elif any(w in prompt for w in easy):
                ctx.deps.console.log("Detected simple task — using fast reasoning.")
                return ModelSettings(thinking="low")
            return ModelSettings()

        return _set_reasoning_effort
        
        
        
        
