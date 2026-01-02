from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpendingCapsResponse")


@_attrs_define
class SpendingCapsResponse:
    """Response with spending cap configuration.

    Attributes:
        current_spending_cents (int): Current spending in current billing cycle (cents)
        current_spending_usd (float): Current spending in current billing cycle (USD)
        monthly_spending_budget (int | None | Unset): Soft spending limit in USD cents (null = unlimited)
        monthly_spending_budget_usd (float | None | Unset): Soft spending limit in USD
        spending_alert_thresholds (list[int] | Unset): Percentage thresholds for spending alerts
        spending_alerts_enabled (bool | Unset): Whether spending alerts are enabled Default: True.
        spending_alerts_sent (list[int] | Unset): Alert thresholds triggered in current billing cycle
        hard_spending_cap (int | None | Unset): Hard spending limit in USD cents (null = no hard cap)
        hard_spending_cap_usd (float | None | Unset): Hard spending limit in USD
        hard_cap_enabled (bool | Unset): Whether hard spending cap is enforced Default: False.
        budget_percentage_used (float | None | Unset): Percentage of budget used (null if no budget set)
    """

    current_spending_cents: int
    current_spending_usd: float
    monthly_spending_budget: int | None | Unset = UNSET
    monthly_spending_budget_usd: float | None | Unset = UNSET
    spending_alert_thresholds: list[int] | Unset = UNSET
    spending_alerts_enabled: bool | Unset = True
    spending_alerts_sent: list[int] | Unset = UNSET
    hard_spending_cap: int | None | Unset = UNSET
    hard_spending_cap_usd: float | None | Unset = UNSET
    hard_cap_enabled: bool | Unset = False
    budget_percentage_used: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_spending_cents = self.current_spending_cents

        current_spending_usd = self.current_spending_usd

        monthly_spending_budget: int | None | Unset
        if isinstance(self.monthly_spending_budget, Unset):
            monthly_spending_budget = UNSET
        else:
            monthly_spending_budget = self.monthly_spending_budget

        monthly_spending_budget_usd: float | None | Unset
        if isinstance(self.monthly_spending_budget_usd, Unset):
            monthly_spending_budget_usd = UNSET
        else:
            monthly_spending_budget_usd = self.monthly_spending_budget_usd

        spending_alert_thresholds: list[int] | Unset = UNSET
        if not isinstance(self.spending_alert_thresholds, Unset):
            spending_alert_thresholds = self.spending_alert_thresholds

        spending_alerts_enabled = self.spending_alerts_enabled

        spending_alerts_sent: list[int] | Unset = UNSET
        if not isinstance(self.spending_alerts_sent, Unset):
            spending_alerts_sent = self.spending_alerts_sent

        hard_spending_cap: int | None | Unset
        if isinstance(self.hard_spending_cap, Unset):
            hard_spending_cap = UNSET
        else:
            hard_spending_cap = self.hard_spending_cap

        hard_spending_cap_usd: float | None | Unset
        if isinstance(self.hard_spending_cap_usd, Unset):
            hard_spending_cap_usd = UNSET
        else:
            hard_spending_cap_usd = self.hard_spending_cap_usd

        hard_cap_enabled = self.hard_cap_enabled

        budget_percentage_used: float | None | Unset
        if isinstance(self.budget_percentage_used, Unset):
            budget_percentage_used = UNSET
        else:
            budget_percentage_used = self.budget_percentage_used

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "current_spending_cents": current_spending_cents,
                "current_spending_usd": current_spending_usd,
            }
        )
        if monthly_spending_budget is not UNSET:
            field_dict["monthly_spending_budget"] = monthly_spending_budget
        if monthly_spending_budget_usd is not UNSET:
            field_dict["monthly_spending_budget_usd"] = monthly_spending_budget_usd
        if spending_alert_thresholds is not UNSET:
            field_dict["spending_alert_thresholds"] = spending_alert_thresholds
        if spending_alerts_enabled is not UNSET:
            field_dict["spending_alerts_enabled"] = spending_alerts_enabled
        if spending_alerts_sent is not UNSET:
            field_dict["spending_alerts_sent"] = spending_alerts_sent
        if hard_spending_cap is not UNSET:
            field_dict["hard_spending_cap"] = hard_spending_cap
        if hard_spending_cap_usd is not UNSET:
            field_dict["hard_spending_cap_usd"] = hard_spending_cap_usd
        if hard_cap_enabled is not UNSET:
            field_dict["hard_cap_enabled"] = hard_cap_enabled
        if budget_percentage_used is not UNSET:
            field_dict["budget_percentage_used"] = budget_percentage_used

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        current_spending_cents = d.pop("current_spending_cents")

        current_spending_usd = d.pop("current_spending_usd")

        def _parse_monthly_spending_budget(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        monthly_spending_budget = _parse_monthly_spending_budget(d.pop("monthly_spending_budget", UNSET))

        def _parse_monthly_spending_budget_usd(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        monthly_spending_budget_usd = _parse_monthly_spending_budget_usd(d.pop("monthly_spending_budget_usd", UNSET))

        spending_alert_thresholds = cast(list[int], d.pop("spending_alert_thresholds", UNSET))

        spending_alerts_enabled = d.pop("spending_alerts_enabled", UNSET)

        spending_alerts_sent = cast(list[int], d.pop("spending_alerts_sent", UNSET))

        def _parse_hard_spending_cap(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        hard_spending_cap = _parse_hard_spending_cap(d.pop("hard_spending_cap", UNSET))

        def _parse_hard_spending_cap_usd(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        hard_spending_cap_usd = _parse_hard_spending_cap_usd(d.pop("hard_spending_cap_usd", UNSET))

        hard_cap_enabled = d.pop("hard_cap_enabled", UNSET)

        def _parse_budget_percentage_used(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        budget_percentage_used = _parse_budget_percentage_used(d.pop("budget_percentage_used", UNSET))

        spending_caps_response = cls(
            current_spending_cents=current_spending_cents,
            current_spending_usd=current_spending_usd,
            monthly_spending_budget=monthly_spending_budget,
            monthly_spending_budget_usd=monthly_spending_budget_usd,
            spending_alert_thresholds=spending_alert_thresholds,
            spending_alerts_enabled=spending_alerts_enabled,
            spending_alerts_sent=spending_alerts_sent,
            hard_spending_cap=hard_spending_cap,
            hard_spending_cap_usd=hard_spending_cap_usd,
            hard_cap_enabled=hard_cap_enabled,
            budget_percentage_used=budget_percentage_used,
        )

        spending_caps_response.additional_properties = d
        return spending_caps_response

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
