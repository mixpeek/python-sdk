from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vector_index import VectorIndex


T = TypeVar("T", bound="CollectionFeatureDescriptor")


@_attrs_define
class CollectionFeatureDescriptor:
    """Descriptor for a collection's available feature using existing models/keys.

    Attributes:
        feature_address (str): Fully qualified feature address
        feature_extractor_name (str): Extractor name
        version (str): Extractor version
        vector_index (VectorIndex): Configuration for a single vector index in Qdrant.

            Defines the fully-qualified vector index including storage name, dimensions,
            distance metric, and inference service. This is the actual index that gets
            created in Qdrant and used for vector similarity search.

            Key Concepts:
                - The `name` field is the FULL qualified name used as the Qdrant collection name
                - Format: {extractor}_{version}_{output} (e.g., "text_extractor_v1_embedding")
                - This ensures namespace isolation between extractors and versions
                - Different from VectorIndexDefinition.name which is the short user-facing name

            Use Cases:
                - Define vector storage configuration for feature extractors
                - Specify inference service and model parameters
                - Configure distance metrics for similarity search
                - Set storage optimization (on-disk for large vectors)

            Requirements:
                - name: REQUIRED - Must be unique across all extractors in namespace
                - description: REQUIRED - Explain what this vector represents
                - dimensions: REQUIRED for DENSE vectors, OPTIONAL for SPARSE
                - type: REQUIRED - Must match VectorType enum
                - inference_name: REQUIRED - Must reference a valid inference service
        primary (bool | Unset): True if this is the primary output (short address allowed) Default: False.
    """

    feature_address: str
    feature_extractor_name: str
    version: str
    vector_index: VectorIndex
    primary: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        feature_address = self.feature_address

        feature_extractor_name = self.feature_extractor_name

        version = self.version

        vector_index = self.vector_index.to_dict()

        primary = self.primary

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "feature_address": feature_address,
                "feature_extractor_name": feature_extractor_name,
                "version": version,
                "vector_index": vector_index,
            }
        )
        if primary is not UNSET:
            field_dict["primary"] = primary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vector_index import VectorIndex

        d = dict(src_dict)
        feature_address = d.pop("feature_address")

        feature_extractor_name = d.pop("feature_extractor_name")

        version = d.pop("version")

        vector_index = VectorIndex.from_dict(d.pop("vector_index"))

        primary = d.pop("primary", UNSET)

        collection_feature_descriptor = cls(
            feature_address=feature_address,
            feature_extractor_name=feature_extractor_name,
            version=version,
            vector_index=vector_index,
            primary=primary,
        )

        collection_feature_descriptor.additional_properties = d
        return collection_feature_descriptor

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
