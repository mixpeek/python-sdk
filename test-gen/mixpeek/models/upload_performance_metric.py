from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="UploadPerformanceMetric")


@_attrs_define
class UploadPerformanceMetric:
    """Upload performance metrics for a time bucket.

    Attributes:
        time_bucket (datetime.datetime): Time bucket timestamp
        upload_count (int): Number of uploads
        avg_latency_ms (float): Average upload latency
        p95_latency_ms (float): 95th percentile latency
        p99_latency_ms (float): 99th percentile latency
        avg_throughput_mbps (float): Average throughput in MB/s
        error_rate (float): Error rate (0-1)
    """

    time_bucket: datetime.datetime
    upload_count: int
    avg_latency_ms: float
    p95_latency_ms: float
    p99_latency_ms: float
    avg_throughput_mbps: float
    error_rate: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time_bucket = self.time_bucket.isoformat()

        upload_count = self.upload_count

        avg_latency_ms = self.avg_latency_ms

        p95_latency_ms = self.p95_latency_ms

        p99_latency_ms = self.p99_latency_ms

        avg_throughput_mbps = self.avg_throughput_mbps

        error_rate = self.error_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "time_bucket": time_bucket,
                "upload_count": upload_count,
                "avg_latency_ms": avg_latency_ms,
                "p95_latency_ms": p95_latency_ms,
                "p99_latency_ms": p99_latency_ms,
                "avg_throughput_mbps": avg_throughput_mbps,
                "error_rate": error_rate,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        time_bucket = isoparse(d.pop("time_bucket"))

        upload_count = d.pop("upload_count")

        avg_latency_ms = d.pop("avg_latency_ms")

        p95_latency_ms = d.pop("p95_latency_ms")

        p99_latency_ms = d.pop("p99_latency_ms")

        avg_throughput_mbps = d.pop("avg_throughput_mbps")

        error_rate = d.pop("error_rate")

        upload_performance_metric = cls(
            time_bucket=time_bucket,
            upload_count=upload_count,
            avg_latency_ms=avg_latency_ms,
            p95_latency_ms=p95_latency_ms,
            p99_latency_ms=p99_latency_ms,
            avg_throughput_mbps=avg_throughput_mbps,
            error_rate=error_rate,
        )

        upload_performance_metric.additional_properties = d
        return upload_performance_metric

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
