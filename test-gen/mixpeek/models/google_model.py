from enum import Enum


class GoogleModel(str, Enum):
    GEMINI_2_0_FLASH = "gemini-2.0-flash"
    GEMINI_2_0_FLASH_EXP = "gemini-2.0-flash-exp"

    def __str__(self) -> str:
        return str(self.value)
