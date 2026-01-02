from enum import Enum


class SourceType(str, Enum):
    BUCKET = "bucket"
    CLUSTER = "cluster"
    COLLECTION = "collection"
    TAXONOMY = "taxonomy"

    def __str__(self) -> str:
        return str(self.value)
