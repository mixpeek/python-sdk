from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.instantiate_taxonomy_template_request_collection_config import (
        InstantiateTaxonomyTemplateRequestCollectionConfig,
    )


T = TypeVar("T", bound="InstantiateTaxonomyTemplateRequest")


@_attrs_define
class InstantiateTaxonomyTemplateRequest:
    """Request to instantiate a taxonomy from a template.

    Attributes:
        taxonomy_name (str): Name for the new taxonomy
        collection_config (InstantiateTaxonomyTemplateRequestCollectionConfig): Collection configuration for the
            taxonomy. For flat taxonomies: {'collection_id': 'col_xxx'} For hierarchical taxonomies: maps node collection
            IDs to actual collection IDs, e.g., {'col_template_root': 'col_actual_root', 'col_template_child':
            'col_actual_child'}
        description (None | str | Unset): Optional description override for the taxonomy
    """

    taxonomy_name: str
    collection_config: InstantiateTaxonomyTemplateRequestCollectionConfig
    description: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        taxonomy_name = self.taxonomy_name

        collection_config = self.collection_config.to_dict()

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "taxonomy_name": taxonomy_name,
                "collection_config": collection_config,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.instantiate_taxonomy_template_request_collection_config import (
            InstantiateTaxonomyTemplateRequestCollectionConfig,
        )

        d = dict(src_dict)
        taxonomy_name = d.pop("taxonomy_name")

        collection_config = InstantiateTaxonomyTemplateRequestCollectionConfig.from_dict(d.pop("collection_config"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        instantiate_taxonomy_template_request = cls(
            taxonomy_name=taxonomy_name,
            collection_config=collection_config,
            description=description,
        )

        instantiate_taxonomy_template_request.additional_properties = d
        return instantiate_taxonomy_template_request

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
