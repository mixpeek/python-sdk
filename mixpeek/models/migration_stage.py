from enum import Enum


class MigrationStage(str, Enum):
    BATCH_CREATION = "batch_creation"
    BATCH_PROCESSING = "batch_processing"
    BENCHMARK_EVALUATION = "benchmark_evaluation"
    CLUSTER_EXECUTION = "cluster_execution"
    FINALIZATION = "finalization"
    NAMESPACE_SETUP = "namespace_setup"
    TAXONOMY_ENRICHMENT = "taxonomy_enrichment"

    def __str__(self) -> str:
        return str(self.value)
