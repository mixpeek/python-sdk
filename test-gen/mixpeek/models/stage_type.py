from enum import Enum


class StageType(str, Enum):
    APPLY = "apply"
    ENRICH = "enrich"
    FILTER = "filter"
    REDUCE = "reduce"
    SORT = "sort"

    def __str__(self) -> str:
        return str(self.value)
