from enum import Enum


class RateLimitTier(str, Enum):
    ELEVATED = "elevated"
    ENTERPRISE = "enterprise"
    STANDARD = "standard"
    UNLIMITED = "unlimited"

    def __str__(self) -> str:
        return str(self.value)
