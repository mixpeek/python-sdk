from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.folder_item import FolderItem


T = TypeVar("T", bound="ListFoldersResponse")


@_attrs_define
class ListFoldersResponse:
    """Response payload for listing Google Drive folders.

    Returns a list of folders available at the specified path, enabling users
    to browse and select folders for sync configuration.

        Attributes:
            results (list[FolderItem]): List of folders found at the specified parent path. Only includes folders (not
                files). Empty list if no folders found or path doesn't exist.
            parent_path (str): The parent folder path that was queried. This is the path specified in the request (or '/'
                for root). Use this to show breadcrumb navigation in UI.
    """

    results: list[FolderItem]
    parent_path: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        parent_path = self.parent_path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "results": results,
                "parent_path": parent_path,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.folder_item import FolderItem

        d = dict(src_dict)
        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = FolderItem.from_dict(results_item_data)

            results.append(results_item)

        parent_path = d.pop("parent_path")

        list_folders_response = cls(
            results=results,
            parent_path=parent_path,
        )

        list_folders_response.additional_properties = d
        return list_folders_response

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
