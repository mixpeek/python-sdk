from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FileSource")


@_attrs_define
class FileSource:
    """Use the synced file itself as the source (for blob mappings).

    This is the primary source for blob-type mappings where the synced file
    content becomes the blob. The mime_type is automatically detected from
    the file unless explicitly overridden in the BlobMappingEntry.

    Provider Compatibility: All providers (works on any synced file)

    Example usage:
        {"type": "file"} -> The synced file becomes the blob content

    This source type has no additional configuration - it simply indicates
    that the synced file content should be used as the blob data.

    Attributes:
        type: Must be "file" to identify this source type

        Attributes:
            type_ (Literal['file'] | Unset): Source type identifier. Must be 'file' for the synced file itself. Default:
                'file'.
    """

    type_: Literal["file"] | Unset = "file"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal["file"] | Unset, d.pop("type", UNSET))
        if type_ != "file" and not isinstance(type_, Unset):
            raise ValueError(f"type must match const 'file', got '{type_}'")

        file_source = cls(
            type_=type_,
        )

        file_source.additional_properties = d
        return file_source

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
