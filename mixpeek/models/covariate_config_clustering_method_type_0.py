from enum import Enum


class CovariateConfigClusteringMethodType0(str, Enum):
    HDBSCAN = "hdbscan"
    KMEANS = "kmeans"

    def __str__(self) -> str:
        return str(self.value)
