from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DrivePropertySource")


@_attrs_define
class DrivePropertySource:
    """Extract value from Google Drive file properties.

    Google Drive files have built-in properties (name, mimeType, etc.) and
    custom properties (appProperties). This source extracts from either.

    Provider Compatibility: Google Drive, Google Workspace Shared Drives

    Built-in properties:
        - name: File name
        - mimeType: MIME type
        - description: File description
        - starred: Boolean star status
        - trashed: Boolean trash status
        - createdTime: Creation timestamp
        - modifiedTime: Last modified timestamp
        - size: File size in bytes

    Custom properties: Set via Drive API appProperties field

    Example mapping:
        {"type": "drive_property", "key": "description"} -> extracts file description

    Attributes:
        type: Must be "drive_property" to identify this source type
        key: The property key to extract (case-sensitive)

        Attributes:
            key (str): The property key to extract. Built-in: 'name', 'mimeType', 'description', 'starred', 'createdTime',
                'modifiedTime', 'size', 'webViewLink', 'parents'. Custom: Any key set in the file's appProperties. Case-
                sensitive.
            type_ (Literal['drive_property'] | Unset): Source type identifier. Must be 'drive_property' for Google Drive.
                Default: 'drive_property'.
    """

    key: str
    type_: Literal["drive_property"] | Unset = "drive_property"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        type_ = cast(Literal["drive_property"] | Unset, d.pop("type", UNSET))
        if type_ != "drive_property" and not isinstance(type_, Unset):
            raise ValueError(f"type must match const 'drive_property', got '{type_}'")

        drive_property_source = cls(
            key=key,
            type_=type_,
        )

        drive_property_source.additional_properties = d
        return drive_property_source

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
