from enum import Enum


class ErrorCategory(str, Enum):
    AUTHENTICATION = "authentication"
    DEPENDENCY = "dependency"
    NETWORK = "network"
    RESOURCE = "resource"
    RUNTIME = "runtime"
    VALIDATION = "validation"

    def __str__(self) -> str:
        return str(self.value)
