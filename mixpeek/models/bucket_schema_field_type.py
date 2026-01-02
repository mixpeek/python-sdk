from enum import Enum


class BucketSchemaFieldType(str, Enum):
    ARRAY = "array"
    AUDIO = "audio"
    BOOLEAN = "boolean"
    DATE = "date"
    DATETIME = "datetime"
    EXCEL = "excel"
    FLOAT = "float"
    IMAGE = "image"
    INTEGER = "integer"
    NUMBER = "number"
    OBJECT = "object"
    PDF = "pdf"
    STRING = "string"
    TEXT = "text"
    VIDEO = "video"

    def __str__(self) -> str:
        return str(self.value)
