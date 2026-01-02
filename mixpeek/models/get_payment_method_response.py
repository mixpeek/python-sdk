from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.payment_method_info import PaymentMethodInfo


T = TypeVar("T", bound="GetPaymentMethodResponse")


@_attrs_define
class GetPaymentMethodResponse:
    """Response with current payment method.

    Attributes:
        has_payment_method (bool): Whether organization has a payment method saved
        auto_billing_enabled (bool): Whether automatic billing is enabled
        payment_method (None | PaymentMethodInfo | Unset): Payment method details (null if none saved)
    """

    has_payment_method: bool
    auto_billing_enabled: bool
    payment_method: None | PaymentMethodInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.payment_method_info import PaymentMethodInfo

        has_payment_method = self.has_payment_method

        auto_billing_enabled = self.auto_billing_enabled

        payment_method: dict[str, Any] | None | Unset
        if isinstance(self.payment_method, Unset):
            payment_method = UNSET
        elif isinstance(self.payment_method, PaymentMethodInfo):
            payment_method = self.payment_method.to_dict()
        else:
            payment_method = self.payment_method

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "has_payment_method": has_payment_method,
                "auto_billing_enabled": auto_billing_enabled,
            }
        )
        if payment_method is not UNSET:
            field_dict["payment_method"] = payment_method

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.payment_method_info import PaymentMethodInfo

        d = dict(src_dict)
        has_payment_method = d.pop("has_payment_method")

        auto_billing_enabled = d.pop("auto_billing_enabled")

        def _parse_payment_method(data: object) -> None | PaymentMethodInfo | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                payment_method_type_0 = PaymentMethodInfo.from_dict(data)

                return payment_method_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PaymentMethodInfo | Unset, data)

        payment_method = _parse_payment_method(d.pop("payment_method", UNSET))

        get_payment_method_response = cls(
            has_payment_method=has_payment_method,
            auto_billing_enabled=auto_billing_enabled,
            payment_method=payment_method,
        )

        get_payment_method_response.additional_properties = d
        return get_payment_method_response

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
