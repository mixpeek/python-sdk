from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.usage_breakdown_response_by_extractor import UsageBreakdownResponseByExtractor
    from ..models.usage_breakdown_response_by_operation import UsageBreakdownResponseByOperation


T = TypeVar("T", bound="UsageBreakdownResponse")


@_attrs_define
class UsageBreakdownResponse:
    """Response with detailed usage breakdown.

    Attributes:
        billing_month (str): Billing month (YYYY-MM)
        total_credits (int): Total credits consumed
        total_cost_usd (float): Total cost in USD
        by_operation (UsageBreakdownResponseByOperation): Credits consumed by operation type
        by_extractor (UsageBreakdownResponseByExtractor): Credits consumed by extractor
        period_start (datetime.datetime): Start of billing period
        period_end (datetime.datetime): End of billing period
    """

    billing_month: str
    total_credits: int
    total_cost_usd: float
    by_operation: UsageBreakdownResponseByOperation
    by_extractor: UsageBreakdownResponseByExtractor
    period_start: datetime.datetime
    period_end: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        billing_month = self.billing_month

        total_credits = self.total_credits

        total_cost_usd = self.total_cost_usd

        by_operation = self.by_operation.to_dict()

        by_extractor = self.by_extractor.to_dict()

        period_start = self.period_start.isoformat()

        period_end = self.period_end.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "billing_month": billing_month,
                "total_credits": total_credits,
                "total_cost_usd": total_cost_usd,
                "by_operation": by_operation,
                "by_extractor": by_extractor,
                "period_start": period_start,
                "period_end": period_end,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.usage_breakdown_response_by_extractor import UsageBreakdownResponseByExtractor
        from ..models.usage_breakdown_response_by_operation import UsageBreakdownResponseByOperation

        d = dict(src_dict)
        billing_month = d.pop("billing_month")

        total_credits = d.pop("total_credits")

        total_cost_usd = d.pop("total_cost_usd")

        by_operation = UsageBreakdownResponseByOperation.from_dict(d.pop("by_operation"))

        by_extractor = UsageBreakdownResponseByExtractor.from_dict(d.pop("by_extractor"))

        period_start = isoparse(d.pop("period_start"))

        period_end = isoparse(d.pop("period_end"))

        usage_breakdown_response = cls(
            billing_month=billing_month,
            total_credits=total_credits,
            total_cost_usd=total_cost_usd,
            by_operation=by_operation,
            by_extractor=by_extractor,
            period_start=period_start,
            period_end=period_end,
        )

        usage_breakdown_response.additional_properties = d
        return usage_breakdown_response

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
