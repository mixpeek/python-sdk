from enum import Enum


class TextSplitStrategy(str, Enum):
    CHARACTERS = "characters"
    NONE = "none"
    PAGES = "pages"
    PARAGRAPHS = "paragraphs"
    SENTENCES = "sentences"
    WORDS = "words"

    def __str__(self) -> str:
        return str(self.value)
