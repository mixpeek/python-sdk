from enum import Enum


class Permission(str, Enum):
    ADMIN = "admin"
    DELETE = "delete"
    READ = "read"
    WRITE = "write"

    def __str__(self) -> str:
        return str(self.value)
