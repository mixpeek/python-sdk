from enum import Enum


class CovariateConfigBinningStrategyType0(str, Enum):
    CUSTOM = "custom"
    DECILES = "deciles"
    QUARTILES = "quartiles"

    def __str__(self) -> str:
        return str(self.value)
