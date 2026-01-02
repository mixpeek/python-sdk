from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ExtractorPerformance")


@_attrs_define
class ExtractorPerformance:
    """Performance breakdown by extractor.

    Attributes:
        extractor_name (str): Name of the extractor
        stage_name (str): Name of the stage
        execution_count (int): Number of executions
        avg_latency_ms (float): Average latency
        p95_latency_ms (float): 95th percentile latency
        max_latency_ms (float): Maximum latency
    """

    extractor_name: str
    stage_name: str
    execution_count: int
    avg_latency_ms: float
    p95_latency_ms: float
    max_latency_ms: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        extractor_name = self.extractor_name

        stage_name = self.stage_name

        execution_count = self.execution_count

        avg_latency_ms = self.avg_latency_ms

        p95_latency_ms = self.p95_latency_ms

        max_latency_ms = self.max_latency_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "extractor_name": extractor_name,
                "stage_name": stage_name,
                "execution_count": execution_count,
                "avg_latency_ms": avg_latency_ms,
                "p95_latency_ms": p95_latency_ms,
                "max_latency_ms": max_latency_ms,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        extractor_name = d.pop("extractor_name")

        stage_name = d.pop("stage_name")

        execution_count = d.pop("execution_count")

        avg_latency_ms = d.pop("avg_latency_ms")

        p95_latency_ms = d.pop("p95_latency_ms")

        max_latency_ms = d.pop("max_latency_ms")

        extractor_performance = cls(
            extractor_name=extractor_name,
            stage_name=stage_name,
            execution_count=execution_count,
            avg_latency_ms=avg_latency_ms,
            p95_latency_ms=p95_latency_ms,
            max_latency_ms=max_latency_ms,
        )

        extractor_performance.additional_properties = d
        return extractor_performance

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
