from enum import Enum


class DateTruncUnit(str, Enum):
    DAY = "day"
    HOUR = "hour"
    MINUTE = "minute"
    MONTH = "month"
    SECOND = "second"
    WEEK = "week"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)
