from enum import Enum


class MigrationType(str, Enum):
    COPY = "copy"
    EXTEND = "extend"
    RE_EXTRACT = "re_extract"

    def __str__(self) -> str:
        return str(self.value)
