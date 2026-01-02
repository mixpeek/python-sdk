from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TaxonomyListStats")


@_attrs_define
class TaxonomyListStats:
    """Aggregate statistics for a list of taxonomies.

    Attributes:
        total_taxonomies (int | Unset): Total number of taxonomies in the result Default: 0.
        flat_taxonomies (int | Unset): Number of flat taxonomies Default: 0.
        hierarchical_taxonomies (int | Unset): Number of hierarchical taxonomies Default: 0.
        taxonomies_with_retrievers (int | Unset): Number of taxonomies with retriever configured Default: 0.
    """

    total_taxonomies: int | Unset = 0
    flat_taxonomies: int | Unset = 0
    hierarchical_taxonomies: int | Unset = 0
    taxonomies_with_retrievers: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_taxonomies = self.total_taxonomies

        flat_taxonomies = self.flat_taxonomies

        hierarchical_taxonomies = self.hierarchical_taxonomies

        taxonomies_with_retrievers = self.taxonomies_with_retrievers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_taxonomies is not UNSET:
            field_dict["total_taxonomies"] = total_taxonomies
        if flat_taxonomies is not UNSET:
            field_dict["flat_taxonomies"] = flat_taxonomies
        if hierarchical_taxonomies is not UNSET:
            field_dict["hierarchical_taxonomies"] = hierarchical_taxonomies
        if taxonomies_with_retrievers is not UNSET:
            field_dict["taxonomies_with_retrievers"] = taxonomies_with_retrievers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_taxonomies = d.pop("total_taxonomies", UNSET)

        flat_taxonomies = d.pop("flat_taxonomies", UNSET)

        hierarchical_taxonomies = d.pop("hierarchical_taxonomies", UNSET)

        taxonomies_with_retrievers = d.pop("taxonomies_with_retrievers", UNSET)

        taxonomy_list_stats = cls(
            total_taxonomies=total_taxonomies,
            flat_taxonomies=flat_taxonomies,
            hierarchical_taxonomies=hierarchical_taxonomies,
            taxonomies_with_retrievers=taxonomies_with_retrievers,
        )

        taxonomy_list_stats.additional_properties = d
        return taxonomy_list_stats

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
