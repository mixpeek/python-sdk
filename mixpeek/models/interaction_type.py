from enum import Enum


class InteractionType(str, Enum):
    ADD_TO_CART = "add_to_cart"
    BOOKMARK = "bookmark"
    CLICK = "click"
    FILTER_TOGGLE = "filter_toggle"
    LONG_VIEW = "long_view"
    NEGATIVE_FEEDBACK = "negative_feedback"
    POSITIVE_FEEDBACK = "positive_feedback"
    PURCHASE = "purchase"
    QUERY_REFINEMENT = "query_refinement"
    RETURN_TO_RESULTS = "return_to_results"
    SHARE = "share"
    SKIP = "skip"
    VIEW = "view"
    WISHLIST = "wishlist"
    ZERO_RESULTS = "zero_results"

    def __str__(self) -> str:
        return str(self.value)
