from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FolderPathSource")


@_attrs_define
class FolderPathSource:
    """Extract value from the folder path structure.

    Useful for deriving categories or metadata from folder organization.
    Can extract the full path, a specific segment, or the immediate parent.

    Provider Compatibility: All providers with folder/prefix structure

    Example folder structure: /Marketing/Campaigns/Q4-2024/videos/
        - segment=0 -> "Marketing"
        - segment=1 -> "Campaigns"
        - segment=2 -> "Q4-2024"
        - segment=-1 -> "videos" (last segment)
        - full_path=True -> "Marketing/Campaigns/Q4-2024/videos"
        - Neither (default) -> "videos" (immediate parent)

    Use Cases:
        - Derive category from top-level folder
        - Extract project name from folder structure
        - Preserve full path for hierarchical organization

    Attributes:
        type: Must be "folder_path" to identify this source type
        segment: Index of path segment to extract (0-based, negative for reverse)
        full_path: Whether to extract complete path

        Attributes:
            type_ (Literal['folder_path'] | Unset): Source type identifier. Must be 'folder_path' for path extraction.
                Default: 'folder_path'.
            segment (int | None | Unset): Extract a specific path segment by index. 0 = first segment (root folder), 1 =
                second segment, etc. -1 = last segment (immediate parent), -2 = second to last, etc. If None and full_path is
                False, extracts the immediate parent folder.
            full_path (bool | Unset): If True, extracts the complete folder path (joined with '/'). If False, extracts only
                the segment specified or immediate parent. Does not include the filename. Default: False.
    """

    type_: Literal["folder_path"] | Unset = "folder_path"
    segment: int | None | Unset = UNSET
    full_path: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        segment: int | None | Unset
        if isinstance(self.segment, Unset):
            segment = UNSET
        else:
            segment = self.segment

        full_path = self.full_path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if segment is not UNSET:
            field_dict["segment"] = segment
        if full_path is not UNSET:
            field_dict["full_path"] = full_path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal["folder_path"] | Unset, d.pop("type", UNSET))
        if type_ != "folder_path" and not isinstance(type_, Unset):
            raise ValueError(f"type must match const 'folder_path', got '{type_}'")

        def _parse_segment(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        segment = _parse_segment(d.pop("segment", UNSET))

        full_path = d.pop("full_path", UNSET)

        folder_path_source = cls(
            type_=type_,
            segment=segment,
            full_path=full_path,
        )

        folder_path_source.additional_properties = d
        return folder_path_source

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
