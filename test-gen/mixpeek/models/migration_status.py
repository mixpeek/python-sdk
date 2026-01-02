from enum import Enum


class MigrationStatus(str, Enum):
    CANCELLED = "cancelled"
    COMPLETED = "completed"
    DRAFT = "draft"
    FAILED = "failed"
    IN_PROGRESS = "in_progress"
    PENDING = "pending"
    VALIDATING = "validating"

    def __str__(self) -> str:
        return str(self.value)
