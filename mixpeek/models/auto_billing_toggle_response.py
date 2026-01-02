from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AutoBillingToggleResponse")


@_attrs_define
class AutoBillingToggleResponse:
    """Response after toggling auto-billing.

    Attributes:
        auto_billing_enabled (bool): New auto-billing status
        message (str): Human-readable message
        success (bool | Unset): Whether the operation was successful Default: True.
        billing_period_start (datetime.datetime | None | Unset): Billing period start (if enabled)
    """

    auto_billing_enabled: bool
    message: str
    success: bool | Unset = True
    billing_period_start: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_billing_enabled = self.auto_billing_enabled

        message = self.message

        success = self.success

        billing_period_start: None | str | Unset
        if isinstance(self.billing_period_start, Unset):
            billing_period_start = UNSET
        elif isinstance(self.billing_period_start, datetime.datetime):
            billing_period_start = self.billing_period_start.isoformat()
        else:
            billing_period_start = self.billing_period_start

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "auto_billing_enabled": auto_billing_enabled,
                "message": message,
            }
        )
        if success is not UNSET:
            field_dict["success"] = success
        if billing_period_start is not UNSET:
            field_dict["billing_period_start"] = billing_period_start

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        auto_billing_enabled = d.pop("auto_billing_enabled")

        message = d.pop("message")

        success = d.pop("success", UNSET)

        def _parse_billing_period_start(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                billing_period_start_type_0 = isoparse(data)

                return billing_period_start_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        billing_period_start = _parse_billing_period_start(d.pop("billing_period_start", UNSET))

        auto_billing_toggle_response = cls(
            auto_billing_enabled=auto_billing_enabled,
            message=message,
            success=success,
            billing_period_start=billing_period_start,
        )

        auto_billing_toggle_response.additional_properties = d
        return auto_billing_toggle_response

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
