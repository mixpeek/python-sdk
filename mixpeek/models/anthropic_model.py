from enum import Enum


class AnthropicModel(str, Enum):
    CLAUDE_3_5_HAIKU_20241022 = "claude-3-5-haiku-20241022"
    CLAUDE_3_5_SONNET_20241022 = "claude-3-5-sonnet-20241022"

    def __str__(self) -> str:
        return str(self.value)
