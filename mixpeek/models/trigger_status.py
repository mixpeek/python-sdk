from enum import Enum


class TriggerStatus(str, Enum):
    ACTIVE = "active"
    DISABLED = "disabled"
    FAILED = "failed"
    PAUSED = "paused"

    def __str__(self) -> str:
        return str(self.value)
