from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pagination_method import PaginationMethod
from ..types import UNSET, Unset

T = TypeVar("T", bound="OffsetPaginationParams")


@_attrs_define
class OffsetPaginationParams:
    """Offset-based pagination using page number sizing.

    Best for: Traditional page UIs with page number navigation

    How it works:
    - Uses page numbers (1, 2, 3...) and page size
    - Calculates offset as: (page_number - 1) * page_size
    - Simple and familiar for users
    - Can jump to any page directly

    Tradeoffs:
    - Can have "page drift" if data changes between requests
    - Example: Items added/deleted causes duplicates or gaps
    - Less efficient for large offsets (database must skip N rows)

    Use when:
    - Building traditional page-numbered UIs
    - Users need to jump to specific pages
    - Result set is relatively stable
    - Working with smaller datasets

    Example:
    Page 1: {"method": "offset", "page_size": 25, "page_number": 1}
    Page 2: {"method": "offset", "page_size": 25, "page_number": 2}

        Attributes:
            method (PaginationMethod | Unset): Supported pagination strategies for retriever execution.
            page_size (int | Unset): Number of documents per page (REQUIRED). Default: 10. Default: 10.
            page_number (int | Unset): 1-based page index to retrieve (REQUIRED). Default: 1. Default: 1.
    """

    method: PaginationMethod | Unset = UNSET
    page_size: int | Unset = 10
    page_number: int | Unset = 1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method: str | Unset = UNSET
        if not isinstance(self.method, Unset):
            method = self.method.value

        page_size = self.page_size

        page_number = self.page_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if method is not UNSET:
            field_dict["method"] = method
        if page_size is not UNSET:
            field_dict["page_size"] = page_size
        if page_number is not UNSET:
            field_dict["page_number"] = page_number

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

        page_size = d.pop("page_size", UNSET)

        page_number = d.pop("page_number", UNSET)

        offset_pagination_params = cls(
            method=method,
            page_size=page_size,
            page_number=page_number,
        )

        offset_pagination_params.additional_properties = d
        return offset_pagination_params

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
