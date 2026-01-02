from enum import Enum


class TriggerActionType(str, Enum):
    CLUSTER = "cluster"
    TAXONOMY_ENRICHMENT = "taxonomy_enrichment"

    def __str__(self) -> str:
        return str(self.value)
