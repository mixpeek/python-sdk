from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FieldPerformanceMetrics")


@_attrs_define
class FieldPerformanceMetrics:
    """Performance correlation metrics for a field.

    Attributes:
        field_name (str): Metadata field name
        usage_count (int): Number of times field was queried
        avg_latency_ms (float): Average latency when field is used
        p50_latency_ms (float): 50th percentile latency
        p95_latency_ms (float): 95th percentile latency
        p99_latency_ms (float): 99th percentile latency
        max_latency_ms (float): Maximum latency observed
        index_priority_score (float): Priority score for indexing (usage_count * avg_latency)
    """

    field_name: str
    usage_count: int
    avg_latency_ms: float
    p50_latency_ms: float
    p95_latency_ms: float
    p99_latency_ms: float
    max_latency_ms: float
    index_priority_score: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_name = self.field_name

        usage_count = self.usage_count

        avg_latency_ms = self.avg_latency_ms

        p50_latency_ms = self.p50_latency_ms

        p95_latency_ms = self.p95_latency_ms

        p99_latency_ms = self.p99_latency_ms

        max_latency_ms = self.max_latency_ms

        index_priority_score = self.index_priority_score

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "field_name": field_name,
                "usage_count": usage_count,
                "avg_latency_ms": avg_latency_ms,
                "p50_latency_ms": p50_latency_ms,
                "p95_latency_ms": p95_latency_ms,
                "p99_latency_ms": p99_latency_ms,
                "max_latency_ms": max_latency_ms,
                "index_priority_score": index_priority_score,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_name = d.pop("field_name")

        usage_count = d.pop("usage_count")

        avg_latency_ms = d.pop("avg_latency_ms")

        p50_latency_ms = d.pop("p50_latency_ms")

        p95_latency_ms = d.pop("p95_latency_ms")

        p99_latency_ms = d.pop("p99_latency_ms")

        max_latency_ms = d.pop("max_latency_ms")

        index_priority_score = d.pop("index_priority_score")

        field_performance_metrics = cls(
            field_name=field_name,
            usage_count=usage_count,
            avg_latency_ms=avg_latency_ms,
            p50_latency_ms=p50_latency_ms,
            p95_latency_ms=p95_latency_ms,
            p99_latency_ms=p99_latency_ms,
            max_latency_ms=max_latency_ms,
            index_priority_score=index_priority_score,
        )

        field_performance_metrics.additional_properties = d
        return field_performance_metrics

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
