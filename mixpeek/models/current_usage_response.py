from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CurrentUsageResponse")


@_attrs_define
class CurrentUsageResponse:
    """Response with current month usage.

    Attributes:
        current_month_usage (int): Credits consumed in current billing cycle
        billing_month (str): Current billing month (YYYY-MM)
        billing_period_start (datetime.datetime): Start of current billing period
        billing_period_end (datetime.datetime): End of current billing period
        estimated_cost_usd (float): Estimated cost for current usage
        auto_billing_enabled (bool): Whether auto-billing is enabled
        next_invoice_date (datetime.datetime): When next invoice will be generated
        credit_rate (float | Unset): Cost per credit in USD Default: 0.001.
    """

    current_month_usage: int
    billing_month: str
    billing_period_start: datetime.datetime
    billing_period_end: datetime.datetime
    estimated_cost_usd: float
    auto_billing_enabled: bool
    next_invoice_date: datetime.datetime
    credit_rate: float | Unset = 0.001
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_month_usage = self.current_month_usage

        billing_month = self.billing_month

        billing_period_start = self.billing_period_start.isoformat()

        billing_period_end = self.billing_period_end.isoformat()

        estimated_cost_usd = self.estimated_cost_usd

        auto_billing_enabled = self.auto_billing_enabled

        next_invoice_date = self.next_invoice_date.isoformat()

        credit_rate = self.credit_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "current_month_usage": current_month_usage,
                "billing_month": billing_month,
                "billing_period_start": billing_period_start,
                "billing_period_end": billing_period_end,
                "estimated_cost_usd": estimated_cost_usd,
                "auto_billing_enabled": auto_billing_enabled,
                "next_invoice_date": next_invoice_date,
            }
        )
        if credit_rate is not UNSET:
            field_dict["credit_rate"] = credit_rate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        current_month_usage = d.pop("current_month_usage")

        billing_month = d.pop("billing_month")

        billing_period_start = isoparse(d.pop("billing_period_start"))

        billing_period_end = isoparse(d.pop("billing_period_end"))

        estimated_cost_usd = d.pop("estimated_cost_usd")

        auto_billing_enabled = d.pop("auto_billing_enabled")

        next_invoice_date = isoparse(d.pop("next_invoice_date"))

        credit_rate = d.pop("credit_rate", UNSET)

        current_usage_response = cls(
            current_month_usage=current_month_usage,
            billing_month=billing_month,
            billing_period_start=billing_period_start,
            billing_period_end=billing_period_end,
            estimated_cost_usd=estimated_cost_usd,
            auto_billing_enabled=auto_billing_enabled,
            next_invoice_date=next_invoice_date,
            credit_rate=credit_rate,
        )

        current_usage_response.additional_properties = d
        return current_usage_response

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
