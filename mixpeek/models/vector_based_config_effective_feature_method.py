from enum import Enum


class VectorBasedConfigEffectiveFeatureMethod(str, Enum):
    MEAN = "mean"
    MEDIAN = "median"
    MEDOID = "medoid"

    def __str__(self) -> str:
        return str(self.value)
