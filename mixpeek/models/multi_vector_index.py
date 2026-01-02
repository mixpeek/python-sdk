from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.multi_vector_index_vectors import MultiVectorIndexVectors


T = TypeVar("T", bound="MultiVectorIndex")


@_attrs_define
class MultiVectorIndex:
    """Configuration for multi-vector indexes.

    Allows a single extractor to produce multiple named vector outputs in one index.
    Useful for hybrid search combining different embedding types or multiple models.

    Use Cases:
        - Hybrid dense + sparse embeddings in one index
        - Multiple models for ensemble retrieval
        - Different granularities (sentence + paragraph embeddings)

    Requirements:
        - name: REQUIRED - Full qualified name for the multi-vector index
        - description: REQUIRED - Explain what vector combinations are included
        - vectors: REQUIRED - Dictionary mapping output names to VectorIndex configs

    Note: Currently less common than single VectorIndex. Most extractors use
    separate VectorIndexDefinitions for each output instead.

        Attributes:
            name (str): REQUIRED. Fully-qualified name for the multi-vector index. Format: {extractor}_{version}_{output}
                (e.g., 'hybrid_extractor_v1_multi'). Must be unique across namespace.
            description (str): REQUIRED. Human-readable description of the multi-vector index. Explain what vector types are
                included and their purposes. Describe use cases for this multi-vector configuration.
            vectors (MultiVectorIndexVectors): REQUIRED. Dictionary mapping vector output names to their VectorIndex
                configurations. Each key is a unique identifier for that vector type within this multi-index. Each value is a
                complete VectorIndex with its own dimensions, type, and inference service. Example keys: 'dense', 'sparse',
                'primary', 'secondary'.
    """

    name: str
    description: str
    vectors: MultiVectorIndexVectors
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        vectors = self.vectors.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "description": description,
                "vectors": vectors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.multi_vector_index_vectors import MultiVectorIndexVectors

        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description")

        vectors = MultiVectorIndexVectors.from_dict(d.pop("vectors"))

        multi_vector_index = cls(
            name=name,
            description=description,
            vectors=vectors,
        )

        multi_vector_index.additional_properties = d
        return multi_vector_index

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
