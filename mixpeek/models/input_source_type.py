from enum import Enum


class InputSourceType(str, Enum):
    LITERAL = "literal"
    PAYLOAD = "payload"
    VECTOR = "vector"

    def __str__(self) -> str:
        return str(self.value)
