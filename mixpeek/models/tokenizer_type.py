from enum import Enum


class TokenizerType(str, Enum):
    MULTILINGUAL = "multilingual"
    PREFIX = "prefix"
    WHITESPACE = "whitespace"
    WORD = "word"

    def __str__(self) -> str:
        return str(self.value)
