from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pagination_method import PaginationMethod
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyset_pagination_params_after_type_0 import KeysetPaginationParamsAfterType0


T = TypeVar("T", bound="KeysetPaginationParams")


@_attrs_define
class KeysetPaginationParams:
    """Stateless keyset pagination relying on last seen sort key.

    Best for: High-performance pagination, large result sets, stable sorting

    How it works:
    - Uses actual field values as pagination markers
    - Database can use indexes efficiently (WHERE score < 0.73)
    - No offset calculation or server state
    - Requires deterministic sort order (e.g., score DESC, id ASC)
    - Most efficient pagination method

    Requirements:
    - Results must be sorted consistently
    - Sort fields must be in the "after" marker
    - Example: sorted by (score DESC, id ASC) → after: {score: 0.73, id: "doc_20"}

    Advantages:
    - No server-side state (truly stateless)
    - Consistent even with concurrent writes
    - Database can use indexes (fast for large datasets)
    - No offset performance degradation

    Use when:
    - You have stable, deterministic sort fields
    - Working with large result sets (10k+ docs)
    - Maximum performance is critical
    - You need infinite scroll with best efficiency

    Example flow:
    1. Request: {"method": "keyset", "limit": 20, "after": null}
    2. Response: {"documents": [...], "next_cursor": {"score": 0.85, "id": "doc_20"}}
    3. Request: {"method": "keyset", "limit": 20, "after": {"score": 0.85, "id": "doc_20"}}

        Attributes:
            method (PaginationMethod | Unset): Supported pagination strategies for retriever execution.
            limit (int | Unset): Maximum number of documents to return per page (REQUIRED). Default: 10. Default: 10.
            after (KeysetPaginationParamsAfterType0 | None | Unset): Last seen keyset marker from previous response
                (OPTIONAL). Must include all sort fields. Example: {'score': 0.73, 'id': 'doc_20'}. null for first page, then
                use next_cursor from response
    """

    method: PaginationMethod | Unset = UNSET
    limit: int | Unset = 10
    after: KeysetPaginationParamsAfterType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.keyset_pagination_params_after_type_0 import KeysetPaginationParamsAfterType0

        method: str | Unset = UNSET
        if not isinstance(self.method, Unset):
            method = self.method.value

        limit = self.limit

        after: dict[str, Any] | None | Unset
        if isinstance(self.after, Unset):
            after = UNSET
        elif isinstance(self.after, KeysetPaginationParamsAfterType0):
            after = self.after.to_dict()
        else:
            after = self.after

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if method is not UNSET:
            field_dict["method"] = method
        if limit is not UNSET:
            field_dict["limit"] = limit
        if after is not UNSET:
            field_dict["after"] = after

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.keyset_pagination_params_after_type_0 import KeysetPaginationParamsAfterType0

        d = dict(src_dict)
        _method = d.pop("method", UNSET)
        method: PaginationMethod | Unset
        if isinstance(_method, Unset):
            method = UNSET
        else:
            method = PaginationMethod(_method)

        limit = d.pop("limit", UNSET)

        def _parse_after(data: object) -> KeysetPaginationParamsAfterType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                after_type_0 = KeysetPaginationParamsAfterType0.from_dict(data)

                return after_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(KeysetPaginationParamsAfterType0 | None | Unset, data)

        after = _parse_after(d.pop("after", UNSET))

        keyset_pagination_params = cls(
            method=method,
            limit=limit,
            after=after,
        )

        keyset_pagination_params.additional_properties = d
        return keyset_pagination_params

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
