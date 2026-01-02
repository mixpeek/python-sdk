from enum import Enum


class HierarchyInferenceStrategy(str, Enum):
    CLUSTER = "cluster"
    LLM = "llm"
    SCHEMA = "schema"

    def __str__(self) -> str:
        return str(self.value)
