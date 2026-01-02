from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.payment_method_info import PaymentMethodInfo


T = TypeVar("T", bound="ConfirmPaymentMethodResponse")


@_attrs_define
class ConfirmPaymentMethodResponse:
    """Response after confirming payment method.

    Attributes:
        payment_method (PaymentMethodInfo): Payment method details.
        auto_billing_enabled (bool): Whether auto-billing is now enabled
        billing_period_start (datetime.datetime): When the current billing period started
        success (bool | Unset): Whether payment method was successfully confirmed Default: True.
    """

    payment_method: PaymentMethodInfo
    auto_billing_enabled: bool
    billing_period_start: datetime.datetime
    success: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        payment_method = self.payment_method.to_dict()

        auto_billing_enabled = self.auto_billing_enabled

        billing_period_start = self.billing_period_start.isoformat()

        success = self.success

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "payment_method": payment_method,
                "auto_billing_enabled": auto_billing_enabled,
                "billing_period_start": billing_period_start,
            }
        )
        if success is not UNSET:
            field_dict["success"] = success

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.payment_method_info import PaymentMethodInfo

        d = dict(src_dict)
        payment_method = PaymentMethodInfo.from_dict(d.pop("payment_method"))

        auto_billing_enabled = d.pop("auto_billing_enabled")

        billing_period_start = isoparse(d.pop("billing_period_start"))

        success = d.pop("success", UNSET)

        confirm_payment_method_response = cls(
            payment_method=payment_method,
            auto_billing_enabled=auto_billing_enabled,
            billing_period_start=billing_period_start,
            success=success,
        )

        confirm_payment_method_response.additional_properties = d
        return confirm_payment_method_response

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
