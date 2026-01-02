from enum import Enum


class AggregationFunction(str, Enum):
    ADD_TO_SET = "add_to_set"
    AVG = "avg"
    COUNT = "count"
    COUNT_DISTINCT = "count_distinct"
    FIRST = "first"
    LAST = "last"
    MAX = "max"
    MIN = "min"
    PUSH = "push"
    SUM = "sum"

    def __str__(self) -> str:
        return str(self.value)
