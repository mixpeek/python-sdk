from enum import Enum


class StageTypesFusionStrategy(str, Enum):
    DBSF = "dbsf"
    LEARNED = "learned"
    MAX = "max"
    RRF = "rrf"
    WEIGHTED = "weighted"

    def __str__(self) -> str:
        return str(self.value)
