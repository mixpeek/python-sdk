from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.internal_payload_model import InternalPayloadModel


T = TypeVar("T", bound="DocumentResponse")


@_attrs_define
class DocumentResponse:
    """Response model for a single document.

    This is the standard response format when fetching documents via API endpoints.
    Contains all document data plus optional presigned URLs for S3 blobs.

    The document payload structure follows native Qdrant format:
        - System fields are stored in `_internal` (lineage, metadata, blobs, etc.)
        - User fields are at root level (brand_name, thumbnail_url, etc.)
        - Only document_id and collection_id are Mixpeek IDs at root level
        - No duplication between root and _internal

    Query Parameters Affecting Response:
        - return_url=true: Adds presigned_url to each document_blobs entry
        - return_vectors=true: Includes embedding arrays in response

    Use Cases:
        - Display document details in UI
        - Download source files or generated artifacts
        - Understand document provenance and processing
        - Access enrichment fields (flat) for filtering/display

        Attributes:
            document_id (str): REQUIRED. Unique identifier for the document. Format: 'doc_' prefix + alphanumeric
                characters. Use for: API queries, references, filtering.
            collection_id (str): REQUIRED. ID of the collection this document belongs to. Format: 'col_' prefix +
                alphanumeric characters. Use for: Collection-scoped queries, filtering.
            field_internal (InternalPayloadModel | None | Unset): System-managed internal fields. Contains all Mixpeek-
                managed metadata including lineage, processing info, timestamps, and blob references. User-defined fields appear
                at root level alongside document_id and collection_id.
    """

    document_id: str
    collection_id: str
    field_internal: InternalPayloadModel | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.internal_payload_model import InternalPayloadModel

        document_id = self.document_id

        collection_id = self.collection_id

        field_internal: dict[str, Any] | None | Unset
        if isinstance(self.field_internal, Unset):
            field_internal = UNSET
        elif isinstance(self.field_internal, InternalPayloadModel):
            field_internal = self.field_internal.to_dict()
        else:
            field_internal = self.field_internal

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "document_id": document_id,
                "collection_id": collection_id,
            }
        )
        if field_internal is not UNSET:
            field_dict["_internal"] = field_internal

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.internal_payload_model import InternalPayloadModel

        d = dict(src_dict)
        document_id = d.pop("document_id")

        collection_id = d.pop("collection_id")

        def _parse_field_internal(data: object) -> InternalPayloadModel | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                field_internal_type_0 = InternalPayloadModel.from_dict(data)

                return field_internal_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InternalPayloadModel | None | Unset, data)

        field_internal = _parse_field_internal(d.pop("_internal", UNSET))

        document_response = cls(
            document_id=document_id,
            collection_id=collection_id,
            field_internal=field_internal,
        )

        document_response.additional_properties = d
        return document_response

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
