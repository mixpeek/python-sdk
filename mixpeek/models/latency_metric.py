from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="LatencyMetric")


@_attrs_define
class LatencyMetric:
    """Latency distribution metric.

    Attributes:
        time_bucket (datetime.datetime):
        document_count (int):
        avg_latency_ms (float):
        p95_latency_ms (float):
        p99_latency_ms (float):
    """

    time_bucket: datetime.datetime
    document_count: int
    avg_latency_ms: float
    p95_latency_ms: float
    p99_latency_ms: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time_bucket = self.time_bucket.isoformat()

        document_count = self.document_count

        avg_latency_ms = self.avg_latency_ms

        p95_latency_ms = self.p95_latency_ms

        p99_latency_ms = self.p99_latency_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "time_bucket": time_bucket,
                "document_count": document_count,
                "avg_latency_ms": avg_latency_ms,
                "p95_latency_ms": p95_latency_ms,
                "p99_latency_ms": p99_latency_ms,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        time_bucket = isoparse(d.pop("time_bucket"))

        document_count = d.pop("document_count")

        avg_latency_ms = d.pop("avg_latency_ms")

        p95_latency_ms = d.pop("p95_latency_ms")

        p99_latency_ms = d.pop("p99_latency_ms")

        latency_metric = cls(
            time_bucket=time_bucket,
            document_count=document_count,
            avg_latency_ms=avg_latency_ms,
            p95_latency_ms=p95_latency_ms,
            p99_latency_ms=p99_latency_ms,
        )

        latency_metric.additional_properties = d
        return latency_metric

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
