from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BatchStatistics")


@_attrs_define
class BatchStatistics:
    """Statistics about batches in a bucket.

    Attributes:
        total (int | Unset): Total number of batches in this bucket Default: 0.
        active (int | Unset): Number of batches that are not completed (DRAFT, PENDING, IN_PROGRESS, PROCESSING)
            Default: 0.
        completed (int | Unset): Number of completed batches Default: 0.
        failed (int | Unset): Number of failed batches Default: 0.
    """

    total: int | Unset = 0
    active: int | Unset = 0
    completed: int | Unset = 0
    failed: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        active = self.active

        completed = self.completed

        failed = self.failed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total is not UNSET:
            field_dict["total"] = total
        if active is not UNSET:
            field_dict["active"] = active
        if completed is not UNSET:
            field_dict["completed"] = completed
        if failed is not UNSET:
            field_dict["failed"] = failed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total = d.pop("total", UNSET)

        active = d.pop("active", UNSET)

        completed = d.pop("completed", UNSET)

        failed = d.pop("failed", UNSET)

        batch_statistics = cls(
            total=total,
            active=active,
            completed=completed,
            failed=failed,
        )

        batch_statistics.additional_properties = d
        return batch_statistics

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
