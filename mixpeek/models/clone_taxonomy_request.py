from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.flat_taxonomy_config import FlatTaxonomyConfig
    from ..models.hierarchical_taxonomy_config import HierarchicalTaxonomyConfig


T = TypeVar("T", bound="CloneTaxonomyRequest")


@_attrs_define
class CloneTaxonomyRequest:
    """Request to clone a taxonomy with optional modifications.

    **Purpose:**
    Cloning creates a NEW taxonomy (with new ID) based on an existing one,
    allowing you to make changes that aren't allowed via PATCH (config,
    retriever_id, collections). This is the recommended way to iterate on
    taxonomy designs.

    **Clone vs Template vs Version:**
    - **Clone**: Copy THIS taxonomy and modify it (for iteration/fixes)
    - **Template**: Create taxonomy from a reusable pattern (for new projects)
    - **Version**: (Not implemented) - Use clone instead

    **Use Cases:**
    - Fix configuration errors without losing join history
    - Change retriever or input mappings
    - Change target collections
    - Test modifications before replacing production taxonomy
    - Create variants for different datasets

    **All fields are OPTIONAL:**
    - Omit a field to keep the original value
    - Provide a field to override the original value
    - taxonomy_name is REQUIRED (clones must have unique names)

        Attributes:
            taxonomy_name (str): REQUIRED. Name for the cloned taxonomy. Must be unique and different from the source
                taxonomy.
            description (None | str | Unset): OPTIONAL. Description override. If omitted, copies from source taxonomy.
            config (FlatTaxonomyConfig | HierarchicalTaxonomyConfig | None | Unset): OPTIONAL. Override taxonomy
                configuration. If omitted, copies from source taxonomy. This allows you to change retriever_id, input_mappings,
                enrichment_fields, or collection hierarchy.
    """

    taxonomy_name: str
    description: None | str | Unset = UNSET
    config: FlatTaxonomyConfig | HierarchicalTaxonomyConfig | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.flat_taxonomy_config import FlatTaxonomyConfig
        from ..models.hierarchical_taxonomy_config import HierarchicalTaxonomyConfig

        taxonomy_name = self.taxonomy_name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        config: dict[str, Any] | None | Unset
        if isinstance(self.config, Unset):
            config = UNSET
        elif isinstance(self.config, FlatTaxonomyConfig):
            config = self.config.to_dict()
        elif isinstance(self.config, HierarchicalTaxonomyConfig):
            config = self.config.to_dict()
        else:
            config = self.config

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "taxonomy_name": taxonomy_name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if config is not UNSET:
            field_dict["config"] = config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.flat_taxonomy_config import FlatTaxonomyConfig
        from ..models.hierarchical_taxonomy_config import HierarchicalTaxonomyConfig

        d = dict(src_dict)
        taxonomy_name = d.pop("taxonomy_name")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_config(data: object) -> FlatTaxonomyConfig | HierarchicalTaxonomyConfig | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_0_type_0 = FlatTaxonomyConfig.from_dict(data)

                return config_type_0_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_0_type_1 = HierarchicalTaxonomyConfig.from_dict(data)

                return config_type_0_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FlatTaxonomyConfig | HierarchicalTaxonomyConfig | None | Unset, data)

        config = _parse_config(d.pop("config", UNSET))

        clone_taxonomy_request = cls(
            taxonomy_name=taxonomy_name,
            description=description,
            config=config,
        )

        clone_taxonomy_request.additional_properties = d
        return clone_taxonomy_request

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
