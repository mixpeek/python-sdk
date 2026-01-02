from enum import Enum


class VectorDataType(str, Enum):
    FLOAT32 = "float32"
    UINT8 = "uint8"

    def __str__(self) -> str:
        return str(self.value)
