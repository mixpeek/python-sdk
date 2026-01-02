from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FieldFormatOptions")


@_attrs_define
class FieldFormatOptions:
    """Format-specific options for field display.

    Different format types support different options:
    - text: label, truncate_chars, show_empty
    - image: width, height, lazy_load, aspect_ratio, object_fit
    - date: label, date_format (iso, relative, custom)
    - number: label, decimals, prefix, suffix, show_empty
    - url: label, open_in_new_tab, show_domain
    - boolean: label, true_label, false_label
    - array: label, separator, max_items

        Attributes:
            label (None | str | Unset): Display label for this field
            show_empty (bool | Unset): Whether to show the field if value is empty/null Default: True.
            truncate_chars (int | None | Unset): Maximum characters before truncation (for text fields)
            width (int | None | Unset): Image width in pixels
            height (int | None | Unset): Image height in pixels
            lazy_load (bool | Unset): Enable lazy loading for images (default: true) Default: True.
            aspect_ratio (None | str | Unset): Aspect ratio for image container
            object_fit (str | Unset): CSS object-fit property for images Default: 'cover'.
            date_format (str | Unset): Date format type: 'iso', 'relative', or custom format string Default: 'relative'.
            decimals (int | None | Unset): Number of decimal places
            prefix (None | str | Unset): Prefix for number display
            suffix (None | str | Unset): Suffix for number display
            open_in_new_tab (bool | Unset): Open URLs in new tab (default: true) Default: True.
            show_domain (bool | Unset): Show domain instead of full URL Default: False.
            true_label (str | Unset): Label for true values Default: 'Yes'.
            false_label (str | Unset): Label for false values Default: 'No'.
            separator (str | Unset): Separator for array items (default: ', ') Default: ', '.
            max_items (int | None | Unset): Maximum array items to display
    """

    label: None | str | Unset = UNSET
    show_empty: bool | Unset = True
    truncate_chars: int | None | Unset = UNSET
    width: int | None | Unset = UNSET
    height: int | None | Unset = UNSET
    lazy_load: bool | Unset = True
    aspect_ratio: None | str | Unset = UNSET
    object_fit: str | Unset = "cover"
    date_format: str | Unset = "relative"
    decimals: int | None | Unset = UNSET
    prefix: None | str | Unset = UNSET
    suffix: None | str | Unset = UNSET
    open_in_new_tab: bool | Unset = True
    show_domain: bool | Unset = False
    true_label: str | Unset = "Yes"
    false_label: str | Unset = "No"
    separator: str | Unset = ", "
    max_items: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        show_empty = self.show_empty

        truncate_chars: int | None | Unset
        if isinstance(self.truncate_chars, Unset):
            truncate_chars = UNSET
        else:
            truncate_chars = self.truncate_chars

        width: int | None | Unset
        if isinstance(self.width, Unset):
            width = UNSET
        else:
            width = self.width

        height: int | None | Unset
        if isinstance(self.height, Unset):
            height = UNSET
        else:
            height = self.height

        lazy_load = self.lazy_load

        aspect_ratio: None | str | Unset
        if isinstance(self.aspect_ratio, Unset):
            aspect_ratio = UNSET
        else:
            aspect_ratio = self.aspect_ratio

        object_fit = self.object_fit

        date_format = self.date_format

        decimals: int | None | Unset
        if isinstance(self.decimals, Unset):
            decimals = UNSET
        else:
            decimals = self.decimals

        prefix: None | str | Unset
        if isinstance(self.prefix, Unset):
            prefix = UNSET
        else:
            prefix = self.prefix

        suffix: None | str | Unset
        if isinstance(self.suffix, Unset):
            suffix = UNSET
        else:
            suffix = self.suffix

        open_in_new_tab = self.open_in_new_tab

        show_domain = self.show_domain

        true_label = self.true_label

        false_label = self.false_label

        separator = self.separator

        max_items: int | None | Unset
        if isinstance(self.max_items, Unset):
            max_items = UNSET
        else:
            max_items = self.max_items

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if label is not UNSET:
            field_dict["label"] = label
        if show_empty is not UNSET:
            field_dict["show_empty"] = show_empty
        if truncate_chars is not UNSET:
            field_dict["truncate_chars"] = truncate_chars
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if lazy_load is not UNSET:
            field_dict["lazy_load"] = lazy_load
        if aspect_ratio is not UNSET:
            field_dict["aspect_ratio"] = aspect_ratio
        if object_fit is not UNSET:
            field_dict["object_fit"] = object_fit
        if date_format is not UNSET:
            field_dict["date_format"] = date_format
        if decimals is not UNSET:
            field_dict["decimals"] = decimals
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if suffix is not UNSET:
            field_dict["suffix"] = suffix
        if open_in_new_tab is not UNSET:
            field_dict["open_in_new_tab"] = open_in_new_tab
        if show_domain is not UNSET:
            field_dict["show_domain"] = show_domain
        if true_label is not UNSET:
            field_dict["true_label"] = true_label
        if false_label is not UNSET:
            field_dict["false_label"] = false_label
        if separator is not UNSET:
            field_dict["separator"] = separator
        if max_items is not UNSET:
            field_dict["max_items"] = max_items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))

        show_empty = d.pop("show_empty", UNSET)

        def _parse_truncate_chars(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        truncate_chars = _parse_truncate_chars(d.pop("truncate_chars", UNSET))

        def _parse_width(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        width = _parse_width(d.pop("width", UNSET))

        def _parse_height(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        height = _parse_height(d.pop("height", UNSET))

        lazy_load = d.pop("lazy_load", UNSET)

        def _parse_aspect_ratio(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        aspect_ratio = _parse_aspect_ratio(d.pop("aspect_ratio", UNSET))

        object_fit = d.pop("object_fit", UNSET)

        date_format = d.pop("date_format", UNSET)

        def _parse_decimals(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        decimals = _parse_decimals(d.pop("decimals", UNSET))

        def _parse_prefix(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        prefix = _parse_prefix(d.pop("prefix", UNSET))

        def _parse_suffix(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        suffix = _parse_suffix(d.pop("suffix", UNSET))

        open_in_new_tab = d.pop("open_in_new_tab", UNSET)

        show_domain = d.pop("show_domain", UNSET)

        true_label = d.pop("true_label", UNSET)

        false_label = d.pop("false_label", UNSET)

        separator = d.pop("separator", UNSET)

        def _parse_max_items(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_items = _parse_max_items(d.pop("max_items", UNSET))

        field_format_options = cls(
            label=label,
            show_empty=show_empty,
            truncate_chars=truncate_chars,
            width=width,
            height=height,
            lazy_load=lazy_load,
            aspect_ratio=aspect_ratio,
            object_fit=object_fit,
            date_format=date_format,
            decimals=decimals,
            prefix=prefix,
            suffix=suffix,
            open_in_new_tab=open_in_new_tab,
            show_domain=show_domain,
            true_label=true_label,
            false_label=false_label,
            separator=separator,
            max_items=max_items,
        )

        field_format_options.additional_properties = d
        return field_format_options

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
