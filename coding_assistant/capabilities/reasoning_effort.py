import json
from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Any

from openai import OpenAI
from pydantic_ai import RunContext
from pydantic_ai.capabilities import AbstractCapability
from pydantic_ai.settings import ModelSettings

from dataclasses import field

@dataclass
class ReasoningEffort(AbstractCapability[Any]):
    # Separate lightweight client for classification calls —
    # reuses the same OpenRouter credentials as the main agent.
    base_url: str
    api_key: str
    model_name: str
    confidence_threshold: float = 0.6
    client: OpenAI = field(init=False)

    # Mapping for log messages based on classification result
    _LOG_MESSAGES: dict[str, str] = field(
        default_factory=lambda: {
            "complex": "Detected complex task — using deep reasoning.",
            "simple": "Detected simple task — using fast reasoning.",
            "default": "Default reasoning effort — using medium reasoning.",
        })

    def __post_init__(self) -> None:
        self.client = OpenAI(base_url=self.base_url, api_key=self.api_key)

    def _classify(self, prompt: str) -> tuple[str, float]:
        # Ask the model to act as a zero-shot classifier via API call.
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Classify the user's request as 'simple' or 'complex'. "
                        "Respond with only JSON: {\"label\": \"...\", \"score\": 0.0}"
                    ),
                },
                {"role": "user", "content": prompt},
            ],
        )
        try:
            result = json.loads(response.choices[0].message.content)
            label = result["label"]
            score = result["score"]
        except (json.JSONDecodeError, KeyError, TypeError) as e:
            raise ValueError(f"Invalid classification response: {e}")
        if label not in ("simple", "complex"):
            raise ValueError(f"Unexpected classification label '{label}'")
        return label, score

    def get_model_settings(self) -> Callable[[RunContext[Any]], ModelSettings]:
        def _set_reasoning_effort(ctx: RunContext[Any]) -> ModelSettings:
            prompt = str(ctx.prompt).lower()

            # Manual tag wins — user already decided.
            if "@low" in prompt:
                ctx.deps.console.log(self._LOG_MESSAGES["simple"])
                return ModelSettings(thinking="low")
            if "@high" in prompt:
                ctx.deps.console.log(self._LOG_MESSAGES["complex"])
                return ModelSettings(thinking="high")

            # No tag: classify automatically via API-based zero-shot call.
            try:
                label, score = self._classify(prompt)
            except ValueError as e:
                ctx.deps.console.log(f"Classification error: {e}")
                return ModelSettings(thinking="medium")

            # Low confidence — fall back to default (medium) settings.
            if score < self.confidence_threshold:
                ctx.deps.console.log(self._LOG_MESSAGES["default"])
                return ModelSettings(thinking="medium")

            # Use mapping for messages and settings.
            message = self._LOG_MESSAGES.get(label, self._LOG_MESSAGES["default"])
            ctx.deps.console.log(message)
            thinking_level = "high" if label == "complex" else "low"
            return ModelSettings(thinking=thinking_level)

        return _set_reasoning_effort
