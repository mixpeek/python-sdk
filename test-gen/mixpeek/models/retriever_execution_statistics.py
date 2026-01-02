from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.retriever_execution_statistics_stages import RetrieverExecutionStatisticsStages


T = TypeVar("T", bound="RetrieverExecutionStatistics")


@_attrs_define
class RetrieverExecutionStatistics:
    """Aggregated execution statistics for an entire retriever execution run.

    Attributes:
        stages (RetrieverExecutionStatisticsStages | Unset): Per-stage statistics keyed by stage instance name
            (REQUIRED).
        total_time_ms (float | Unset): Total retriever execution time in milliseconds (REQUIRED). Default: 0.0.
        credits_used (float | Unset): Total credits consumed across all stages (OPTIONAL in MVP). Default: 0.0.
    """

    stages: RetrieverExecutionStatisticsStages | Unset = UNSET
    total_time_ms: float | Unset = 0.0
    credits_used: float | Unset = 0.0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stages: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stages, Unset):
            stages = self.stages.to_dict()

        total_time_ms = self.total_time_ms

        credits_used = self.credits_used

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stages is not UNSET:
            field_dict["stages"] = stages
        if total_time_ms is not UNSET:
            field_dict["total_time_ms"] = total_time_ms
        if credits_used is not UNSET:
            field_dict["credits_used"] = credits_used

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.retriever_execution_statistics_stages import RetrieverExecutionStatisticsStages

        d = dict(src_dict)
        _stages = d.pop("stages", UNSET)
        stages: RetrieverExecutionStatisticsStages | Unset
        if isinstance(_stages, Unset):
            stages = UNSET
        else:
            stages = RetrieverExecutionStatisticsStages.from_dict(_stages)

        total_time_ms = d.pop("total_time_ms", UNSET)

        credits_used = d.pop("credits_used", UNSET)

        retriever_execution_statistics = cls(
            stages=stages,
            total_time_ms=total_time_ms,
            credits_used=credits_used,
        )

        retriever_execution_statistics.additional_properties = d
        return retriever_execution_statistics

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
