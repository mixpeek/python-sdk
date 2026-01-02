from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.batch_confirm_request_confirmations_item import BatchConfirmRequestConfirmationsItem


T = TypeVar("T", bound="BatchConfirmRequest")


@_attrs_define
class BatchConfirmRequest:
    """Request to confirm multiple uploads in batch.

    Attributes:
        confirmations (list[BatchConfirmRequestConfirmationsItem]): List of confirmations with upload_id, etag,
            file_size_bytes
    """

    confirmations: list[BatchConfirmRequestConfirmationsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        confirmations = []
        for confirmations_item_data in self.confirmations:
            confirmations_item = confirmations_item_data.to_dict()
            confirmations.append(confirmations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "confirmations": confirmations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.batch_confirm_request_confirmations_item import BatchConfirmRequestConfirmationsItem

        d = dict(src_dict)
        confirmations = []
        _confirmations = d.pop("confirmations")
        for confirmations_item_data in _confirmations:
            confirmations_item = BatchConfirmRequestConfirmationsItem.from_dict(confirmations_item_data)

            confirmations.append(confirmations_item)

        batch_confirm_request = cls(
            confirmations=confirmations,
        )

        batch_confirm_request.additional_properties = d
        return batch_confirm_request

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
