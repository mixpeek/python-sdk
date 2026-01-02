from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="StagePerformanceMetrics")


@_attrs_define
class StagePerformanceMetrics:
    """Stage-level performance metrics.

    Attributes:
        stage_name (str): Name of the stage
        stage_type (str): Type of the stage
        execution_count (int): Number of executions
        avg_latency_ms (float): Average latency
        p95_latency_ms (float): P95 latency
        avg_documents_in (float): Average documents input
        avg_documents_out (float): Average documents output
    """

    stage_name: str
    stage_type: str
    execution_count: int
    avg_latency_ms: float
    p95_latency_ms: float
    avg_documents_in: float
    avg_documents_out: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stage_name = self.stage_name

        stage_type = self.stage_type

        execution_count = self.execution_count

        avg_latency_ms = self.avg_latency_ms

        p95_latency_ms = self.p95_latency_ms

        avg_documents_in = self.avg_documents_in

        avg_documents_out = self.avg_documents_out

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stage_name": stage_name,
                "stage_type": stage_type,
                "execution_count": execution_count,
                "avg_latency_ms": avg_latency_ms,
                "p95_latency_ms": p95_latency_ms,
                "avg_documents_in": avg_documents_in,
                "avg_documents_out": avg_documents_out,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        stage_name = d.pop("stage_name")

        stage_type = d.pop("stage_type")

        execution_count = d.pop("execution_count")

        avg_latency_ms = d.pop("avg_latency_ms")

        p95_latency_ms = d.pop("p95_latency_ms")

        avg_documents_in = d.pop("avg_documents_in")

        avg_documents_out = d.pop("avg_documents_out")

        stage_performance_metrics = cls(
            stage_name=stage_name,
            stage_type=stage_type,
            execution_count=execution_count,
            avg_latency_ms=avg_latency_ms,
            p95_latency_ms=p95_latency_ms,
            avg_documents_in=avg_documents_in,
            avg_documents_out=avg_documents_out,
        )

        stage_performance_metrics.additional_properties = d
        return stage_performance_metrics

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
