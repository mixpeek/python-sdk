from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ExtractorMetrics")


@_attrs_define
class ExtractorMetrics:
    """Extractor performance metrics.

    Attributes:
        extractor_name (str):
        version (str):
        execution_count (int):
        success_count (int):
        failure_count (int):
        success_rate (float):
        avg_latency_ms (float):
        p95_latency_ms (float):
        p99_latency_ms (float):
    """

    extractor_name: str
    version: str
    execution_count: int
    success_count: int
    failure_count: int
    success_rate: float
    avg_latency_ms: float
    p95_latency_ms: float
    p99_latency_ms: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        extractor_name = self.extractor_name

        version = self.version

        execution_count = self.execution_count

        success_count = self.success_count

        failure_count = self.failure_count

        success_rate = self.success_rate

        avg_latency_ms = self.avg_latency_ms

        p95_latency_ms = self.p95_latency_ms

        p99_latency_ms = self.p99_latency_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "extractor_name": extractor_name,
                "version": version,
                "execution_count": execution_count,
                "success_count": success_count,
                "failure_count": failure_count,
                "success_rate": success_rate,
                "avg_latency_ms": avg_latency_ms,
                "p95_latency_ms": p95_latency_ms,
                "p99_latency_ms": p99_latency_ms,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        extractor_name = d.pop("extractor_name")

        version = d.pop("version")

        execution_count = d.pop("execution_count")

        success_count = d.pop("success_count")

        failure_count = d.pop("failure_count")

        success_rate = d.pop("success_rate")

        avg_latency_ms = d.pop("avg_latency_ms")

        p95_latency_ms = d.pop("p95_latency_ms")

        p99_latency_ms = d.pop("p99_latency_ms")

        extractor_metrics = cls(
            extractor_name=extractor_name,
            version=version,
            execution_count=execution_count,
            success_count=success_count,
            failure_count=failure_count,
            success_rate=success_rate,
            avg_latency_ms=avg_latency_ms,
            p95_latency_ms=p95_latency_ms,
            p99_latency_ms=p99_latency_ms,
        )

        extractor_metrics.additional_properties = d
        return extractor_metrics

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
