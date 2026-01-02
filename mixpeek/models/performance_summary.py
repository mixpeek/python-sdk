from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PerformanceSummary")


@_attrs_define
class PerformanceSummary:
    """Summary statistics for performance.

    Attributes:
        total_executions (int | Unset): Total number of executions Default: 0.
        avg_latency_ms (float | Unset): Average latency Default: 0.0.
        p50_latency_ms (float | Unset): Median latency Default: 0.0.
        p95_latency_ms (float | Unset): 95th percentile latency Default: 0.0.
        p99_latency_ms (float | Unset): 99th percentile latency Default: 0.0.
        max_latency_ms (float | Unset): Maximum latency Default: 0.0.
        total_time_seconds (float | Unset): Total time spent across all executions Default: 0.0.
    """

    total_executions: int | Unset = 0
    avg_latency_ms: float | Unset = 0.0
    p50_latency_ms: float | Unset = 0.0
    p95_latency_ms: float | Unset = 0.0
    p99_latency_ms: float | Unset = 0.0
    max_latency_ms: float | Unset = 0.0
    total_time_seconds: float | Unset = 0.0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_executions = self.total_executions

        avg_latency_ms = self.avg_latency_ms

        p50_latency_ms = self.p50_latency_ms

        p95_latency_ms = self.p95_latency_ms

        p99_latency_ms = self.p99_latency_ms

        max_latency_ms = self.max_latency_ms

        total_time_seconds = self.total_time_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_executions is not UNSET:
            field_dict["total_executions"] = total_executions
        if avg_latency_ms is not UNSET:
            field_dict["avg_latency_ms"] = avg_latency_ms
        if p50_latency_ms is not UNSET:
            field_dict["p50_latency_ms"] = p50_latency_ms
        if p95_latency_ms is not UNSET:
            field_dict["p95_latency_ms"] = p95_latency_ms
        if p99_latency_ms is not UNSET:
            field_dict["p99_latency_ms"] = p99_latency_ms
        if max_latency_ms is not UNSET:
            field_dict["max_latency_ms"] = max_latency_ms
        if total_time_seconds is not UNSET:
            field_dict["total_time_seconds"] = total_time_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_executions = d.pop("total_executions", UNSET)

        avg_latency_ms = d.pop("avg_latency_ms", UNSET)

        p50_latency_ms = d.pop("p50_latency_ms", UNSET)

        p95_latency_ms = d.pop("p95_latency_ms", UNSET)

        p99_latency_ms = d.pop("p99_latency_ms", UNSET)

        max_latency_ms = d.pop("max_latency_ms", UNSET)

        total_time_seconds = d.pop("total_time_seconds", UNSET)

        performance_summary = cls(
            total_executions=total_executions,
            avg_latency_ms=avg_latency_ms,
            p50_latency_ms=p50_latency_ms,
            p95_latency_ms=p95_latency_ms,
            p99_latency_ms=p99_latency_ms,
            max_latency_ms=max_latency_ms,
            total_time_seconds=total_time_seconds,
        )

        performance_summary.additional_properties = d
        return performance_summary

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
