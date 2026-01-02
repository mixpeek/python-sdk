from enum import Enum


class RetryBatchRequestRetryMode(str, Enum):
    ALL = "all"
    TRANSIENT_ONLY = "transient_only"

    def __str__(self) -> str:
        return str(self.value)
