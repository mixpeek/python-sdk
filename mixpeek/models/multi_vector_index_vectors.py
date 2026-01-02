from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.vector_index import VectorIndex


T = TypeVar("T", bound="MultiVectorIndexVectors")


@_attrs_define
class MultiVectorIndexVectors:
    """REQUIRED. Dictionary mapping vector output names to their VectorIndex configurations. Each key is a unique
    identifier for that vector type within this multi-index. Each value is a complete VectorIndex with its own
    dimensions, type, and inference service. Example keys: 'dense', 'sparse', 'primary', 'secondary'.

    """

    additional_properties: dict[str, VectorIndex] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vector_index import VectorIndex

        d = dict(src_dict)
        multi_vector_index_vectors = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = VectorIndex.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        multi_vector_index_vectors.additional_properties = additional_properties
        return multi_vector_index_vectors

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> VectorIndex:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: VectorIndex) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
