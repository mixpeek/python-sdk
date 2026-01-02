from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="InvoiceInfo")


@_attrs_define
class InvoiceInfo:
    """Information about a monthly invoice.

    Attributes:
        invoice_id (str): Stripe Invoice ID
        invoice_url (str): Stripe-hosted invoice URL
        invoice_pdf (str): PDF download URL
        amount_due (int): Amount due in cents
        amount_paid (int): Amount paid in cents
        status (str): Invoice status
        billing_month (str): Billing month (YYYY-MM)
        total_credits (int): Total credits billed
        created (datetime.datetime): When invoice was created
        paid_at (datetime.datetime | None | Unset): When invoice was paid
    """

    invoice_id: str
    invoice_url: str
    invoice_pdf: str
    amount_due: int
    amount_paid: int
    status: str
    billing_month: str
    total_credits: int
    created: datetime.datetime
    paid_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        invoice_id = self.invoice_id

        invoice_url = self.invoice_url

        invoice_pdf = self.invoice_pdf

        amount_due = self.amount_due

        amount_paid = self.amount_paid

        status = self.status

        billing_month = self.billing_month

        total_credits = self.total_credits

        created = self.created.isoformat()

        paid_at: None | str | Unset
        if isinstance(self.paid_at, Unset):
            paid_at = UNSET
        elif isinstance(self.paid_at, datetime.datetime):
            paid_at = self.paid_at.isoformat()
        else:
            paid_at = self.paid_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "invoice_id": invoice_id,
                "invoice_url": invoice_url,
                "invoice_pdf": invoice_pdf,
                "amount_due": amount_due,
                "amount_paid": amount_paid,
                "status": status,
                "billing_month": billing_month,
                "total_credits": total_credits,
                "created": created,
            }
        )
        if paid_at is not UNSET:
            field_dict["paid_at"] = paid_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        invoice_id = d.pop("invoice_id")

        invoice_url = d.pop("invoice_url")

        invoice_pdf = d.pop("invoice_pdf")

        amount_due = d.pop("amount_due")

        amount_paid = d.pop("amount_paid")

        status = d.pop("status")

        billing_month = d.pop("billing_month")

        total_credits = d.pop("total_credits")

        created = isoparse(d.pop("created"))

        def _parse_paid_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                paid_at_type_0 = isoparse(data)

                return paid_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        paid_at = _parse_paid_at(d.pop("paid_at", UNSET))

        invoice_info = cls(
            invoice_id=invoice_id,
            invoice_url=invoice_url,
            invoice_pdf=invoice_pdf,
            amount_due=amount_due,
            amount_paid=amount_paid,
            status=status,
            billing_month=billing_month,
            total_credits=total_credits,
            created=created,
            paid_at=paid_at,
        )

        invoice_info.additional_properties = d
        return invoice_info

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
