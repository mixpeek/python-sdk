from enum import Enum


class StageTypesOnEmptyBehavior(str, Enum):
    ERROR = "error"
    RANDOM = "random"
    SKIP = "skip"

    def __str__(self) -> str:
        return str(self.value)
