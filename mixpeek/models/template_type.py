from enum import Enum


class TemplateType(str, Enum):
    BUCKET = "bucket"
    CLUSTER = "cluster"
    COLLECTION = "collection"
    NAMESPACE = "namespace"
    RETRIEVER = "retriever"
    SCAFFOLD = "scaffold"
    TAXONOMY = "taxonomy"

    def __str__(self) -> str:
        return str(self.value)
