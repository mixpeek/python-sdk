from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StorageStatistics")


@_attrs_define
class StorageStatistics:
    """Statistics about object storage in a bucket.

    Attributes:
        total_size_bytes (int | Unset): Total size of all objects/blobs in the bucket in bytes Default: 0.
        avg_size_bytes (int | Unset): Average object size in bytes Default: 0.
        max_size_bytes (int | Unset): Size of the largest object in bytes Default: 0.
        min_size_bytes (int | Unset): Size of the smallest object in bytes Default: 0.
    """

    total_size_bytes: int | Unset = 0
    avg_size_bytes: int | Unset = 0
    max_size_bytes: int | Unset = 0
    min_size_bytes: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_size_bytes = self.total_size_bytes

        avg_size_bytes = self.avg_size_bytes

        max_size_bytes = self.max_size_bytes

        min_size_bytes = self.min_size_bytes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_size_bytes is not UNSET:
            field_dict["total_size_bytes"] = total_size_bytes
        if avg_size_bytes is not UNSET:
            field_dict["avg_size_bytes"] = avg_size_bytes
        if max_size_bytes is not UNSET:
            field_dict["max_size_bytes"] = max_size_bytes
        if min_size_bytes is not UNSET:
            field_dict["min_size_bytes"] = min_size_bytes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_size_bytes = d.pop("total_size_bytes", UNSET)

        avg_size_bytes = d.pop("avg_size_bytes", UNSET)

        max_size_bytes = d.pop("max_size_bytes", UNSET)

        min_size_bytes = d.pop("min_size_bytes", UNSET)

        storage_statistics = cls(
            total_size_bytes=total_size_bytes,
            avg_size_bytes=avg_size_bytes,
            max_size_bytes=max_size_bytes,
            min_size_bytes=min_size_bytes,
        )

        storage_statistics.additional_properties = d
        return storage_statistics

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
