from enum import Enum


class VectorBasedConfigMultiFeatureStrategy(str, Enum):
    CONCATENATE = "concatenate"
    INDEPENDENT = "independent"
    WEIGHTED = "weighted"

    def __str__(self) -> str:
        return str(self.value)
