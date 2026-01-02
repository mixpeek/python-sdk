from enum import Enum


class SyncMode(str, Enum):
    CONTINUOUS = "continuous"
    INITIAL_ONLY = "initial_only"

    def __str__(self) -> str:
        return str(self.value)
