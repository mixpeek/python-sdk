from enum import Enum


class PaginationMethod(str, Enum):
    CURSOR = "cursor"
    KEYSET = "keyset"
    OFFSET = "offset"
    SCROLL = "scroll"

    def __str__(self) -> str:
        return str(self.value)
