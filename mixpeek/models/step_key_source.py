from enum import Enum


class StepKeySource(str, Enum):
    ASSIGNMENT_LABEL = "assignment_label"
    ASSIGNMENT_NODE_ID = "assignment_node_id"
    FIELD_PATH = "field_path"

    def __str__(self) -> str:
        return str(self.value)
