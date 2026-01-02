from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.message_history_item import MessageHistoryItem


T = TypeVar("T", bound="GetHistoryResponse")


@_attrs_define
class GetHistoryResponse:
    """Response for retrieving conversation history.

    Attributes:
        session_id: Session identifier
        messages: List of messages in chronological order
        total_messages: Total number of messages in session
        returned_messages: Number of messages returned (may be limited)
        has_more: Whether there are more messages available

    Example:
        ```python
        response = GetHistoryResponse(
            session_id="ses_abc123",
            messages=[...],
            total_messages=50,
            returned_messages=20,
            has_more=True
        )
        ```

        Attributes:
            session_id (str): Session identifier
            messages (list[MessageHistoryItem]): Message history
            total_messages (int): Total messages in session
            returned_messages (int): Messages returned
            has_more (bool): Whether more messages available
    """

    session_id: str
    messages: list[MessageHistoryItem]
    total_messages: int
    returned_messages: int
    has_more: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        session_id = self.session_id

        messages = []
        for messages_item_data in self.messages:
            messages_item = messages_item_data.to_dict()
            messages.append(messages_item)

        total_messages = self.total_messages

        returned_messages = self.returned_messages

        has_more = self.has_more

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "session_id": session_id,
                "messages": messages,
                "total_messages": total_messages,
                "returned_messages": returned_messages,
                "has_more": has_more,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.message_history_item import MessageHistoryItem

        d = dict(src_dict)
        session_id = d.pop("session_id")

        messages = []
        _messages = d.pop("messages")
        for messages_item_data in _messages:
            messages_item = MessageHistoryItem.from_dict(messages_item_data)

            messages.append(messages_item)

        total_messages = d.pop("total_messages")

        returned_messages = d.pop("returned_messages")

        has_more = d.pop("has_more")

        get_history_response = cls(
            session_id=session_id,
            messages=messages,
            total_messages=total_messages,
            returned_messages=returned_messages,
            has_more=has_more,
        )

        get_history_response.additional_properties = d
        return get_history_response

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
