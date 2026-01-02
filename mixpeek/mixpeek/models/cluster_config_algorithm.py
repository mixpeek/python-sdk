from enum import Enum


class ClusterConfigAlgorithm(str, Enum):
    AGGLOMERATIVE = "agglomerative"
    DBSCAN = "dbscan"
    GAUSSIAN_MIXTURE = "gaussian_mixture"
    HDBSCAN = "hdbscan"
    KMEANS = "kmeans"
    SPECTRAL = "spectral"

    def __str__(self) -> str:
        return str(self.value)
