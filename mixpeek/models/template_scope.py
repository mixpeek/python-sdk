from enum import Enum


class TemplateScope(str, Enum):
    ORGANIZATION = "organization"
    PUBLIC = "public"
    SYSTEM = "system"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
