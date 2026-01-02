from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.flat_taxonomy_config import FlatTaxonomyConfig
    from ..models.hierarchical_taxonomy_config import HierarchicalTaxonomyConfig


T = TypeVar("T", bound="CreateTaxonomyRequest")


@_attrs_define
class CreateTaxonomyRequest:
    """Request model to create a taxonomy.

    Attributes:
        taxonomy_name (str): A unique name for the taxonomy within the namespace.
        config (FlatTaxonomyConfig | HierarchicalTaxonomyConfig): Configuration specific to the taxonomy type.
        description (None | str | Unset): An optional description of the taxonomy.
    """

    taxonomy_name: str
    config: FlatTaxonomyConfig | HierarchicalTaxonomyConfig
    description: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.flat_taxonomy_config import FlatTaxonomyConfig

        taxonomy_name = self.taxonomy_name

        config: dict[str, Any]
        if isinstance(self.config, FlatTaxonomyConfig):
            config = self.config.to_dict()
        else:
            config = self.config.to_dict()

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
                "config": config,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.flat_taxonomy_config import FlatTaxonomyConfig
        from ..models.hierarchical_taxonomy_config import HierarchicalTaxonomyConfig

        d = dict(src_dict)
        taxonomy_name = d.pop("taxonomy_name")

        def _parse_config(data: object) -> FlatTaxonomyConfig | HierarchicalTaxonomyConfig:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_0 = FlatTaxonomyConfig.from_dict(data)

                return config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            config_type_1 = HierarchicalTaxonomyConfig.from_dict(data)

            return config_type_1

        config = _parse_config(d.pop("config"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        create_taxonomy_request = cls(
            taxonomy_name=taxonomy_name,
            config=config,
            description=description,
        )

        create_taxonomy_request.additional_properties = d
        return create_taxonomy_request

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
