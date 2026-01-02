from enum import Enum


class DatePartUnit(str, Enum):
    DAY = "day"
    DAYOFWEEK = "dayOfWeek"
    DAYOFYEAR = "dayOfYear"
    HOUR = "hour"
    MINUTE = "minute"
    MONTH = "month"
    SECOND = "second"
    WEEK = "week"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)
