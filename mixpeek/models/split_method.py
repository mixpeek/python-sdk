from enum import Enum


class SplitMethod(str, Enum):
    SCENE = "scene"
    SILENCE = "silence"
    TIME = "time"

    def __str__(self) -> str:
        return str(self.value)
