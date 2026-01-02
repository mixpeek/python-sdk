from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.enrichment_field_mapping import EnrichmentFieldMapping


T = TypeVar("T", bound="SourceEnrichmentConfig")


@_attrs_define
class SourceEnrichmentConfig:
    """Configuration for enriching source collection documents with cluster assignments.

    When enrich_source_collection=True, cluster assignments are written back to
    the original source documents, similar to taxonomy enrichment.

    Uses flexible field mapping pattern to support any cluster result fields.

        Attributes:
            field_mappings (list[EnrichmentFieldMapping] | Unset): List of field mappings from cluster results to document
                fields. Default includes cluster_id and cluster_label. Can include: distance_to_centroid, member_count,
                keywords, visualization coords (x, y, z), etc.
    """

    field_mappings: list[EnrichmentFieldMapping] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_mappings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.field_mappings, Unset):
            field_mappings = []
            for field_mappings_item_data in self.field_mappings:
                field_mappings_item = field_mappings_item_data.to_dict()
                field_mappings.append(field_mappings_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_mappings is not UNSET:
            field_dict["field_mappings"] = field_mappings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.enrichment_field_mapping import EnrichmentFieldMapping

        d = dict(src_dict)
        _field_mappings = d.pop("field_mappings", UNSET)
        field_mappings: list[EnrichmentFieldMapping] | Unset = UNSET
        if _field_mappings is not UNSET:
            field_mappings = []
            for field_mappings_item_data in _field_mappings:
                field_mappings_item = EnrichmentFieldMapping.from_dict(field_mappings_item_data)

                field_mappings.append(field_mappings_item)

        source_enrichment_config = cls(
            field_mappings=field_mappings,
        )

        source_enrichment_config.additional_properties = d
        return source_enrichment_config

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
