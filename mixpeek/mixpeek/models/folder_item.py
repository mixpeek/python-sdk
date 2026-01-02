from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FolderItem")


@_attrs_define
class FolderItem:
    """Represents a folder in Google Drive for folder selection in sync configuration.

    Used by the list folders endpoint to help users browse and select folders
    for sync operations. Only available for Google Drive connections.

        Attributes:
            id (str): REQUIRED. Folder ID in Google Drive. Use this ID when configuring sync operations. Format: Google
                Drive folder identifier (e.g., '0AH-Xabc123').
            name (str): REQUIRED. Display name of the folder. Human-readable name shown in the Google Drive UI.
            path (str): REQUIRED. Full path from root to this folder. Format: '/' for root, '/FolderName' for first level,
                '/Parent/Child' for nested folders.
            mime_type (str): REQUIRED. MIME type identifier for folders. Always 'application/vnd.google-apps.folder' for
                folders.
    """

    id: str
    name: str
    path: str
    mime_type: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        path = self.path

        mime_type = self.mime_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "path": path,
                "mime_type": mime_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        path = d.pop("path")

        mime_type = d.pop("mime_type")

        folder_item = cls(
            id=id,
            name=name,
            path=path,
            mime_type=mime_type,
        )

        folder_item.additional_properties = d
        return folder_item

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
