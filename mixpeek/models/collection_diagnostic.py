from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CollectionDiagnostic")


@_attrs_define
class CollectionDiagnostic:
    """Diagnostic information for a collection.

    Attributes:
        collection_id (str): Collection ID
        collection_name (str): Collection name
        status (str): Collection status (ready, processing, empty)
        document_count (int | Unset): Number of documents in collection Default: 0.
        expected_documents (int | None | Unset): Expected document count
    """

    collection_id: str
    collection_name: str
    status: str
    document_count: int | Unset = 0
    expected_documents: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        collection_id = self.collection_id

        collection_name = self.collection_name

        status = self.status

        document_count = self.document_count

        expected_documents: int | None | Unset
        if isinstance(self.expected_documents, Unset):
            expected_documents = UNSET
        else:
            expected_documents = self.expected_documents

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "collection_id": collection_id,
                "collection_name": collection_name,
                "status": status,
            }
        )
        if document_count is not UNSET:
            field_dict["document_count"] = document_count
        if expected_documents is not UNSET:
            field_dict["expected_documents"] = expected_documents

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        collection_id = d.pop("collection_id")

        collection_name = d.pop("collection_name")

        status = d.pop("status")

        document_count = d.pop("document_count", UNSET)

        def _parse_expected_documents(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        expected_documents = _parse_expected_documents(d.pop("expected_documents", UNSET))

        collection_diagnostic = cls(
            collection_id=collection_id,
            collection_name=collection_name,
            status=status,
            document_count=document_count,
            expected_documents=expected_documents,
        )

        collection_diagnostic.additional_properties = d
        return collection_diagnostic

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
