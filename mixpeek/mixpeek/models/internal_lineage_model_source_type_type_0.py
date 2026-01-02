from enum import Enum


class InternalLineageModelSourceTypeType0(str, Enum):
    BUCKET = "bucket"
    COLLECTION = "collection"

    def __str__(self) -> str:
        return str(self.value)
