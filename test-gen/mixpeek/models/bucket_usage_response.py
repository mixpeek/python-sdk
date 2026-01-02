from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.cost_breakdown import CostBreakdown
    from ..models.time_range import TimeRange
    from ..models.usage_metric import UsageMetric


T = TypeVar("T", bound="BucketUsageResponse")


@_attrs_define
class BucketUsageResponse:
    """Bucket usage and cost analytics response.

    Attributes:
        bucket_id (str): Bucket identifier
        time_range (TimeRange): Time range for analytics queries.
        metrics (list[UsageMetric]): Usage metrics
        cost_breakdown (CostBreakdown): Cost breakdown by category.
        total_credits (int): Total credits consumed
        total_cost_usd (float): Total cost in USD
    """

    bucket_id: str
    time_range: TimeRange
    metrics: list[UsageMetric]
    cost_breakdown: CostBreakdown
    total_credits: int
    total_cost_usd: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bucket_id = self.bucket_id

        time_range = self.time_range.to_dict()

        metrics = []
        for metrics_item_data in self.metrics:
            metrics_item = metrics_item_data.to_dict()
            metrics.append(metrics_item)

        cost_breakdown = self.cost_breakdown.to_dict()

        total_credits = self.total_credits

        total_cost_usd = self.total_cost_usd

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bucket_id": bucket_id,
                "time_range": time_range,
                "metrics": metrics,
                "cost_breakdown": cost_breakdown,
                "total_credits": total_credits,
                "total_cost_usd": total_cost_usd,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cost_breakdown import CostBreakdown
        from ..models.time_range import TimeRange
        from ..models.usage_metric import UsageMetric

        d = dict(src_dict)
        bucket_id = d.pop("bucket_id")

        time_range = TimeRange.from_dict(d.pop("time_range"))

        metrics = []
        _metrics = d.pop("metrics")
        for metrics_item_data in _metrics:
            metrics_item = UsageMetric.from_dict(metrics_item_data)

            metrics.append(metrics_item)

        cost_breakdown = CostBreakdown.from_dict(d.pop("cost_breakdown"))

        total_credits = d.pop("total_credits")

        total_cost_usd = d.pop("total_cost_usd")

        bucket_usage_response = cls(
            bucket_id=bucket_id,
            time_range=time_range,
            metrics=metrics,
            cost_breakdown=cost_breakdown,
            total_credits=total_credits,
            total_cost_usd=total_cost_usd,
        )

        bucket_usage_response.additional_properties = d
        return bucket_usage_response

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
