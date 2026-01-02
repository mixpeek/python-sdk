from enum import Enum


class TriggerType(str, Enum):
    CONDITIONAL = "conditional"
    CRON = "cron"
    EVENT = "event"
    INTERVAL = "interval"

    def __str__(self) -> str:
        return str(self.value)
