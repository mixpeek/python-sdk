from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.aggregation_result_group import AggregationResultGroup
    from ..models.aggregation_result_metrics import AggregationResultMetrics


T = TypeVar("T", bound="AggregationResult")


@_attrs_define
class AggregationResult:
    """Single aggregation result row.

    Contains grouped field values and computed aggregations.

        Attributes:
            group (AggregationResultGroup): Grouped field values that define this result row.
            metrics (AggregationResultMetrics): Computed aggregation values for this group.
    """

    group: AggregationResultGroup
    metrics: AggregationResultMetrics
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group = self.group.to_dict()

        metrics = self.metrics.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "group": group,
                "metrics": metrics,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.aggregation_result_group import AggregationResultGroup
        from ..models.aggregation_result_metrics import AggregationResultMetrics

        d = dict(src_dict)
        group = AggregationResultGroup.from_dict(d.pop("group"))

        metrics = AggregationResultMetrics.from_dict(d.pop("metrics"))

        aggregation_result = cls(
            group=group,
            metrics=metrics,
        )

        aggregation_result.additional_properties = d
        return aggregation_result

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
