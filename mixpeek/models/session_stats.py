from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SessionStats")


@_attrs_define
class SessionStats:
    """Session usage statistics.

    Tracked in MongoDB session document, updated on each message.
    Use this to display usage metrics in your UI.

    Attributes:
        total_messages: Total messages sent in session
        total_tokens: Cumulative tokens used (for cost tracking)
        total_tool_calls: Total tool invocations
        avg_latency_ms: Average message latency in milliseconds

    Example:
        ```python
        # Display in UI
        stats = session_response.stats
        print(f"Messages: {stats.total_messages}")
        print(f"Tokens used: {stats.total_tokens}")
        print(f"Tool calls: {stats.total_tool_calls}")
        print(f"Avg latency: {stats.avg_latency_ms:.0f}ms")
        ```

        Attributes:
            total_messages (int | Unset): Total messages sent in session Default: 0.
            total_tokens (int | Unset): Cumulative tokens used (for cost tracking) Default: 0.
            total_tool_calls (int | Unset): Total tool invocations Default: 0.
            avg_latency_ms (float | Unset): Average message latency in milliseconds Default: 0.0.
    """

    total_messages: int | Unset = 0
    total_tokens: int | Unset = 0
    total_tool_calls: int | Unset = 0
    avg_latency_ms: float | Unset = 0.0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_messages = self.total_messages

        total_tokens = self.total_tokens

        total_tool_calls = self.total_tool_calls

        avg_latency_ms = self.avg_latency_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_messages is not UNSET:
            field_dict["total_messages"] = total_messages
        if total_tokens is not UNSET:
            field_dict["total_tokens"] = total_tokens
        if total_tool_calls is not UNSET:
            field_dict["total_tool_calls"] = total_tool_calls
        if avg_latency_ms is not UNSET:
            field_dict["avg_latency_ms"] = avg_latency_ms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_messages = d.pop("total_messages", UNSET)

        total_tokens = d.pop("total_tokens", UNSET)

        total_tool_calls = d.pop("total_tool_calls", UNSET)

        avg_latency_ms = d.pop("avg_latency_ms", UNSET)

        session_stats = cls(
            total_messages=total_messages,
            total_tokens=total_tokens,
            total_tool_calls=total_tool_calls,
            avg_latency_ms=avg_latency_ms,
        )

        session_stats.additional_properties = d
        return session_stats

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
