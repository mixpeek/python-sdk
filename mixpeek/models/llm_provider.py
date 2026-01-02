from enum import Enum


class LLMProvider(str, Enum):
    ANTHROPIC = "anthropic"
    GOOGLE = "google"
    OPENAI = "openai"

    def __str__(self) -> str:
        return str(self.value)
