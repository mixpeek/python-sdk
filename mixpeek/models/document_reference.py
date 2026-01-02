from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DocumentReference")


@_attrs_define
class DocumentReference:
    """Reference to an existing document to use its pre-computed features.

    Use this to perform similarity search using a document's existing embeddings
    without re-processing the document. The system will fetch the document's
    feature vectors and use them directly for the search.

    Use Cases:
        - "Find documents similar to this one"
        - Reverse image search using indexed images
        - Document-to-document similarity
        - Multi-hop similarity chains

    Examples:
        Find similar documents:
            ```json
            {
                "collection_id": "col_abc123",
                "document_id": "doc_xyz789"
            }
            ```

        Attributes:
            collection_id (None | str | Unset): Collection ID containing the reference document. Can be the same or
                different from the target search collection. Must be accessible within the current namespace. None values are
                handled by on_empty behavior (skip/random/error).
            document_id (None | str | Unset): Document ID to use as similarity reference. The document must exist and have
                feature vectors for the specified feature_uri. If the document doesn't have the required feature, the search
                will fail. None values are handled by on_empty behavior (skip/random/error).
    """

    collection_id: None | str | Unset = UNSET
    document_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        collection_id: None | str | Unset
        if isinstance(self.collection_id, Unset):
            collection_id = UNSET
        else:
            collection_id = self.collection_id

        document_id: None | str | Unset
        if isinstance(self.document_id, Unset):
            document_id = UNSET
        else:
            document_id = self.document_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if collection_id is not UNSET:
            field_dict["collection_id"] = collection_id
        if document_id is not UNSET:
            field_dict["document_id"] = document_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_collection_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        collection_id = _parse_collection_id(d.pop("collection_id", UNSET))

        def _parse_document_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        document_id = _parse_document_id(d.pop("document_id", UNSET))

        document_reference = cls(
            collection_id=collection_id,
            document_id=document_id,
        )

        document_reference.additional_properties = d
        return document_reference

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
