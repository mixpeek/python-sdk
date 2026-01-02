from enum import Enum


class ResourceType(str, Enum):
    API_KEY = "api_key"
    BUCKET = "bucket"
    CLUSTER = "cluster"
    COLLECTION = "collection"
    NAMESPACE = "namespace"
    ORGANIZATION = "organization"
    RETRIEVER = "retriever"
    STORAGE_CONNECTION = "storage_connection"
    TAXONOMY = "taxonomy"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
