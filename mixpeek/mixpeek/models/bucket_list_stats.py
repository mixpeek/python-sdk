from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BucketListStats")


@_attrs_define
class BucketListStats:
    """Aggregate statistics for a list of buckets.

    Attributes:
        total_objects (int | Unset): Total number of objects across all buckets Default: 0.
        total_size_bytes (int | Unset): Total size in bytes across all buckets Default: 0.
        avg_objects_per_bucket (float | Unset): Average number of objects per bucket Default: 0.0.
        avg_size_per_bucket (float | Unset): Average size in bytes per bucket Default: 0.0.
    """

    total_objects: int | Unset = 0
    total_size_bytes: int | Unset = 0
    avg_objects_per_bucket: float | Unset = 0.0
    avg_size_per_bucket: float | Unset = 0.0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_objects = self.total_objects

        total_size_bytes = self.total_size_bytes

        avg_objects_per_bucket = self.avg_objects_per_bucket

        avg_size_per_bucket = self.avg_size_per_bucket

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_objects is not UNSET:
            field_dict["total_objects"] = total_objects
        if total_size_bytes is not UNSET:
            field_dict["total_size_bytes"] = total_size_bytes
        if avg_objects_per_bucket is not UNSET:
            field_dict["avg_objects_per_bucket"] = avg_objects_per_bucket
        if avg_size_per_bucket is not UNSET:
            field_dict["avg_size_per_bucket"] = avg_size_per_bucket

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_objects = d.pop("total_objects", UNSET)

        total_size_bytes = d.pop("total_size_bytes", UNSET)

        avg_objects_per_bucket = d.pop("avg_objects_per_bucket", UNSET)

        avg_size_per_bucket = d.pop("avg_size_per_bucket", UNSET)

        bucket_list_stats = cls(
            total_objects=total_objects,
            total_size_bytes=total_size_bytes,
            avg_objects_per_bucket=avg_objects_per_bucket,
            avg_size_per_bucket=avg_size_per_bucket,
        )

        bucket_list_stats.additional_properties = d
        return bucket_list_stats

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
