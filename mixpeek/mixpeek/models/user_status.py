from enum import Enum


class UserStatus(str, Enum):
    ACTIVE = "active"
    PENDING = "pending"
    SUSPENDED = "suspended"

    def __str__(self) -> str:
        return str(self.value)
