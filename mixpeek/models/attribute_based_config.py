from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AttributeBasedConfig")


@_attrs_define
class AttributeBasedConfig:
    """Configuration for attribute-based clustering.

    Attribute-based clustering groups documents by metadata attributes (e.g., category, brand, status)
    instead of vector similarity. This is useful for organizing content by business logic rather than
    semantic similarity.

    Examples:
        - Group products by category and brand
        - Organize orders by status and priority
        - Cluster content by author and topic

        Attributes:
            attributes (list[str]): List of attribute field names to use for clustering. Documents will be grouped by unique
                combinations of these attribute values. Supports dot-notation for nested fields (e.g., 'metadata.category').
                Order matters for hierarchical grouping: first attribute is top-level, subsequent are nested.
            hierarchical_grouping (bool | Unset): Whether to create hierarchical clusters based on attribute order. When
                True: Creates parent clusters for each unique value of the first attribute, then child clusters for subsequent
                attributes within each parent. When False: Creates flat clusters for each unique combination of all attributes.
                Example with ['category', 'brand']:   hierarchical=True → 'Electronics' (parent) → 'Apple', 'Samsung'
                (children).   hierarchical=False → 'Electronics_Apple', 'Electronics_Samsung' (flat). Default: False.
            aggregation_method (None | str | Unset): Method for aggregating attribute values when creating cluster
                centroids. Options: 'most_frequent' (default), 'first', 'last'. Most use cases should use the default.
    """

    attributes: list[str]
    hierarchical_grouping: bool | Unset = False
    aggregation_method: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attributes = self.attributes

        hierarchical_grouping = self.hierarchical_grouping

        aggregation_method: None | str | Unset
        if isinstance(self.aggregation_method, Unset):
            aggregation_method = UNSET
        else:
            aggregation_method = self.aggregation_method

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attributes": attributes,
            }
        )
        if hierarchical_grouping is not UNSET:
            field_dict["hierarchical_grouping"] = hierarchical_grouping
        if aggregation_method is not UNSET:
            field_dict["aggregation_method"] = aggregation_method

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        attributes = cast(list[str], d.pop("attributes"))

        hierarchical_grouping = d.pop("hierarchical_grouping", UNSET)

        def _parse_aggregation_method(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        aggregation_method = _parse_aggregation_method(d.pop("aggregation_method", UNSET))

        attribute_based_config = cls(
            attributes=attributes,
            hierarchical_grouping=hierarchical_grouping,
            aggregation_method=aggregation_method,
        )

        attribute_based_config.additional_properties = d
        return attribute_based_config

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
