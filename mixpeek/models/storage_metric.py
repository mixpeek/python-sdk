from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="StorageMetric")


@_attrs_define
class StorageMetric:
    """Single time bucket storage metric.

    Attributes:
        time_bucket (datetime.datetime): Time bucket timestamp
        total_size_bytes (int): Total storage size in bytes
        object_count (int): Number of objects
        avg_size_bytes (int): Average object size in bytes
        growth_rate_percent (float | None | Unset): Growth rate vs previous period
    """

    time_bucket: datetime.datetime
    total_size_bytes: int
    object_count: int
    avg_size_bytes: int
    growth_rate_percent: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time_bucket = self.time_bucket.isoformat()

        total_size_bytes = self.total_size_bytes

        object_count = self.object_count

        avg_size_bytes = self.avg_size_bytes

        growth_rate_percent: float | None | Unset
        if isinstance(self.growth_rate_percent, Unset):
            growth_rate_percent = UNSET
        else:
            growth_rate_percent = self.growth_rate_percent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "time_bucket": time_bucket,
                "total_size_bytes": total_size_bytes,
                "object_count": object_count,
                "avg_size_bytes": avg_size_bytes,
            }
        )
        if growth_rate_percent is not UNSET:
            field_dict["growth_rate_percent"] = growth_rate_percent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        time_bucket = isoparse(d.pop("time_bucket"))

        total_size_bytes = d.pop("total_size_bytes")

        object_count = d.pop("object_count")

        avg_size_bytes = d.pop("avg_size_bytes")

        def _parse_growth_rate_percent(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        growth_rate_percent = _parse_growth_rate_percent(d.pop("growth_rate_percent", UNSET))

        storage_metric = cls(
            time_bucket=time_bucket,
            total_size_bytes=total_size_bytes,
            object_count=object_count,
            avg_size_bytes=avg_size_bytes,
            growth_rate_percent=growth_rate_percent,
        )

        storage_metric.additional_properties = d
        return storage_metric

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
