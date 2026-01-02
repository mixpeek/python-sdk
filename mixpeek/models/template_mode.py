from enum import Enum


class TemplateMode(str, Enum):
    CLONE = "clone"
    CONFIG = "config"
    SCAFFOLD = "scaffold"

    def __str__(self) -> str:
        return str(self.value)
