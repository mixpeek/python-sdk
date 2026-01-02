from enum import Enum


class VectorBasedConfigOutputStrategy(str, Enum):
    PER_FEATURE = "per_feature"
    SINGLE = "single"

    def __str__(self) -> str:
        return str(self.value)
