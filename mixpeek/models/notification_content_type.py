from enum import Enum


class NotificationContentType(str, Enum):
    HTML = "html"
    JSON = "json"
    MARKDOWN = "markdown"
    PLAIN_TEXT = "plain_text"

    def __str__(self) -> str:
        return str(self.value)
