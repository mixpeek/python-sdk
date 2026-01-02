from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="SubmitFeedbackResponse")


@_attrs_define
class SubmitFeedbackResponse:
    """Response for feedback submission.

    Attributes:
        session_id: Session identifier
        message_id: Message that received feedback
        rating: The feedback rating submitted
        stored: Whether the exchange was stored to memory
        recorded_at: Timestamp when feedback was recorded

    Example:
        ```python
        response = SubmitFeedbackResponse(
            session_id="ses_abc123",
            message_id="msg_xyz789",
            rating="positive",
            stored=True,
            recorded_at=datetime.utcnow()
        )
        ```

        Attributes:
            session_id (str): Session identifier
            message_id (str): Message identifier
            rating (str): Feedback rating submitted
            stored (bool): Whether exchange was stored to memory
            recorded_at (datetime.datetime): Feedback timestamp
    """

    session_id: str
    message_id: str
    rating: str
    stored: bool
    recorded_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        session_id = self.session_id

        message_id = self.message_id

        rating = self.rating

        stored = self.stored

        recorded_at = self.recorded_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "session_id": session_id,
                "message_id": message_id,
                "rating": rating,
                "stored": stored,
                "recorded_at": recorded_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        session_id = d.pop("session_id")

        message_id = d.pop("message_id")

        rating = d.pop("rating")

        stored = d.pop("stored")

        recorded_at = isoparse(d.pop("recorded_at"))

        submit_feedback_response = cls(
            session_id=session_id,
            message_id=message_id,
            rating=rating,
            stored=stored,
            recorded_at=recorded_at,
        )

        submit_feedback_response.additional_properties = d
        return submit_feedback_response

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
