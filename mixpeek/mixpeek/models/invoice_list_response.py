from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invoice_info import InvoiceInfo


T = TypeVar("T", bound="InvoiceListResponse")


@_attrs_define
class InvoiceListResponse:
    """Response with list of invoices.

    Attributes:
        total (int): Total number of invoices
        has_more (bool): Whether there are more invoices
        invoices (list[InvoiceInfo] | Unset): List of invoices
    """

    total: int
    has_more: bool
    invoices: list[InvoiceInfo] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        has_more = self.has_more

        invoices: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.invoices, Unset):
            invoices = []
            for invoices_item_data in self.invoices:
                invoices_item = invoices_item_data.to_dict()
                invoices.append(invoices_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "has_more": has_more,
            }
        )
        if invoices is not UNSET:
            field_dict["invoices"] = invoices

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.invoice_info import InvoiceInfo

        d = dict(src_dict)
        total = d.pop("total")

        has_more = d.pop("has_more")

        _invoices = d.pop("invoices", UNSET)
        invoices: list[InvoiceInfo] | Unset = UNSET
        if _invoices is not UNSET:
            invoices = []
            for invoices_item_data in _invoices:
                invoices_item = InvoiceInfo.from_dict(invoices_item_data)

                invoices.append(invoices_item)

        invoice_list_response = cls(
            total=total,
            has_more=has_more,
            invoices=invoices,
        )

        invoice_list_response.additional_properties = d
        return invoice_list_response

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
