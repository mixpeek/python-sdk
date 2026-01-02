from enum import Enum


class OpenAIModel(str, Enum):
    GPT_4O_2024_08_06 = "gpt-4o-2024-08-06"
    GPT_4O_MINI_2024_07_18 = "gpt-4o-mini-2024-07-18"
    GPT_4_1_2025_04_14 = "gpt-4.1-2025-04-14"
    GPT_4_1_MINI_2025_04_14 = "gpt-4.1-mini-2025-04-14"
    O3_MINI_2025_01_31 = "o3-mini-2025-01-31"

    def __str__(self) -> str:
        return str(self.value)
