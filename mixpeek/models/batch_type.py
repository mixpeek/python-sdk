from enum import Enum


class BatchType(str, Enum):
    BUCKET = "BUCKET"
    COLLECTION = "COLLECTION"

    def __str__(self) -> str:
        return str(self.value)
