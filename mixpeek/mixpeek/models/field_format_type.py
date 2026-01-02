from enum import Enum


class FieldFormatType(str, Enum):
    ARRAY = "array"
    BOOLEAN = "boolean"
    DATE = "date"
    IMAGE = "image"
    NUMBER = "number"
    OBJECT = "object"
    TEXT = "text"
    URL = "url"

    def __str__(self) -> str:
        return str(self.value)
