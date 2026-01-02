from enum import Enum


class NotificationChannel(str, Enum):
    EMAIL = "email"
    SLACK = "slack"
    SMS = "sms"
    WEBHOOK = "webhook"

    def __str__(self) -> str:
        return str(self.value)
