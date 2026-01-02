from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sort_direction import SortDirection
from ..types import UNSET, Unset

T = TypeVar("T", bound="SortOption")


@_attrs_define
class SortOption:
    """Specifies how to sort query results.

    Attributes:
        field: Field to sort by
        direction: Sort direction (ascending or descending)

        Attributes:
            field (str): Field to sort by, supports dot notation for nested fields Example: created_at.
            direction (SortDirection | Unset): Sort direction options.
    """

    field: str
    direction: SortDirection | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field = self.field

        direction: str | Unset = UNSET
        if not isinstance(self.direction, Unset):
            direction = self.direction.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "field": field,
            }
        )
        if direction is not UNSET:
            field_dict["direction"] = direction

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field = d.pop("field")

        _direction = d.pop("direction", UNSET)
        direction: SortDirection | Unset
        if isinstance(_direction, Unset):
            direction = UNSET
        else:
            direction = SortDirection(_direction)

        sort_option = cls(
            field=field,
            direction=direction,
        )

        sort_option.additional_properties = d
        return sort_option

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
