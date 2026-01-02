from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.diff_item import DiffItem


T = TypeVar("T", bound="DiffResult")


@_attrs_define
class DiffResult:
    """Result of comparing manifest to current state.

    Attributes:
        to_create (list[DiffItem] | Unset): Resources in manifest but not in system
        in_system_only (list[DiffItem] | Unset): Resources in system but not in manifest
        differences (list[DiffItem] | Unset): Resources in both with differences
    """

    to_create: list[DiffItem] | Unset = UNSET
    in_system_only: list[DiffItem] | Unset = UNSET
    differences: list[DiffItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        to_create: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.to_create, Unset):
            to_create = []
            for to_create_item_data in self.to_create:
                to_create_item = to_create_item_data.to_dict()
                to_create.append(to_create_item)

        in_system_only: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.in_system_only, Unset):
            in_system_only = []
            for in_system_only_item_data in self.in_system_only:
                in_system_only_item = in_system_only_item_data.to_dict()
                in_system_only.append(in_system_only_item)

        differences: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.differences, Unset):
            differences = []
            for differences_item_data in self.differences:
                differences_item = differences_item_data.to_dict()
                differences.append(differences_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if to_create is not UNSET:
            field_dict["to_create"] = to_create
        if in_system_only is not UNSET:
            field_dict["in_system_only"] = in_system_only
        if differences is not UNSET:
            field_dict["differences"] = differences

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.diff_item import DiffItem

        d = dict(src_dict)
        _to_create = d.pop("to_create", UNSET)
        to_create: list[DiffItem] | Unset = UNSET
        if _to_create is not UNSET:
            to_create = []
            for to_create_item_data in _to_create:
                to_create_item = DiffItem.from_dict(to_create_item_data)

                to_create.append(to_create_item)

        _in_system_only = d.pop("in_system_only", UNSET)
        in_system_only: list[DiffItem] | Unset = UNSET
        if _in_system_only is not UNSET:
            in_system_only = []
            for in_system_only_item_data in _in_system_only:
                in_system_only_item = DiffItem.from_dict(in_system_only_item_data)

                in_system_only.append(in_system_only_item)

        _differences = d.pop("differences", UNSET)
        differences: list[DiffItem] | Unset = UNSET
        if _differences is not UNSET:
            differences = []
            for differences_item_data in _differences:
                differences_item = DiffItem.from_dict(differences_item_data)

                differences.append(differences_item)

        diff_result = cls(
            to_create=to_create,
            in_system_only=in_system_only,
            differences=differences,
        )

        diff_result.additional_properties = d
        return diff_result

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
