from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.field_format_type import FieldFormatType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.field_format_options import FieldFormatOptions


T = TypeVar("T", bound="FieldConfig")


@_attrs_define
class FieldConfig:
    """Configuration for how to display a specific field in results.

    Attributes:
        format_ (FieldFormatType): Supported field format types for result display.
        format_options (FieldFormatOptions | Unset): Format-specific options for field display.

            Different format types support different options:
            - text: label, truncate_chars, show_empty
            - image: width, height, lazy_load, aspect_ratio, object_fit
            - date: label, date_format (iso, relative, custom)
            - number: label, decimals, prefix, suffix, show_empty
            - url: label, open_in_new_tab, show_domain
            - boolean: label, true_label, false_label
            - array: label, separator, max_items
    """

    format_: FieldFormatType
    format_options: FieldFormatOptions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        format_ = self.format_.value

        format_options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.format_options, Unset):
            format_options = self.format_options.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "format": format_,
            }
        )
        if format_options is not UNSET:
            field_dict["format_options"] = format_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.field_format_options import FieldFormatOptions

        d = dict(src_dict)
        format_ = FieldFormatType(d.pop("format"))

        _format_options = d.pop("format_options", UNSET)
        format_options: FieldFormatOptions | Unset
        if isinstance(_format_options, Unset):
            format_options = UNSET
        else:
            format_options = FieldFormatOptions.from_dict(_format_options)

        field_config = cls(
            format_=format_,
            format_options=format_options,
        )

        field_config.additional_properties = d
        return field_config

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
