from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.vector_index_definition_type import VectorIndexDefinitionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.multi_vector_index import MultiVectorIndex
    from ..models.vector_index import VectorIndex


T = TypeVar("T", bound="VectorIndexDefinition")


@_attrs_define
class VectorIndexDefinition:
    """Complete vector index definition that can be either single or multi-vector.

    This is the USER-FACING representation that appears in feature extractor definitions
    and API responses. It wraps a VectorIndex (or MultiVectorIndex) and adds metadata.

    Key Concepts - Two-Name System:
        - VectorIndexDefinition.name: SHORT user-facing name (e.g., "embedding")
          Used in feature URIs: mixpeek://text_extractor@v1/multilingual_e5_large_instruct_v1
                                                            ^^^^^^^^^^

        - VectorIndex.name: FULL storage name (e.g., "text_extractor_v1_embedding")
          Used as Qdrant collection name for namespace isolation

    This two-level naming allows clean URIs while preventing storage collisions.

    Use Cases:
        - Define extractor outputs in feature extractor definitions
        - Expose available vector indexes in collection metadata
        - Enable feature URI resolution (short name → full storage name)

    Requirements:
        - name: REQUIRED - Short output name for feature URIs
        - description: REQUIRED - Explain what this output produces
        - type: REQUIRED - "single" (most common) or "multi" (rare)
        - index: REQUIRED - Nested VectorIndex or MultiVectorIndex
        - feature_uri: OPTIONAL - Populated at collection creation time

        Attributes:
            name (str): REQUIRED. Short user-facing output name used in feature URIs. This is NOT the Qdrant collection name
                - it's the clean identifier for this output. Format: Simple snake_case name (e.g., 'embedding',
                'video_embedding', 'sparse_embedding'). Used in feature URIs: mixpeek://{extractor}@{version}/{THIS_NAME}. Must
                be unique within this extractor's outputs.
            description (str): REQUIRED. Human-readable description of this vector output. Explain what content this output
                embeds and when to use it. Appears in API documentation and helps users choose the right feature URI. Be
                specific about the embedding type and use cases.
            type_ (VectorIndexDefinitionType): REQUIRED. Index type - 'single' or 'multi'. 'single': One vector per document
                (most common). Use for standard embeddings. 'multi': Multiple named vectors per document (rare). Use for
                hybrid/ensemble. Determines whether 'index' field contains VectorIndex or MultiVectorIndex.
            index (MultiVectorIndex | VectorIndex): REQUIRED. Nested index configuration. VectorIndex if type='single' (most
                common case). MultiVectorIndex if type='multi' (rare, for hybrid search). Contains the full storage
                configuration including Qdrant collection name, dimensions, distance metric, and inference service.
            feature_uri (None | str | Unset): Full feature URI for this vector index. Format:
                mixpeek://{extractor}@{version}/{output_name}. Populated at collection creation time. Use this URI in retriever
                feature_filter stages.
    """

    name: str
    description: str
    type_: VectorIndexDefinitionType
    index: MultiVectorIndex | VectorIndex
    feature_uri: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.vector_index import VectorIndex

        name = self.name

        description = self.description

        type_ = self.type_.value

        index: dict[str, Any]
        if isinstance(self.index, VectorIndex):
            index = self.index.to_dict()
        else:
            index = self.index.to_dict()

        feature_uri: None | str | Unset
        if isinstance(self.feature_uri, Unset):
            feature_uri = UNSET
        else:
            feature_uri = self.feature_uri

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "description": description,
                "type": type_,
                "index": index,
            }
        )
        if feature_uri is not UNSET:
            field_dict["feature_uri"] = feature_uri

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.multi_vector_index import MultiVectorIndex
        from ..models.vector_index import VectorIndex

        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description")

        type_ = VectorIndexDefinitionType(d.pop("type"))

        def _parse_index(data: object) -> MultiVectorIndex | VectorIndex:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                index_type_0 = VectorIndex.from_dict(data)

                return index_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            index_type_1 = MultiVectorIndex.from_dict(data)

            return index_type_1

        index = _parse_index(d.pop("index"))

        def _parse_feature_uri(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        feature_uri = _parse_feature_uri(d.pop("feature_uri", UNSET))

        vector_index_definition = cls(
            name=name,
            description=description,
            type_=type_,
            index=index,
            feature_uri=feature_uri,
        )

        vector_index_definition.additional_properties = d
        return vector_index_definition

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
