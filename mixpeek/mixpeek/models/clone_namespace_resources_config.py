from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CloneNamespaceResourcesConfig")


@_attrs_define
class CloneNamespaceResourcesConfig:
    """Configuration for which resources to include in clone.

    Attributes:
        collections (bool | Unset): Include collections (with all embeddings/vectors) Default: True.
        retrievers (bool | Unset): Include retrievers Default: True.
        taxonomies (bool | Unset): Include taxonomies Default: False.
    """

    collections: bool | Unset = True
    retrievers: bool | Unset = True
    taxonomies: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        collections = self.collections

        retrievers = self.retrievers

        taxonomies = self.taxonomies

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if collections is not UNSET:
            field_dict["collections"] = collections
        if retrievers is not UNSET:
            field_dict["retrievers"] = retrievers
        if taxonomies is not UNSET:
            field_dict["taxonomies"] = taxonomies

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        collections = d.pop("collections", UNSET)

        retrievers = d.pop("retrievers", UNSET)

        taxonomies = d.pop("taxonomies", UNSET)

        clone_namespace_resources_config = cls(
            collections=collections,
            retrievers=retrievers,
            taxonomies=taxonomies,
        )

        clone_namespace_resources_config.additional_properties = d
        return clone_namespace_resources_config

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
