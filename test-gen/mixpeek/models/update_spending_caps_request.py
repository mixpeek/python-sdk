from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateSpendingCapsRequest")


@_attrs_define
class UpdateSpendingCapsRequest:
    """Request to update spending cap configuration.

    Attributes:
        monthly_spending_budget (int | None | Unset): Soft spending limit in USD cents. Triggers alerts but doesn't
            block API access. Set to null to remove budget limit.
        spending_alert_thresholds (list[int] | None | Unset): Percentage thresholds for spending alerts (0-100). When
            current spending reaches each threshold, an alert is sent.
        spending_alerts_enabled (bool | None | Unset): Whether to send spending alerts when thresholds are crossed.
        hard_spending_cap (int | None | Unset): Hard spending limit in USD cents. When reached, API access is blocked.
            Set to null to remove hard cap.
        hard_cap_enabled (bool | None | Unset): Whether to enforce the hard spending cap.
    """

    monthly_spending_budget: int | None | Unset = UNSET
    spending_alert_thresholds: list[int] | None | Unset = UNSET
    spending_alerts_enabled: bool | None | Unset = UNSET
    hard_spending_cap: int | None | Unset = UNSET
    hard_cap_enabled: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        monthly_spending_budget: int | None | Unset
        if isinstance(self.monthly_spending_budget, Unset):
            monthly_spending_budget = UNSET
        else:
            monthly_spending_budget = self.monthly_spending_budget

        spending_alert_thresholds: list[int] | None | Unset
        if isinstance(self.spending_alert_thresholds, Unset):
            spending_alert_thresholds = UNSET
        elif isinstance(self.spending_alert_thresholds, list):
            spending_alert_thresholds = self.spending_alert_thresholds

        else:
            spending_alert_thresholds = self.spending_alert_thresholds

        spending_alerts_enabled: bool | None | Unset
        if isinstance(self.spending_alerts_enabled, Unset):
            spending_alerts_enabled = UNSET
        else:
            spending_alerts_enabled = self.spending_alerts_enabled

        hard_spending_cap: int | None | Unset
        if isinstance(self.hard_spending_cap, Unset):
            hard_spending_cap = UNSET
        else:
            hard_spending_cap = self.hard_spending_cap

        hard_cap_enabled: bool | None | Unset
        if isinstance(self.hard_cap_enabled, Unset):
            hard_cap_enabled = UNSET
        else:
            hard_cap_enabled = self.hard_cap_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if monthly_spending_budget is not UNSET:
            field_dict["monthly_spending_budget"] = monthly_spending_budget
        if spending_alert_thresholds is not UNSET:
            field_dict["spending_alert_thresholds"] = spending_alert_thresholds
        if spending_alerts_enabled is not UNSET:
            field_dict["spending_alerts_enabled"] = spending_alerts_enabled
        if hard_spending_cap is not UNSET:
            field_dict["hard_spending_cap"] = hard_spending_cap
        if hard_cap_enabled is not UNSET:
            field_dict["hard_cap_enabled"] = hard_cap_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_monthly_spending_budget(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        monthly_spending_budget = _parse_monthly_spending_budget(d.pop("monthly_spending_budget", UNSET))

        def _parse_spending_alert_thresholds(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                spending_alert_thresholds_type_0 = cast(list[int], data)

                return spending_alert_thresholds_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        spending_alert_thresholds = _parse_spending_alert_thresholds(d.pop("spending_alert_thresholds", UNSET))

        def _parse_spending_alerts_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        spending_alerts_enabled = _parse_spending_alerts_enabled(d.pop("spending_alerts_enabled", UNSET))

        def _parse_hard_spending_cap(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        hard_spending_cap = _parse_hard_spending_cap(d.pop("hard_spending_cap", UNSET))

        def _parse_hard_cap_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        hard_cap_enabled = _parse_hard_cap_enabled(d.pop("hard_cap_enabled", UNSET))

        update_spending_caps_request = cls(
            monthly_spending_budget=monthly_spending_budget,
            spending_alert_thresholds=spending_alert_thresholds,
            spending_alerts_enabled=spending_alerts_enabled,
            hard_spending_cap=hard_spending_cap,
            hard_cap_enabled=hard_cap_enabled,
        )

        update_spending_caps_request.additional_properties = d
        return update_spending_caps_request

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
