from enum import Enum


class ComputeTier(str, Enum):
    DEDICATED_CPU = "dedicated_cpu"
    DEDICATED_GPU = "dedicated_gpu"
    SHARED = "shared"

    def __str__(self) -> str:
        return str(self.value)
