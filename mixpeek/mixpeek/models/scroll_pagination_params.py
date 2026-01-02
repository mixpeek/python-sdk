from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pagination_method import PaginationMethod
from ..types import UNSET, Unset

T = TypeVar("T", bound="ScrollPaginationParams")


@_attrs_define
class ScrollPaginationParams:
    """Scroll-style pagination maintaining server-side context for TTL.

    Best for: Bulk exports, batch processing, iterating through all results

    How it works:
    - Server maintains a snapshot of results
    - First request: scroll_id=null, returns scroll_id
    - Subsequent requests: use scroll_id from response
    - Context expires after scroll_ttl seconds
    - Consistent view of data (point-in-time snapshot)

    Tradeoffs:
    - Requires server-side state (memory/cache)
    - TTL means sessions can expire
    - Not suitable for long-lived sessions
    - Good for background jobs, not user-facing UIs

    Use when:
    - Exporting large datasets
    - Batch processing all results
    - Background jobs iterating through results
    - You need consistent point-in-time view

    Example flow:
    1. Request: {"method": "scroll", "limit": 100, "scroll_id": null}
    2. Response: {"documents": [...], "scroll_id": "xyz789", "has_next": true}
    3. Request: {"method": "scroll", "limit": 100, "scroll_id": "xyz789"}

        Attributes:
            method (PaginationMethod | Unset): Supported pagination strategies for retriever execution.
            limit (int | Unset): Number of documents to fetch per scroll page (REQUIRED). Default: 100. Default: 100.
            scroll_id (None | str | Unset): Server-issued scroll session identifier (OPTIONAL). null for first request, then
                use scroll_id from response
            scroll_ttl (int | Unset): Seconds to keep scroll context alive (REQUIRED). Default: 300 (5 minutes). Default:
                300.
    """

    method: PaginationMethod | Unset = UNSET
    limit: int | Unset = 100
    scroll_id: None | str | Unset = UNSET
    scroll_ttl: int | Unset = 300
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method: str | Unset = UNSET
        if not isinstance(self.method, Unset):
            method = self.method.value

        limit = self.limit

        scroll_id: None | str | Unset
        if isinstance(self.scroll_id, Unset):
            scroll_id = UNSET
        else:
            scroll_id = self.scroll_id

        scroll_ttl = self.scroll_ttl

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if method is not UNSET:
            field_dict["method"] = method
        if limit is not UNSET:
            field_dict["limit"] = limit
        if scroll_id is not UNSET:
            field_dict["scroll_id"] = scroll_id
        if scroll_ttl is not UNSET:
            field_dict["scroll_ttl"] = scroll_ttl

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _method = d.pop("method", UNSET)
        method: PaginationMethod | Unset
        if isinstance(_method, Unset):
            method = UNSET
        else:
            method = PaginationMethod(_method)

        limit = d.pop("limit", UNSET)

        def _parse_scroll_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scroll_id = _parse_scroll_id(d.pop("scroll_id", UNSET))

        scroll_ttl = d.pop("scroll_ttl", UNSET)

        scroll_pagination_params = cls(
            method=method,
            limit=limit,
            scroll_id=scroll_id,
            scroll_ttl=scroll_ttl,
        )

        scroll_pagination_params.additional_properties = d
        return scroll_pagination_params

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
