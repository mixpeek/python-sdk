from enum import Enum


class QueryExpandParametersFusionStrategy(str, Enum):
    LINEAR = "linear"
    RRF = "rrf"

    def __str__(self) -> str:
        return str(self.value)
