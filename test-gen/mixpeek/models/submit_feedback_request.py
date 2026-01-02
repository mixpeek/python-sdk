from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubmitFeedbackRequest")


@_attrs_define
class SubmitFeedbackRequest:
    """Request payload for submitting feedback on a message.

    Attributes:
        message_id: The assistant message ID to provide feedback for
        rating: Feedback rating (positive or negative)
        feedback_text: Optional additional feedback text

    Example:
        ```python
        request = SubmitFeedbackRequest(
            message_id="msg_abc123",
            rating="positive",
            feedback_text="This was very helpful!"
        )
        ```

        Attributes:
            message_id (str): Assistant message ID (REQUIRED)
            rating (str): Feedback rating: 'positive' or 'negative' (REQUIRED)
            feedback_text (None | str | Unset): Additional feedback text (OPTIONAL)
    """

    message_id: str
    rating: str
    feedback_text: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message_id = self.message_id

        rating = self.rating

        feedback_text: None | str | Unset
        if isinstance(self.feedback_text, Unset):
            feedback_text = UNSET
        else:
            feedback_text = self.feedback_text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message_id": message_id,
                "rating": rating,
            }
        )
        if feedback_text is not UNSET:
            field_dict["feedback_text"] = feedback_text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message_id = d.pop("message_id")

        rating = d.pop("rating")

        def _parse_feedback_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        feedback_text = _parse_feedback_text(d.pop("feedback_text", UNSET))

        submit_feedback_request = cls(
            message_id=message_id,
            rating=rating,
            feedback_text=feedback_text,
        )

        submit_feedback_request.additional_properties = d
        return submit_feedback_request

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
