from enum import Enum


class BlobType(str, Enum):
    AUDIO = "audio"
    AUTO = "auto"
    EXCEL = "excel"
    IMAGE = "image"
    PDF = "pdf"
    TEXT = "text"
    VIDEO = "video"

    def __str__(self) -> str:
        return str(self.value)
