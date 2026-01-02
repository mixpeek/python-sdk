from enum import Enum


class FilterOperator(str, Enum):
    CONTAINS = "contains"
    ENDS_WITH = "ends_with"
    EQ = "eq"
    EXISTS = "exists"
    GT = "gt"
    GTE = "gte"
    IN = "in"
    IS_NULL = "is_null"
    LT = "lt"
    LTE = "lte"
    NE = "ne"
    NIN = "nin"
    REGEX = "regex"
    STARTS_WITH = "starts_with"
    TEXT = "text"

    def __str__(self) -> str:
        return str(self.value)
