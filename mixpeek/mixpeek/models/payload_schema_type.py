from enum import Enum


class PayloadSchemaType(str, Enum):
    BOOL = "bool"
    DATETIME = "datetime"
    FLOAT = "float"
    GEO = "geo"
    INTEGER = "integer"
    KEYWORD = "keyword"
    TEXT = "text"
    UUID = "uuid"

    def __str__(self) -> str:
        return str(self.value)
