from enum import Enum


class ClusteringAlgorithm(str, Enum):
    AGGLOMERATIVE = "agglomerative"
    ATTRIBUTE_BASED = "attribute_based"
    DBSCAN = "dbscan"
    GAUSSIAN_MIXTURE = "gaussian_mixture"
    HDBSCAN = "hdbscan"
    KMEANS = "kmeans"
    MEAN_SHIFT = "mean_shift"
    OPTICS = "optics"
    SPECTRAL = "spectral"

    def __str__(self) -> str:
        return str(self.value)
