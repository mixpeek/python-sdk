from enum import Enum


class JoinMode(str, Enum):
    BATCH = "batch"
    ON_DEMAND = "on_demand"

    def __str__(self) -> str:
        return str(self.value)
