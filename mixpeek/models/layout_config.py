from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LayoutConfig")


@_attrs_define
class LayoutConfig:
    """Layout configuration for search results display.

    Attributes:
        mode (str | Unset): Display mode for results Default: 'grid'.
        columns (int | Unset): Number of columns for grid/masonry layouts Default: 3.
        gap (str | Unset): Gap between items Default: '16px'.
        full_width (bool | Unset): Whether to use full viewport width for the layout (edge-to-edge) Default: False.
    """

    mode: str | Unset = "grid"
    columns: int | Unset = 3
    gap: str | Unset = "16px"
    full_width: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode = self.mode

        columns = self.columns

        gap = self.gap

        full_width = self.full_width

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mode is not UNSET:
            field_dict["mode"] = mode
        if columns is not UNSET:
            field_dict["columns"] = columns
        if gap is not UNSET:
            field_dict["gap"] = gap
        if full_width is not UNSET:
            field_dict["full_width"] = full_width

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mode = d.pop("mode", UNSET)

        columns = d.pop("columns", UNSET)

        gap = d.pop("gap", UNSET)

        full_width = d.pop("full_width", UNSET)

        layout_config = cls(
            mode=mode,
            columns=columns,
            gap=gap,
            full_width=full_width,
        )

        layout_config.additional_properties = d
        return layout_config

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
