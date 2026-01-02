from enum import Enum


class RetrieverStatus(str, Enum):
    ACTIVE = "active"
    DISABLED = "disabled"
    DRAFT = "draft"
    ERROR = "error"

    def __str__(self) -> str:
        return str(self.value)
