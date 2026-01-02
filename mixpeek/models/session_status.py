from enum import Enum


class SessionStatus(str, Enum):
    ACTIVE = "active"
    ARCHIVED = "archived"
    IDLE = "idle"
    TERMINATED = "terminated"

    def __str__(self) -> str:
        return str(self.value)
