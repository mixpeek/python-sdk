from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="MessageHistoryItem")


@_attrs_define
class MessageHistoryItem:
    """Single message in conversation history.

    Attributes:
        message_id: Message identifier
        role: Message role (user, assistant, tool)
        content: Message text content
        content_type: Content type (text, tool_call, tool_result)
        tool_name: Tool name (if tool message)
        tool_inputs: Tool inputs (if tool call)
        tool_outputs: Tool outputs (if tool result)
        tool_status: Tool execution status (if tool message)
        timestamp: Message timestamp

        Attributes:
            message_id (str): Message identifier
            role (str): Message role
            content (str): Message content
            content_type (str): Content type
            timestamp (datetime.datetime): Message timestamp
            tool_name (None | str | Unset): Tool name (if tool message)
            tool_inputs (None | str | Unset): Tool inputs (if tool call)
            tool_outputs (None | str | Unset): Tool outputs (if tool result)
            tool_status (None | str | Unset): Tool status (if tool message)
    """

    message_id: str
    role: str
    content: str
    content_type: str
    timestamp: datetime.datetime
    tool_name: None | str | Unset = UNSET
    tool_inputs: None | str | Unset = UNSET
    tool_outputs: None | str | Unset = UNSET
    tool_status: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message_id = self.message_id

        role = self.role

        content = self.content

        content_type = self.content_type

        timestamp = self.timestamp.isoformat()

        tool_name: None | str | Unset
        if isinstance(self.tool_name, Unset):
            tool_name = UNSET
        else:
            tool_name = self.tool_name

        tool_inputs: None | str | Unset
        if isinstance(self.tool_inputs, Unset):
            tool_inputs = UNSET
        else:
            tool_inputs = self.tool_inputs

        tool_outputs: None | str | Unset
        if isinstance(self.tool_outputs, Unset):
            tool_outputs = UNSET
        else:
            tool_outputs = self.tool_outputs

        tool_status: None | str | Unset
        if isinstance(self.tool_status, Unset):
            tool_status = UNSET
        else:
            tool_status = self.tool_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message_id": message_id,
                "role": role,
                "content": content,
                "content_type": content_type,
                "timestamp": timestamp,
            }
        )
        if tool_name is not UNSET:
            field_dict["tool_name"] = tool_name
        if tool_inputs is not UNSET:
            field_dict["tool_inputs"] = tool_inputs
        if tool_outputs is not UNSET:
            field_dict["tool_outputs"] = tool_outputs
        if tool_status is not UNSET:
            field_dict["tool_status"] = tool_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message_id = d.pop("message_id")

        role = d.pop("role")

        content = d.pop("content")

        content_type = d.pop("content_type")

        timestamp = isoparse(d.pop("timestamp"))

        def _parse_tool_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tool_name = _parse_tool_name(d.pop("tool_name", UNSET))

        def _parse_tool_inputs(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tool_inputs = _parse_tool_inputs(d.pop("tool_inputs", UNSET))

        def _parse_tool_outputs(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tool_outputs = _parse_tool_outputs(d.pop("tool_outputs", UNSET))

        def _parse_tool_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tool_status = _parse_tool_status(d.pop("tool_status", UNSET))

        message_history_item = cls(
            message_id=message_id,
            role=role,
            content=content,
            content_type=content_type,
            timestamp=timestamp,
            tool_name=tool_name,
            tool_inputs=tool_inputs,
            tool_outputs=tool_outputs,
            tool_status=tool_status,
        )

        message_history_item.additional_properties = d
        return message_history_item

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
