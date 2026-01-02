from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="InstantiateTaxonomyTemplateRequestCollectionConfig")


@_attrs_define
class InstantiateTaxonomyTemplateRequestCollectionConfig:
    """Collection configuration for the taxonomy. For flat taxonomies: {'collection_id': 'col_xxx'} For hierarchical
    taxonomies: maps node collection IDs to actual collection IDs, e.g., {'col_template_root': 'col_actual_root',
    'col_template_child': 'col_actual_child'}

    """

    additional_properties: dict[str, str] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        instantiate_taxonomy_template_request_collection_config = cls()

        instantiate_taxonomy_template_request_collection_config.additional_properties = d
        return instantiate_taxonomy_template_request_collection_config

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> str:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: str) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
