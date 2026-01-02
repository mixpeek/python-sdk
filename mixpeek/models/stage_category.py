from enum import Enum


class StageCategory(str, Enum):
    APPLY = "apply"
    ENRICH = "enrich"
    FILTER = "filter"
    REDUCE = "reduce"
    SORT = "sort"

    def __str__(self) -> str:
        return str(self.value)
