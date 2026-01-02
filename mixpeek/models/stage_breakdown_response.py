from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.stage_performance_metrics import StagePerformanceMetrics


T = TypeVar("T", bound="StageBreakdownResponse")


@_attrs_define
class StageBreakdownResponse:
    """Stage breakdown response.

    Attributes:
        retriever_id (str): Retriever identifier
        stages (list[StagePerformanceMetrics]): Stage metrics
        total_latency_ms (float): Total pipeline latency
    """

    retriever_id: str
    stages: list[StagePerformanceMetrics]
    total_latency_ms: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        retriever_id = self.retriever_id

        stages = []
        for stages_item_data in self.stages:
            stages_item = stages_item_data.to_dict()
            stages.append(stages_item)

        total_latency_ms = self.total_latency_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "retriever_id": retriever_id,
                "stages": stages,
                "total_latency_ms": total_latency_ms,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.stage_performance_metrics import StagePerformanceMetrics

        d = dict(src_dict)
        retriever_id = d.pop("retriever_id")

        stages = []
        _stages = d.pop("stages")
        for stages_item_data in _stages:
            stages_item = StagePerformanceMetrics.from_dict(stages_item_data)

            stages.append(stages_item)

        total_latency_ms = d.pop("total_latency_ms")

        stage_breakdown_response = cls(
            retriever_id=retriever_id,
            stages=stages,
            total_latency_ms=total_latency_ms,
        )

        stage_breakdown_response.additional_properties = d
        return stage_breakdown_response

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
