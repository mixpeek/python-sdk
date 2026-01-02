from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.document_create_request_source_type_type_0 import DocumentCreateRequestSourceTypeType0
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.document_create_request_metadata import DocumentCreateRequestMetadata
    from ..models.feature_model import FeatureModel
    from ..models.lineage_step import LineageStep


T = TypeVar("T", bound="DocumentCreateRequest")


@_attrs_define
class DocumentCreateRequest:
    """Request model for creating a document.

    Attributes:
        collection_id (str): ID of the collection the document belongs to. Example: collection_123.
        root_object_id (None | str | Unset): Optional denormalized root object identifier provided during creation.
        root_bucket_id (None | str | Unset): Optional denormalized bucket identifier provided during creation.
        source_type (DocumentCreateRequestSourceTypeType0 | None | Unset): Optional immediate parent type for the
            document.
        source_collection_id (None | str | Unset): Optional parent collection identifier when sourced from a collection.
        source_document_id (None | str | Unset): Optional parent document identifier when sourced from a collection.
        source_object_id (None | str | Unset): Optional parent object identifier when sourced directly from a bucket.
        lineage_path (None | str | Unset): Optional materialized lineage path to set during creation.
        lineage_chain (list[LineageStep] | Unset): Processing steps from root object to this document. Recommended for
            decomposition trees.
        document_schema_version (None | str | Unset): Optional document schema version (v1 or v2). If not provided, uses
            system default.
        metadata (DocumentCreateRequestMetadata | Unset): Optional metadata dictionary for user-defined fields and
            custom attributes.
        features (list[FeatureModel] | Unset): Features to associate with the document
    """

    collection_id: str
    root_object_id: None | str | Unset = UNSET
    root_bucket_id: None | str | Unset = UNSET
    source_type: DocumentCreateRequestSourceTypeType0 | None | Unset = UNSET
    source_collection_id: None | str | Unset = UNSET
    source_document_id: None | str | Unset = UNSET
    source_object_id: None | str | Unset = UNSET
    lineage_path: None | str | Unset = UNSET
    lineage_chain: list[LineageStep] | Unset = UNSET
    document_schema_version: None | str | Unset = UNSET
    metadata: DocumentCreateRequestMetadata | Unset = UNSET
    features: list[FeatureModel] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        collection_id = self.collection_id

        root_object_id: None | str | Unset
        if isinstance(self.root_object_id, Unset):
            root_object_id = UNSET
        else:
            root_object_id = self.root_object_id

        root_bucket_id: None | str | Unset
        if isinstance(self.root_bucket_id, Unset):
            root_bucket_id = UNSET
        else:
            root_bucket_id = self.root_bucket_id

        source_type: None | str | Unset
        if isinstance(self.source_type, Unset):
            source_type = UNSET
        elif isinstance(self.source_type, DocumentCreateRequestSourceTypeType0):
            source_type = self.source_type.value
        else:
            source_type = self.source_type

        source_collection_id: None | str | Unset
        if isinstance(self.source_collection_id, Unset):
            source_collection_id = UNSET
        else:
            source_collection_id = self.source_collection_id

        source_document_id: None | str | Unset
        if isinstance(self.source_document_id, Unset):
            source_document_id = UNSET
        else:
            source_document_id = self.source_document_id

        source_object_id: None | str | Unset
        if isinstance(self.source_object_id, Unset):
            source_object_id = UNSET
        else:
            source_object_id = self.source_object_id

        lineage_path: None | str | Unset
        if isinstance(self.lineage_path, Unset):
            lineage_path = UNSET
        else:
            lineage_path = self.lineage_path

        lineage_chain: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.lineage_chain, Unset):
            lineage_chain = []
            for lineage_chain_item_data in self.lineage_chain:
                lineage_chain_item = lineage_chain_item_data.to_dict()
                lineage_chain.append(lineage_chain_item)

        document_schema_version: None | str | Unset
        if isinstance(self.document_schema_version, Unset):
            document_schema_version = UNSET
        else:
            document_schema_version = self.document_schema_version

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        features: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.features, Unset):
            features = []
            for features_item_data in self.features:
                features_item = features_item_data.to_dict()
                features.append(features_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "collection_id": collection_id,
            }
        )
        if root_object_id is not UNSET:
            field_dict["root_object_id"] = root_object_id
        if root_bucket_id is not UNSET:
            field_dict["root_bucket_id"] = root_bucket_id
        if source_type is not UNSET:
            field_dict["source_type"] = source_type
        if source_collection_id is not UNSET:
            field_dict["source_collection_id"] = source_collection_id
        if source_document_id is not UNSET:
            field_dict["source_document_id"] = source_document_id
        if source_object_id is not UNSET:
            field_dict["source_object_id"] = source_object_id
        if lineage_path is not UNSET:
            field_dict["lineage_path"] = lineage_path
        if lineage_chain is not UNSET:
            field_dict["lineage_chain"] = lineage_chain
        if document_schema_version is not UNSET:
            field_dict["document_schema_version"] = document_schema_version
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if features is not UNSET:
            field_dict["features"] = features

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.document_create_request_metadata import DocumentCreateRequestMetadata
        from ..models.feature_model import FeatureModel
        from ..models.lineage_step import LineageStep

        d = dict(src_dict)
        collection_id = d.pop("collection_id")

        def _parse_root_object_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        root_object_id = _parse_root_object_id(d.pop("root_object_id", UNSET))

        def _parse_root_bucket_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        root_bucket_id = _parse_root_bucket_id(d.pop("root_bucket_id", UNSET))

        def _parse_source_type(data: object) -> DocumentCreateRequestSourceTypeType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                source_type_type_0 = DocumentCreateRequestSourceTypeType0(data)

                return source_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DocumentCreateRequestSourceTypeType0 | None | Unset, data)

        source_type = _parse_source_type(d.pop("source_type", UNSET))

        def _parse_source_collection_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_collection_id = _parse_source_collection_id(d.pop("source_collection_id", UNSET))

        def _parse_source_document_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_document_id = _parse_source_document_id(d.pop("source_document_id", UNSET))

        def _parse_source_object_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_object_id = _parse_source_object_id(d.pop("source_object_id", UNSET))

        def _parse_lineage_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lineage_path = _parse_lineage_path(d.pop("lineage_path", UNSET))

        _lineage_chain = d.pop("lineage_chain", UNSET)
        lineage_chain: list[LineageStep] | Unset = UNSET
        if _lineage_chain is not UNSET:
            lineage_chain = []
            for lineage_chain_item_data in _lineage_chain:
                lineage_chain_item = LineageStep.from_dict(lineage_chain_item_data)

                lineage_chain.append(lineage_chain_item)

        def _parse_document_schema_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        document_schema_version = _parse_document_schema_version(d.pop("document_schema_version", UNSET))

        _metadata = d.pop("metadata", UNSET)
        metadata: DocumentCreateRequestMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = DocumentCreateRequestMetadata.from_dict(_metadata)

        _features = d.pop("features", UNSET)
        features: list[FeatureModel] | Unset = UNSET
        if _features is not UNSET:
            features = []
            for features_item_data in _features:
                features_item = FeatureModel.from_dict(features_item_data)

                features.append(features_item)

        document_create_request = cls(
            collection_id=collection_id,
            root_object_id=root_object_id,
            root_bucket_id=root_bucket_id,
            source_type=source_type,
            source_collection_id=source_collection_id,
            source_document_id=source_document_id,
            source_object_id=source_object_id,
            lineage_path=lineage_path,
            lineage_chain=lineage_chain,
            document_schema_version=document_schema_version,
            metadata=metadata,
            features=features,
        )

        document_create_request.additional_properties = d
        return document_create_request

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
