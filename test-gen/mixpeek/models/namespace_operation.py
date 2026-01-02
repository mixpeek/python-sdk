from enum import Enum


class NamespaceOperation(str, Enum):
    CANCEL_JOB = "cancel_job"
    CREATE_CLUSTER = "create_cluster"
    CREATE_RETRIEVER = "create_retriever"
    DELETE_CLUSTER = "delete_cluster"
    DELETE_DATA = "delete_data"
    DELETE_RETRIEVER = "delete_retriever"
    EXECUTE_JOB = "execute_job"
    EXECUTE_RETRIEVER = "execute_retriever"
    MANAGE_PERMISSIONS = "manage_permissions"
    MODIFY_CLUSTER = "modify_cluster"
    MODIFY_INFRASTRUCTURE = "modify_infrastructure"
    READ_DATA = "read_data"
    WRITE_DATA = "write_data"

    def __str__(self) -> str:
        return str(self.value)
