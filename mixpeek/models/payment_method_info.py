from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PaymentMethodInfo")


@_attrs_define
class PaymentMethodInfo:
    """Payment method details.

    Attributes:
        payment_method_id (str): Stripe PaymentMethod ID
        type_ (str): Payment method type
        card_last4 (str): Last 4 digits of card
        card_brand (str): Card brand
    """

    payment_method_id: str
    type_: str
    card_last4: str
    card_brand: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        payment_method_id = self.payment_method_id

        type_ = self.type_

        card_last4 = self.card_last4

        card_brand = self.card_brand

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "payment_method_id": payment_method_id,
                "type": type_,
                "card_last4": card_last4,
                "card_brand": card_brand,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        payment_method_id = d.pop("payment_method_id")

        type_ = d.pop("type")

        card_last4 = d.pop("card_last4")

        card_brand = d.pop("card_brand")

        payment_method_info = cls(
            payment_method_id=payment_method_id,
            type_=type_,
            card_last4=card_last4,
            card_brand=card_brand,
        )

        payment_method_info.additional_properties = d
        return payment_method_info

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
