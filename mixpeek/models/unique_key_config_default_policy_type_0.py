from enum import Enum


class UniqueKeyConfigDefaultPolicyType0(str, Enum):
    INSERT = "insert"
    UPDATE = "update"
    UPSERT = "upsert"

    def __str__(self) -> str:
        return str(self.value)
