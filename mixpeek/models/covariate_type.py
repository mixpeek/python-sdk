from enum import Enum


class CovariateType(str, Enum):
    CATEGORICAL = "categorical"
    CLUSTER_ID = "cluster_id"
    EMBEDDING = "embedding"
    NUMERIC = "numeric"

    def __str__(self) -> str:
        return str(self.value)
