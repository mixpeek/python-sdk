from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.batch_document_update_update_data import BatchDocumentUpdateUpdateData


T = TypeVar("T", bound="BatchDocumentUpdate")


@_attrs_define
class BatchDocumentUpdate:
    """Single document update specification for batch operations.

    Represents one document's update within a batch request.

        Attributes:
            document_id (str): REQUIRED. Document ID to update. Must exist in the collection. Format: 'doc_' prefix +
                alphanumeric characters.
            update_data (BatchDocumentUpdateUpdateData): REQUIRED. Fields to update for this specific document. Can update
                any document field except vectors. Supported fields: metadata, source_blobs, document_blobs, lineage fields
                (root_object_id, source_type, etc.), and any custom fields. Each document in the batch can have different
                update_data.
    """

    document_id: str
    update_data: BatchDocumentUpdateUpdateData
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        document_id = self.document_id

        update_data = self.update_data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "document_id": document_id,
                "update_data": update_data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.batch_document_update_update_data import BatchDocumentUpdateUpdateData

        d = dict(src_dict)
        document_id = d.pop("document_id")

        update_data = BatchDocumentUpdateUpdateData.from_dict(d.pop("update_data"))

        batch_document_update = cls(
            document_id=document_id,
            update_data=update_data,
        )

        batch_document_update.additional_properties = d
        return batch_document_update

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
