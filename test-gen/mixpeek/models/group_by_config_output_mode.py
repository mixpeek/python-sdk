from enum import Enum


class GroupByConfigOutputMode(str, Enum):
    ALL = "all"
    FIRST = "first"
    FLATTEN = "flatten"

    def __str__(self) -> str:
        return str(self.value)
