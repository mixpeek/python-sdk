from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.send_message_request_metadata import SendMessageRequestMetadata


T = TypeVar("T", bound="SendMessageRequest")


@_attrs_define
class SendMessageRequest:
    """Request payload for sending a message to the agent.

    Attributes:
        content: Message text content
        metadata: Optional message metadata
        stream: Whether to stream response as SSE (default: True)

    Note:
        When stream=True, the response will be Server-Sent Events (SSE).
        When stream=False, the response will be a MessageResponse object.

    Example:
        ```python
        # Streaming request (SSE)
        request = SendMessageRequest(
            content="Find videos about machine learning",
            stream=True
        )

        # Non-streaming request
        request = SendMessageRequest(
            content="Find videos about machine learning",
            stream=False
        )
        ```

        Attributes:
            content (str): Message text content (REQUIRED)
            metadata (SendMessageRequestMetadata | Unset): Message metadata (OPTIONAL)
            stream (bool | Unset): Stream response as SSE (default: True) Default: True.
    """

    content: str
    metadata: SendMessageRequestMetadata | Unset = UNSET
    stream: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content = self.content

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        stream = self.stream

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if stream is not UNSET:
            field_dict["stream"] = stream

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.send_message_request_metadata import SendMessageRequestMetadata

        d = dict(src_dict)
        content = d.pop("content")

        _metadata = d.pop("metadata", UNSET)
        metadata: SendMessageRequestMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = SendMessageRequestMetadata.from_dict(_metadata)

        stream = d.pop("stream", UNSET)

        send_message_request = cls(
            content=content,
            metadata=metadata,
            stream=stream,
        )

        send_message_request.additional_properties = d
        return send_message_request

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
