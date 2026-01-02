from enum import Enum


class ClusterType(str, Enum):
    ATTRIBUTE = "attribute"
    VECTOR = "vector"

    def __str__(self) -> str:
        return str(self.value)
