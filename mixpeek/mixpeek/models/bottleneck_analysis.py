from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BottleneckAnalysis")


@_attrs_define
class BottleneckAnalysis:
    """Bottleneck analysis result.

    Attributes:
        stage_name (str): Stage name
        component (str): Component
        execution_count (int): Number of executions
        total_time_ms (float): Total time spent
        avg_time_ms (float): Average time per execution
        pct_of_total (float): Percentage of total execution time
        rank (int): Bottleneck ranking (1 = worst)
    """

    stage_name: str
    component: str
    execution_count: int
    total_time_ms: float
    avg_time_ms: float
    pct_of_total: float
    rank: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stage_name = self.stage_name

        component = self.component

        execution_count = self.execution_count

        total_time_ms = self.total_time_ms

        avg_time_ms = self.avg_time_ms

        pct_of_total = self.pct_of_total

        rank = self.rank

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stage_name": stage_name,
                "component": component,
                "execution_count": execution_count,
                "total_time_ms": total_time_ms,
                "avg_time_ms": avg_time_ms,
                "pct_of_total": pct_of_total,
                "rank": rank,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        stage_name = d.pop("stage_name")

        component = d.pop("component")

        execution_count = d.pop("execution_count")

        total_time_ms = d.pop("total_time_ms")

        avg_time_ms = d.pop("avg_time_ms")

        pct_of_total = d.pop("pct_of_total")

        rank = d.pop("rank")

        bottleneck_analysis = cls(
            stage_name=stage_name,
            component=component,
            execution_count=execution_count,
            total_time_ms=total_time_ms,
            avg_time_ms=avg_time_ms,
            pct_of_total=pct_of_total,
            rank=rank,
        )

        bottleneck_analysis.additional_properties = d
        return bottleneck_analysis

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
