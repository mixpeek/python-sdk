from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.internal_lineage_model_source_type_type_0 import InternalLineageModelSourceTypeType0
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.internal_lineage_model_chain_type_0_item import InternalLineageModelChainType0Item


T = TypeVar("T", bound="InternalLineageModel")


@_attrs_define
class InternalLineageModel:
    """Lineage tracking information for document provenance.

    Tracks the complete processing history from the original bucket object
    through all transformation stages in the decomposition tree.

        Attributes:
            root_object_id (None | str | Unset): Original object ID from bucket (root of decomposition tree). All documents
                derived from the same object share this ID.
            root_bucket_id (None | str | Unset): Bucket ID containing the root object.
            source_type (InternalLineageModelSourceTypeType0 | None | Unset): Type of immediate parent source. 'bucket':
                Document created directly from bucket object (tier 1). 'collection': Document created from another collection
                (tier 2+).
            source_object_id (None | str | Unset): Object ID of immediate parent when source_type='bucket'.
            source_document_id (None | str | Unset): Document ID of immediate parent when source_type='collection'.
            source_collection_id (None | str | Unset): Collection ID of immediate parent when source_type='collection'.
            path (None | str | Unset): Materialized lineage path string (e.g., 'bkt_123/col_456/col_789').
            chain (list[InternalLineageModelChainType0Item] | None | Unset): Ordered list of processing steps from root
                object to this document. Each step contains: collection_id, feature_extractor_id, document_id, timestamp.
    """

    root_object_id: None | str | Unset = UNSET
    root_bucket_id: None | str | Unset = UNSET
    source_type: InternalLineageModelSourceTypeType0 | None | Unset = UNSET
    source_object_id: None | str | Unset = UNSET
    source_document_id: None | str | Unset = UNSET
    source_collection_id: None | str | Unset = UNSET
    path: None | str | Unset = UNSET
    chain: list[InternalLineageModelChainType0Item] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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
        elif isinstance(self.source_type, InternalLineageModelSourceTypeType0):
            source_type = self.source_type.value
        else:
            source_type = self.source_type

        source_object_id: None | str | Unset
        if isinstance(self.source_object_id, Unset):
            source_object_id = UNSET
        else:
            source_object_id = self.source_object_id

        source_document_id: None | str | Unset
        if isinstance(self.source_document_id, Unset):
            source_document_id = UNSET
        else:
            source_document_id = self.source_document_id

        source_collection_id: None | str | Unset
        if isinstance(self.source_collection_id, Unset):
            source_collection_id = UNSET
        else:
            source_collection_id = self.source_collection_id

        path: None | str | Unset
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        chain: list[dict[str, Any]] | None | Unset
        if isinstance(self.chain, Unset):
            chain = UNSET
        elif isinstance(self.chain, list):
            chain = []
            for chain_type_0_item_data in self.chain:
                chain_type_0_item = chain_type_0_item_data.to_dict()
                chain.append(chain_type_0_item)

        else:
            chain = self.chain

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if root_object_id is not UNSET:
            field_dict["root_object_id"] = root_object_id
        if root_bucket_id is not UNSET:
            field_dict["root_bucket_id"] = root_bucket_id
        if source_type is not UNSET:
            field_dict["source_type"] = source_type
        if source_object_id is not UNSET:
            field_dict["source_object_id"] = source_object_id
        if source_document_id is not UNSET:
            field_dict["source_document_id"] = source_document_id
        if source_collection_id is not UNSET:
            field_dict["source_collection_id"] = source_collection_id
        if path is not UNSET:
            field_dict["path"] = path
        if chain is not UNSET:
            field_dict["chain"] = chain

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.internal_lineage_model_chain_type_0_item import InternalLineageModelChainType0Item

        d = dict(src_dict)

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

        def _parse_source_type(data: object) -> InternalLineageModelSourceTypeType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                source_type_type_0 = InternalLineageModelSourceTypeType0(data)

                return source_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InternalLineageModelSourceTypeType0 | None | Unset, data)

        source_type = _parse_source_type(d.pop("source_type", UNSET))

        def _parse_source_object_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_object_id = _parse_source_object_id(d.pop("source_object_id", UNSET))

        def _parse_source_document_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_document_id = _parse_source_document_id(d.pop("source_document_id", UNSET))

        def _parse_source_collection_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_collection_id = _parse_source_collection_id(d.pop("source_collection_id", UNSET))

        def _parse_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        path = _parse_path(d.pop("path", UNSET))

        def _parse_chain(data: object) -> list[InternalLineageModelChainType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                chain_type_0 = []
                _chain_type_0 = data
                for chain_type_0_item_data in _chain_type_0:
                    chain_type_0_item = InternalLineageModelChainType0Item.from_dict(chain_type_0_item_data)

                    chain_type_0.append(chain_type_0_item)

                return chain_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[InternalLineageModelChainType0Item] | None | Unset, data)

        chain = _parse_chain(d.pop("chain", UNSET))

        internal_lineage_model = cls(
            root_object_id=root_object_id,
            root_bucket_id=root_bucket_id,
            source_type=source_type,
            source_object_id=source_object_id,
            source_document_id=source_document_id,
            source_collection_id=source_collection_id,
            path=path,
            chain=chain,
        )

        internal_lineage_model.additional_properties = d
        return internal_lineage_model

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
