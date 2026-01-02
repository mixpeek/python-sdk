from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FieldQueryMetrics")


@_attrs_define
class FieldQueryMetrics:
    """Metrics for a metadata field's query usage.

    Attributes:
        field_name (str): Metadata field name
        query_count (int): Number of queries using this field
        avg_latency_ms (float): Average query latency in milliseconds
        p95_latency_ms (float): 95th percentile latency in milliseconds
    """

    field_name: str
    query_count: int
    avg_latency_ms: float
    p95_latency_ms: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_name = self.field_name

        query_count = self.query_count

        avg_latency_ms = self.avg_latency_ms

        p95_latency_ms = self.p95_latency_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "field_name": field_name,
                "query_count": query_count,
                "avg_latency_ms": avg_latency_ms,
                "p95_latency_ms": p95_latency_ms,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_name = d.pop("field_name")

        query_count = d.pop("query_count")

        avg_latency_ms = d.pop("avg_latency_ms")

        p95_latency_ms = d.pop("p95_latency_ms")

        field_query_metrics = cls(
            field_name=field_name,
            query_count=query_count,
            avg_latency_ms=avg_latency_ms,
            p95_latency_ms=p95_latency_ms,
        )

        field_query_metrics.additional_properties = d
        return field_query_metrics

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
