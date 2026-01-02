from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.internal_lineage_model import InternalLineageModel
    from ..models.internal_payload_model_document_blobs_type_0_item import InternalPayloadModelDocumentBlobsType0Item
    from ..models.internal_payload_model_metadata_type_0 import InternalPayloadModelMetadataType0
    from ..models.internal_payload_model_source_blobs_type_0_item import InternalPayloadModelSourceBlobsType0Item
    from ..models.internal_payload_model_source_details_type_0_item import InternalPayloadModelSourceDetailsType0Item
    from ..models.internal_processing_model import InternalProcessingModel


T = TypeVar("T", bound="InternalPayloadModel")


@_attrs_define
class InternalPayloadModel:
    """Complete _internal field structure for Qdrant document payloads.

    All Mixpeek-managed system fields are namespaced under this structure to:
    - Prevent collision with user-defined fields
    - Provide clear separation of system vs user data
    - Enable filtering on internal fields via _internal.field_name paths

    This structure is stored in Qdrant and returned in API responses.

        Attributes:
            internal_id (None | str | Unset): Organization/tenant identifier for multi-tenancy isolation.
            namespace_id (None | str | Unset): Namespace identifier within the organization.
            document_id (None | str | Unset): Document identifier (also at root level for convenience).
            collection_id (None | str | Unset): Collection identifier (also at root level for convenience).
            created_at (None | str | Unset): ISO 8601 timestamp when document was created.
            updated_at (None | str | Unset): ISO 8601 timestamp when document was last updated.
            lineage (InternalLineageModel | None | Unset): Document lineage and provenance tracking.
            processing (InternalProcessingModel | None | Unset): Processing history and provenance metadata.
            source_blobs (list[InternalPayloadModelSourceBlobsType0Item] | None | Unset): Blobs that constituted the
                original source object.
            document_blobs (list[InternalPayloadModelDocumentBlobsType0Item] | None | Unset): Blobs generated during
                document processing (thumbnails, etc.).
            source_details (list[InternalPayloadModelSourceDetailsType0Item] | None | Unset): Enrichment tracking and source
                detail entries.
            modality (None | str | Unset): Content modality (text, image, video, audio, etc.).
            metadata (InternalPayloadModelMetadataType0 | None | Unset): System metadata including ingestion_status,
                feature_extractor_config_hash, and other processing-related information.
            mime_type (None | str | Unset): MIME type of the source content.
            size_bytes (int | None | Unset): Size of the source content in bytes.
            content_hash (None | str | Unset): SHA256 hash of the source content for deduplication.
    """

    internal_id: None | str | Unset = UNSET
    namespace_id: None | str | Unset = UNSET
    document_id: None | str | Unset = UNSET
    collection_id: None | str | Unset = UNSET
    created_at: None | str | Unset = UNSET
    updated_at: None | str | Unset = UNSET
    lineage: InternalLineageModel | None | Unset = UNSET
    processing: InternalProcessingModel | None | Unset = UNSET
    source_blobs: list[InternalPayloadModelSourceBlobsType0Item] | None | Unset = UNSET
    document_blobs: list[InternalPayloadModelDocumentBlobsType0Item] | None | Unset = UNSET
    source_details: list[InternalPayloadModelSourceDetailsType0Item] | None | Unset = UNSET
    modality: None | str | Unset = UNSET
    metadata: InternalPayloadModelMetadataType0 | None | Unset = UNSET
    mime_type: None | str | Unset = UNSET
    size_bytes: int | None | Unset = UNSET
    content_hash: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.internal_lineage_model import InternalLineageModel
        from ..models.internal_payload_model_metadata_type_0 import InternalPayloadModelMetadataType0
        from ..models.internal_processing_model import InternalProcessingModel

        internal_id: None | str | Unset
        if isinstance(self.internal_id, Unset):
            internal_id = UNSET
        else:
            internal_id = self.internal_id

        namespace_id: None | str | Unset
        if isinstance(self.namespace_id, Unset):
            namespace_id = UNSET
        else:
            namespace_id = self.namespace_id

        document_id: None | str | Unset
        if isinstance(self.document_id, Unset):
            document_id = UNSET
        else:
            document_id = self.document_id

        collection_id: None | str | Unset
        if isinstance(self.collection_id, Unset):
            collection_id = UNSET
        else:
            collection_id = self.collection_id

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        else:
            created_at = self.created_at

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = self.updated_at

        lineage: dict[str, Any] | None | Unset
        if isinstance(self.lineage, Unset):
            lineage = UNSET
        elif isinstance(self.lineage, InternalLineageModel):
            lineage = self.lineage.to_dict()
        else:
            lineage = self.lineage

        processing: dict[str, Any] | None | Unset
        if isinstance(self.processing, Unset):
            processing = UNSET
        elif isinstance(self.processing, InternalProcessingModel):
            processing = self.processing.to_dict()
        else:
            processing = self.processing

        source_blobs: list[dict[str, Any]] | None | Unset
        if isinstance(self.source_blobs, Unset):
            source_blobs = UNSET
        elif isinstance(self.source_blobs, list):
            source_blobs = []
            for source_blobs_type_0_item_data in self.source_blobs:
                source_blobs_type_0_item = source_blobs_type_0_item_data.to_dict()
                source_blobs.append(source_blobs_type_0_item)

        else:
            source_blobs = self.source_blobs

        document_blobs: list[dict[str, Any]] | None | Unset
        if isinstance(self.document_blobs, Unset):
            document_blobs = UNSET
        elif isinstance(self.document_blobs, list):
            document_blobs = []
            for document_blobs_type_0_item_data in self.document_blobs:
                document_blobs_type_0_item = document_blobs_type_0_item_data.to_dict()
                document_blobs.append(document_blobs_type_0_item)

        else:
            document_blobs = self.document_blobs

        source_details: list[dict[str, Any]] | None | Unset
        if isinstance(self.source_details, Unset):
            source_details = UNSET
        elif isinstance(self.source_details, list):
            source_details = []
            for source_details_type_0_item_data in self.source_details:
                source_details_type_0_item = source_details_type_0_item_data.to_dict()
                source_details.append(source_details_type_0_item)

        else:
            source_details = self.source_details

        modality: None | str | Unset
        if isinstance(self.modality, Unset):
            modality = UNSET
        else:
            modality = self.modality

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, InternalPayloadModelMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        mime_type: None | str | Unset
        if isinstance(self.mime_type, Unset):
            mime_type = UNSET
        else:
            mime_type = self.mime_type

        size_bytes: int | None | Unset
        if isinstance(self.size_bytes, Unset):
            size_bytes = UNSET
        else:
            size_bytes = self.size_bytes

        content_hash: None | str | Unset
        if isinstance(self.content_hash, Unset):
            content_hash = UNSET
        else:
            content_hash = self.content_hash

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if internal_id is not UNSET:
            field_dict["internal_id"] = internal_id
        if namespace_id is not UNSET:
            field_dict["namespace_id"] = namespace_id
        if document_id is not UNSET:
            field_dict["document_id"] = document_id
        if collection_id is not UNSET:
            field_dict["collection_id"] = collection_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if lineage is not UNSET:
            field_dict["lineage"] = lineage
        if processing is not UNSET:
            field_dict["processing"] = processing
        if source_blobs is not UNSET:
            field_dict["source_blobs"] = source_blobs
        if document_blobs is not UNSET:
            field_dict["document_blobs"] = document_blobs
        if source_details is not UNSET:
            field_dict["source_details"] = source_details
        if modality is not UNSET:
            field_dict["modality"] = modality
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if mime_type is not UNSET:
            field_dict["mime_type"] = mime_type
        if size_bytes is not UNSET:
            field_dict["size_bytes"] = size_bytes
        if content_hash is not UNSET:
            field_dict["content_hash"] = content_hash

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.internal_lineage_model import InternalLineageModel
        from ..models.internal_payload_model_document_blobs_type_0_item import (
            InternalPayloadModelDocumentBlobsType0Item,
        )
        from ..models.internal_payload_model_metadata_type_0 import InternalPayloadModelMetadataType0
        from ..models.internal_payload_model_source_blobs_type_0_item import InternalPayloadModelSourceBlobsType0Item
        from ..models.internal_payload_model_source_details_type_0_item import (
            InternalPayloadModelSourceDetailsType0Item,
        )
        from ..models.internal_processing_model import InternalProcessingModel

        d = dict(src_dict)

        def _parse_internal_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        internal_id = _parse_internal_id(d.pop("internal_id", UNSET))

        def _parse_namespace_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        namespace_id = _parse_namespace_id(d.pop("namespace_id", UNSET))

        def _parse_document_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        document_id = _parse_document_id(d.pop("document_id", UNSET))

        def _parse_collection_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        collection_id = _parse_collection_id(d.pop("collection_id", UNSET))

        def _parse_created_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_at = _parse_created_at(d.pop("created_at", UNSET))

        def _parse_updated_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))

        def _parse_lineage(data: object) -> InternalLineageModel | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                lineage_type_0 = InternalLineageModel.from_dict(data)

                return lineage_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InternalLineageModel | None | Unset, data)

        lineage = _parse_lineage(d.pop("lineage", UNSET))

        def _parse_processing(data: object) -> InternalProcessingModel | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                processing_type_0 = InternalProcessingModel.from_dict(data)

                return processing_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InternalProcessingModel | None | Unset, data)

        processing = _parse_processing(d.pop("processing", UNSET))

        def _parse_source_blobs(data: object) -> list[InternalPayloadModelSourceBlobsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                source_blobs_type_0 = []
                _source_blobs_type_0 = data
                for source_blobs_type_0_item_data in _source_blobs_type_0:
                    source_blobs_type_0_item = InternalPayloadModelSourceBlobsType0Item.from_dict(
                        source_blobs_type_0_item_data
                    )

                    source_blobs_type_0.append(source_blobs_type_0_item)

                return source_blobs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[InternalPayloadModelSourceBlobsType0Item] | None | Unset, data)

        source_blobs = _parse_source_blobs(d.pop("source_blobs", UNSET))

        def _parse_document_blobs(data: object) -> list[InternalPayloadModelDocumentBlobsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                document_blobs_type_0 = []
                _document_blobs_type_0 = data
                for document_blobs_type_0_item_data in _document_blobs_type_0:
                    document_blobs_type_0_item = InternalPayloadModelDocumentBlobsType0Item.from_dict(
                        document_blobs_type_0_item_data
                    )

                    document_blobs_type_0.append(document_blobs_type_0_item)

                return document_blobs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[InternalPayloadModelDocumentBlobsType0Item] | None | Unset, data)

        document_blobs = _parse_document_blobs(d.pop("document_blobs", UNSET))

        def _parse_source_details(data: object) -> list[InternalPayloadModelSourceDetailsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                source_details_type_0 = []
                _source_details_type_0 = data
                for source_details_type_0_item_data in _source_details_type_0:
                    source_details_type_0_item = InternalPayloadModelSourceDetailsType0Item.from_dict(
                        source_details_type_0_item_data
                    )

                    source_details_type_0.append(source_details_type_0_item)

                return source_details_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[InternalPayloadModelSourceDetailsType0Item] | None | Unset, data)

        source_details = _parse_source_details(d.pop("source_details", UNSET))

        def _parse_modality(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        modality = _parse_modality(d.pop("modality", UNSET))

        def _parse_metadata(data: object) -> InternalPayloadModelMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = InternalPayloadModelMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InternalPayloadModelMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        def _parse_mime_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mime_type = _parse_mime_type(d.pop("mime_type", UNSET))

        def _parse_size_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        size_bytes = _parse_size_bytes(d.pop("size_bytes", UNSET))

        def _parse_content_hash(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content_hash = _parse_content_hash(d.pop("content_hash", UNSET))

        internal_payload_model = cls(
            internal_id=internal_id,
            namespace_id=namespace_id,
            document_id=document_id,
            collection_id=collection_id,
            created_at=created_at,
            updated_at=updated_at,
            lineage=lineage,
            processing=processing,
            source_blobs=source_blobs,
            document_blobs=document_blobs,
            source_details=source_details,
            modality=modality,
            metadata=metadata,
            mime_type=mime_type,
            size_bytes=size_bytes,
            content_hash=content_hash,
        )

        internal_payload_model.additional_properties = d
        return internal_payload_model

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
