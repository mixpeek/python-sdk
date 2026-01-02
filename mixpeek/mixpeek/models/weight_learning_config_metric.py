from enum import Enum


class WeightLearningConfigMetric(str, Enum):
    CALINSKI_HARABASZ = "calinski_harabasz"
    DAVIES_BOULDIN = "davies_bouldin"
    SILHOUETTE = "silhouette"

    def __str__(self) -> str:
        return str(self.value)
