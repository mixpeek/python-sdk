from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="UsageMetric")


@_attrs_define
class UsageMetric:
    """Usage and cost metrics for a time bucket.

    Attributes:
        time_bucket (datetime.datetime): Time bucket timestamp
        storage_gb_hours (float): Storage GB-hours
        upload_operations (int): Upload operation count
        sync_operations (int): Sync operation count
        total_credits (int): Total credits consumed
        estimated_cost_usd (float): Estimated cost in USD
    """

    time_bucket: datetime.datetime
    storage_gb_hours: float
    upload_operations: int
    sync_operations: int
    total_credits: int
    estimated_cost_usd: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time_bucket = self.time_bucket.isoformat()

        storage_gb_hours = self.storage_gb_hours

        upload_operations = self.upload_operations

        sync_operations = self.sync_operations

        total_credits = self.total_credits

        estimated_cost_usd = self.estimated_cost_usd

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "time_bucket": time_bucket,
                "storage_gb_hours": storage_gb_hours,
                "upload_operations": upload_operations,
                "sync_operations": sync_operations,
                "total_credits": total_credits,
                "estimated_cost_usd": estimated_cost_usd,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        time_bucket = isoparse(d.pop("time_bucket"))

        storage_gb_hours = d.pop("storage_gb_hours")

        upload_operations = d.pop("upload_operations")

        sync_operations = d.pop("sync_operations")

        total_credits = d.pop("total_credits")

        estimated_cost_usd = d.pop("estimated_cost_usd")

        usage_metric = cls(
            time_bucket=time_bucket,
            storage_gb_hours=storage_gb_hours,
            upload_operations=upload_operations,
            sync_operations=sync_operations,
            total_credits=total_credits,
            estimated_cost_usd=estimated_cost_usd,
        )

        usage_metric.additional_properties = d
        return usage_metric

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
