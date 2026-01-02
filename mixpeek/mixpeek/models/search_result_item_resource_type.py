from enum import Enum


class SearchResultItemResourceType(str, Enum):
    BUCKET = "bucket"
    CLUSTER = "cluster"
    COLLECTION = "collection"
    NAMESPACE = "namespace"
    PUBLISHED_RETRIEVER = "published_retriever"
    RETRIEVER = "retriever"
    TAXONOMY = "taxonomy"

    def __str__(self) -> str:
        return str(self.value)
