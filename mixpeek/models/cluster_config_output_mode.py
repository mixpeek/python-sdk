from enum import Enum


class ClusterConfigOutputMode(str, Enum):
    CLUSTERS = "clusters"
    LABELED = "labeled"
    REPRESENTATIVES = "representatives"

    def __str__(self) -> str:
        return str(self.value)
