from enum import Enum


class WeightLearningConfigMethod(str, Enum):
    BAYESIAN = "bayesian"
    GRID_SEARCH = "grid_search"

    def __str__(self) -> str:
        return str(self.value)
