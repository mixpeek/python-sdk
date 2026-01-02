from enum import Enum


class AccountTier(str, Enum):
    ENTERPRISE = "enterprise"
    FREE = "free"
    PRO = "pro"
    TEAM = "team"

    def __str__(self) -> str:
        return str(self.value)
