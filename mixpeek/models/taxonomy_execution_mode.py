from enum import Enum


class TaxonomyExecutionMode(str, Enum):
    MATERIALIZE = "materialize"

    def __str__(self) -> str:
        return str(self.value)
