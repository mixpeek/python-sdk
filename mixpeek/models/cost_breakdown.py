from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CostBreakdown")


@_attrs_define
class CostBreakdown:
    """Cost breakdown by category.

    Attributes:
        storage_percent (float): Storage cost percentage
        upload_percent (float): Upload cost percentage
        sync_percent (float): Sync cost percentage
        other_percent (float): Other cost percentage
    """

    storage_percent: float
    upload_percent: float
    sync_percent: float
    other_percent: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        storage_percent = self.storage_percent

        upload_percent = self.upload_percent

        sync_percent = self.sync_percent

        other_percent = self.other_percent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "storage_percent": storage_percent,
                "upload_percent": upload_percent,
                "sync_percent": sync_percent,
                "other_percent": other_percent,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        storage_percent = d.pop("storage_percent")

        upload_percent = d.pop("upload_percent")

        sync_percent = d.pop("sync_percent")

        other_percent = d.pop("other_percent")

        cost_breakdown = cls(
            storage_percent=storage_percent,
            upload_percent=upload_percent,
            sync_percent=sync_percent,
            other_percent=other_percent,
        )

        cost_breakdown.additional_properties = d
        return cost_breakdown

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
