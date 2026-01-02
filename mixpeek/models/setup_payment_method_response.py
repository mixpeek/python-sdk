from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SetupPaymentMethodResponse")


@_attrs_define
class SetupPaymentMethodResponse:
    """Response after creating a SetupIntent.

    Attributes:
        setup_intent_id (str): Stripe SetupIntent ID
        client_secret (str): Client secret for Stripe Elements
        customer_id (str): Stripe Customer ID
    """

    setup_intent_id: str
    client_secret: str
    customer_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        setup_intent_id = self.setup_intent_id

        client_secret = self.client_secret

        customer_id = self.customer_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "setup_intent_id": setup_intent_id,
                "client_secret": client_secret,
                "customer_id": customer_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        setup_intent_id = d.pop("setup_intent_id")

        client_secret = d.pop("client_secret")

        customer_id = d.pop("customer_id")

        setup_payment_method_response = cls(
            setup_intent_id=setup_intent_id,
            client_secret=client_secret,
            customer_id=customer_id,
        )

        setup_payment_method_response.additional_properties = d
        return setup_payment_method_response

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
