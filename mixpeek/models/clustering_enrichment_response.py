from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ClusteringEnrichmentResponse")


@_attrs_define
class ClusteringEnrichmentResponse:
    """Response after applying clustering enrichment.

    Attributes:
        processed (int): Number of processed points
        enriched (int): Number of enriched points
        failed (int): Number of failed points
        batches (int): Batches processed
    """

    processed: int
    enriched: int
    failed: int
    batches: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        processed = self.processed

        enriched = self.enriched

        failed = self.failed

        batches = self.batches

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "processed": processed,
                "enriched": enriched,
                "failed": failed,
                "batches": batches,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        processed = d.pop("processed")

        enriched = d.pop("enriched")

        failed = d.pop("failed")

        batches = d.pop("batches")

        clustering_enrichment_response = cls(
            processed=processed,
            enriched=enriched,
            failed=failed,
            batches=batches,
        )

        clustering_enrichment_response.additional_properties = d
        return clustering_enrichment_response

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
