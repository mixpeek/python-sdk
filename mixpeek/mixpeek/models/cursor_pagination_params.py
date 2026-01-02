from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pagination_method import PaginationMethod
from ..types import UNSET, Unset

T = TypeVar("T", bound="CursorPaginationParams")


@_attrs_define
class CursorPaginationParams:
    """Cursor-based pagination referencing last seen position.

    Best for: Infinite scroll UIs, mobile apps, real-time feeds

    How it works:
    - First request: cursor=null
    - Response includes next cursor token
    - Next request: pass cursor from previous response
    - Stateless: no server-side state
    - Consistent: no duplicates/gaps even with concurrent writes

    Use when:
    - Building infinite scroll interfaces
    - Users scroll through results sequentially
    - You need consistency across pages
    - You don't need to jump to arbitrary pages

    Example flow:
    1. Request: {"method": "cursor", "limit": 20, "cursor": null}
    2. Response: {"documents": [...], "pagination": {"cursor": "abc123", "has_next": true}}
    3. Request: {"method": "cursor", "limit": 20, "cursor": "abc123"}

        Attributes:
            method (PaginationMethod | Unset): Supported pagination strategies for retriever execution.
            limit (int | Unset): Maximum number of documents to return per page (REQUIRED). Default: 10. Default: 10.
            cursor (None | str | Unset): Opaque base64 cursor from previous response (OPTIONAL). null for first page, then
                use cursor from response.pagination.cursor
    """

    method: PaginationMethod | Unset = UNSET
    limit: int | Unset = 10
    cursor: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method: str | Unset = UNSET
        if not isinstance(self.method, Unset):
            method = self.method.value

        limit = self.limit

        cursor: None | str | Unset
        if isinstance(self.cursor, Unset):
            cursor = UNSET
        else:
            cursor = self.cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if method is not UNSET:
            field_dict["method"] = method
        if limit is not UNSET:
            field_dict["limit"] = limit
        if cursor is not UNSET:
            field_dict["cursor"] = cursor

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

        def _parse_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cursor = _parse_cursor(d.pop("cursor", UNSET))

        cursor_pagination_params = cls(
            method=method,
            limit=limit,
            cursor=cursor,
        )

        cursor_pagination_params.additional_properties = d
        return cursor_pagination_params

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
