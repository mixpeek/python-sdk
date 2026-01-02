from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.document_response import DocumentResponse


T = TypeVar("T", bound="DocumentGroup")


@_attrs_define
class DocumentGroup:
    """A group of documents with the same field value.

    Used when group_by parameter is specified in ListDocumentsRequest.

        Attributes:
            group_key (Any): The value that documents in this group share for the group_by field. Can be string, number,
                boolean, or null depending on the field type. Examples: 'obj_video123' (for source_object_id), 'Electronics'
                (for metadata.category).
            documents (list[DocumentResponse]): List of documents that share the same group_key value. Documents within each
                group are sorted by relevance/score if applicable. Each document contains full document data including metadata,
                lineage, and blobs.
            count (int): Number of documents in this group.
    """

    group_key: Any
    documents: list[DocumentResponse]
    count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group_key = self.group_key

        documents = []
        for documents_item_data in self.documents:
            documents_item = documents_item_data.to_dict()
            documents.append(documents_item)

        count = self.count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "group_key": group_key,
                "documents": documents,
                "count": count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.document_response import DocumentResponse

        d = dict(src_dict)
        group_key = d.pop("group_key")

        documents = []
        _documents = d.pop("documents")
        for documents_item_data in _documents:
            documents_item = DocumentResponse.from_dict(documents_item_data)

            documents.append(documents_item)

        count = d.pop("count")

        document_group = cls(
            group_key=group_key,
            documents=documents,
            count=count,
        )

        document_group.additional_properties = d
        return document_group

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
