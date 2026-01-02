from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EnrichmentFieldMapping")


@_attrs_define
class EnrichmentFieldMapping:
    """Maps a cluster result field to a document enrichment field.

    Similar to InputMapping pattern used throughout Mixpeek.

        Attributes:
            source_field (str): Field from cluster results to include. Available fields: cluster_id, cluster_label,
                distance_to_centroid, member_count, keywords, x, y, z (visualization coords), metadata.*
            target_field (str): Target field name in enriched document. Example: 'category_id' for cluster_id,
                'product_category' for cluster_label
    """

    source_field: str
    target_field: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_field = self.source_field

        target_field = self.target_field

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source_field": source_field,
                "target_field": target_field,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source_field = d.pop("source_field")

        target_field = d.pop("target_field")

        enrichment_field_mapping = cls(
            source_field=source_field,
            target_field=target_field,
        )

        enrichment_field_mapping.additional_properties = d
        return enrichment_field_mapping

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
