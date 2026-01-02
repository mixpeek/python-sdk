from enum import Enum


class VectorType(str, Enum):
    DENSE = "dense"
    MULTI_DENSE = "multi_dense"
    SPARSE = "sparse"

    def __str__(self) -> str:
        return str(self.value)
