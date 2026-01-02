from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PaginationMetadata")


@_attrs_define
class PaginationMetadata:
    """Pagination metadata envelope.

    Attributes:
        total (int): Total number of records
        limit (int): Requested page size
        offset (int): Offset applied to query
        has_next (bool): Whether additional pages exist
    """

    total: int
    limit: int
    offset: int
    has_next: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        limit = self.limit

        offset = self.offset

        has_next = self.has_next

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "limit": limit,
                "offset": offset,
                "has_next": has_next,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total = d.pop("total")

        limit = d.pop("limit")

        offset = d.pop("offset")

        has_next = d.pop("has_next")

        pagination_metadata = cls(
            total=total,
            limit=limit,
            offset=offset,
            has_next=has_next,
        )

        pagination_metadata.additional_properties = d
        return pagination_metadata

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
