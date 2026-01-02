from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="EnrichmentMetric")


@_attrs_define
class EnrichmentMetric:
    """Taxonomy enrichment metrics.

    Attributes:
        time_bucket (datetime.datetime):
        enrichment_count (int):
        success_count (int):
        failure_count (int):
        avg_latency_ms (float):
        success_rate (float):
    """

    time_bucket: datetime.datetime
    enrichment_count: int
    success_count: int
    failure_count: int
    avg_latency_ms: float
    success_rate: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time_bucket = self.time_bucket.isoformat()

        enrichment_count = self.enrichment_count

        success_count = self.success_count

        failure_count = self.failure_count

        avg_latency_ms = self.avg_latency_ms

        success_rate = self.success_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "time_bucket": time_bucket,
                "enrichment_count": enrichment_count,
                "success_count": success_count,
                "failure_count": failure_count,
                "avg_latency_ms": avg_latency_ms,
                "success_rate": success_rate,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        time_bucket = isoparse(d.pop("time_bucket"))

        enrichment_count = d.pop("enrichment_count")

        success_count = d.pop("success_count")

        failure_count = d.pop("failure_count")

        avg_latency_ms = d.pop("avg_latency_ms")

        success_rate = d.pop("success_rate")

        enrichment_metric = cls(
            time_bucket=time_bucket,
            enrichment_count=enrichment_count,
            success_count=success_count,
            failure_count=failure_count,
            avg_latency_ms=avg_latency_ms,
            success_rate=success_rate,
        )

        enrichment_metric.additional_properties = d
        return enrichment_metric

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
