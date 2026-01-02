from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SessionQuotas")


@_attrs_define
class SessionQuotas:
    """Session-level quotas and rate limits.

    These limits are enforced per-session to prevent runaway costs.
    All fields are optional - unset means unlimited.

    Attributes:
        max_messages: Maximum messages allowed in session (prevents long conversations)
        max_tokens_total: Maximum cumulative tokens for session (cost control)
        max_tool_calls: Maximum tool calls per session (limits API usage)
        max_session_duration_minutes: Maximum session lifetime in minutes
        rate_limit_messages_per_minute: Max messages per minute (prevents spam)

    Example:
        ```python
        # Basic quotas for a demo session
        quotas = SessionQuotas(
            max_messages=50,
            max_tokens_total=50000,
            max_tool_calls=25
        )

        # Strict quotas for production
        quotas = SessionQuotas(
            max_messages=100,
            max_tokens_total=100000,
            max_tool_calls=50,
            max_session_duration_minutes=60,
            rate_limit_messages_per_minute=10
        )
        ```

        Attributes:
            max_messages (int | None | Unset): Maximum messages allowed in session. Unset = unlimited.
            max_tokens_total (int | None | Unset): Maximum cumulative tokens for session. Unset = unlimited.
            max_tool_calls (int | None | Unset): Maximum tool calls per session. Unset = unlimited.
            max_session_duration_minutes (int | None | Unset): Maximum session lifetime in minutes. Unset = no time limit.
            rate_limit_messages_per_minute (int | None | Unset): Max messages per minute to prevent spam. Unset = unlimited.
    """

    max_messages: int | None | Unset = UNSET
    max_tokens_total: int | None | Unset = UNSET
    max_tool_calls: int | None | Unset = UNSET
    max_session_duration_minutes: int | None | Unset = UNSET
    rate_limit_messages_per_minute: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_messages: int | None | Unset
        if isinstance(self.max_messages, Unset):
            max_messages = UNSET
        else:
            max_messages = self.max_messages

        max_tokens_total: int | None | Unset
        if isinstance(self.max_tokens_total, Unset):
            max_tokens_total = UNSET
        else:
            max_tokens_total = self.max_tokens_total

        max_tool_calls: int | None | Unset
        if isinstance(self.max_tool_calls, Unset):
            max_tool_calls = UNSET
        else:
            max_tool_calls = self.max_tool_calls

        max_session_duration_minutes: int | None | Unset
        if isinstance(self.max_session_duration_minutes, Unset):
            max_session_duration_minutes = UNSET
        else:
            max_session_duration_minutes = self.max_session_duration_minutes

        rate_limit_messages_per_minute: int | None | Unset
        if isinstance(self.rate_limit_messages_per_minute, Unset):
            rate_limit_messages_per_minute = UNSET
        else:
            rate_limit_messages_per_minute = self.rate_limit_messages_per_minute

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_messages is not UNSET:
            field_dict["max_messages"] = max_messages
        if max_tokens_total is not UNSET:
            field_dict["max_tokens_total"] = max_tokens_total
        if max_tool_calls is not UNSET:
            field_dict["max_tool_calls"] = max_tool_calls
        if max_session_duration_minutes is not UNSET:
            field_dict["max_session_duration_minutes"] = max_session_duration_minutes
        if rate_limit_messages_per_minute is not UNSET:
            field_dict["rate_limit_messages_per_minute"] = rate_limit_messages_per_minute

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_max_messages(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_messages = _parse_max_messages(d.pop("max_messages", UNSET))

        def _parse_max_tokens_total(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_tokens_total = _parse_max_tokens_total(d.pop("max_tokens_total", UNSET))

        def _parse_max_tool_calls(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_tool_calls = _parse_max_tool_calls(d.pop("max_tool_calls", UNSET))

        def _parse_max_session_duration_minutes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_session_duration_minutes = _parse_max_session_duration_minutes(d.pop("max_session_duration_minutes", UNSET))

        def _parse_rate_limit_messages_per_minute(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        rate_limit_messages_per_minute = _parse_rate_limit_messages_per_minute(
            d.pop("rate_limit_messages_per_minute", UNSET)
        )

        session_quotas = cls(
            max_messages=max_messages,
            max_tokens_total=max_tokens_total,
            max_tool_calls=max_tool_calls,
            max_session_duration_minutes=max_session_duration_minutes,
            rate_limit_messages_per_minute=rate_limit_messages_per_minute,
        )

        session_quotas.additional_properties = d
        return session_quotas

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
