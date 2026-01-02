from enum import Enum


class SampleStageConfigStrategy(str, Enum):
    RANDOM = "random"
    RESERVOIR = "reservoir"
    STRATIFIED = "stratified"

    def __str__(self) -> str:
        return str(self.value)
