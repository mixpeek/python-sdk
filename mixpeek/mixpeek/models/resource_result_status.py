from enum import Enum


class ResourceResultStatus(str, Enum):
    CREATED = "created"
    FAILED = "failed"
    SKIPPED = "skipped"

    def __str__(self) -> str:
        return str(self.value)
