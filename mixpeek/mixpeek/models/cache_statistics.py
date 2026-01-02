from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CacheStatistics")


@_attrs_define
class CacheStatistics:
    """Statistics about cache performance.

    Attributes:
        hit_count (int | Unset): Number of cache hits Default: 0.
        miss_count (int | Unset): Number of cache misses Default: 0.
        hit_rate (float | Unset): Cache hit rate (0.0 - 1.0) Default: 0.0.
        size_bytes (int | Unset): Total size of cached data in bytes Default: 0.
        entry_count (int | Unset): Number of entries in cache Default: 0.
        last_invalidated_at (datetime.datetime | None | Unset): When the cache was last invalidated
    """

    hit_count: int | Unset = 0
    miss_count: int | Unset = 0
    hit_rate: float | Unset = 0.0
    size_bytes: int | Unset = 0
    entry_count: int | Unset = 0
    last_invalidated_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hit_count = self.hit_count

        miss_count = self.miss_count

        hit_rate = self.hit_rate

        size_bytes = self.size_bytes

        entry_count = self.entry_count

        last_invalidated_at: None | str | Unset
        if isinstance(self.last_invalidated_at, Unset):
            last_invalidated_at = UNSET
        elif isinstance(self.last_invalidated_at, datetime.datetime):
            last_invalidated_at = self.last_invalidated_at.isoformat()
        else:
            last_invalidated_at = self.last_invalidated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hit_count is not UNSET:
            field_dict["hit_count"] = hit_count
        if miss_count is not UNSET:
            field_dict["miss_count"] = miss_count
        if hit_rate is not UNSET:
            field_dict["hit_rate"] = hit_rate
        if size_bytes is not UNSET:
            field_dict["size_bytes"] = size_bytes
        if entry_count is not UNSET:
            field_dict["entry_count"] = entry_count
        if last_invalidated_at is not UNSET:
            field_dict["last_invalidated_at"] = last_invalidated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        hit_count = d.pop("hit_count", UNSET)

        miss_count = d.pop("miss_count", UNSET)

        hit_rate = d.pop("hit_rate", UNSET)

        size_bytes = d.pop("size_bytes", UNSET)

        entry_count = d.pop("entry_count", UNSET)

        def _parse_last_invalidated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_invalidated_at_type_0 = isoparse(data)

                return last_invalidated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_invalidated_at = _parse_last_invalidated_at(d.pop("last_invalidated_at", UNSET))

        cache_statistics = cls(
            hit_count=hit_count,
            miss_count=miss_count,
            hit_rate=hit_rate,
            size_bytes=size_bytes,
            entry_count=entry_count,
            last_invalidated_at=last_invalidated_at,
        )

        cache_statistics.additional_properties = d
        return cache_statistics

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
