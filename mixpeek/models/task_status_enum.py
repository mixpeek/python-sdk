from enum import Enum


class TaskStatusEnum(str, Enum):
    ACTIVE = "ACTIVE"
    ARCHIVED = "ARCHIVED"
    CANCELED = "CANCELED"
    COMPLETED = "COMPLETED"
    COMPLETED_WITH_ERRORS = "COMPLETED_WITH_ERRORS"
    DRAFT = "DRAFT"
    FAILED = "FAILED"
    IN_PROGRESS = "IN_PROGRESS"
    PENDING = "PENDING"
    PROCESSING = "PROCESSING"
    SKIPPED = "SKIPPED"
    SUSPENDED = "SUSPENDED"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
