from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SyncConfigMetric")


@_attrs_define
class SyncConfigMetric:
    """Sync configuration comparison metrics.

    Attributes:
        sync_config_id (str): Sync config identifier
        provider_type (str): Provider type
        avg_duration_seconds (float): Average sync duration
        avg_throughput_mbps (float): Average throughput
        success_rate (float): Success rate (0-1)
        total_files_synced (int): Total files synced
        total_bytes_synced (int): Total bytes synced
    """

    sync_config_id: str
    provider_type: str
    avg_duration_seconds: float
    avg_throughput_mbps: float
    success_rate: float
    total_files_synced: int
    total_bytes_synced: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sync_config_id = self.sync_config_id

        provider_type = self.provider_type

        avg_duration_seconds = self.avg_duration_seconds

        avg_throughput_mbps = self.avg_throughput_mbps

        success_rate = self.success_rate

        total_files_synced = self.total_files_synced

        total_bytes_synced = self.total_bytes_synced

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sync_config_id": sync_config_id,
                "provider_type": provider_type,
                "avg_duration_seconds": avg_duration_seconds,
                "avg_throughput_mbps": avg_throughput_mbps,
                "success_rate": success_rate,
                "total_files_synced": total_files_synced,
                "total_bytes_synced": total_bytes_synced,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sync_config_id = d.pop("sync_config_id")

        provider_type = d.pop("provider_type")

        avg_duration_seconds = d.pop("avg_duration_seconds")

        avg_throughput_mbps = d.pop("avg_throughput_mbps")

        success_rate = d.pop("success_rate")

        total_files_synced = d.pop("total_files_synced")

        total_bytes_synced = d.pop("total_bytes_synced")

        sync_config_metric = cls(
            sync_config_id=sync_config_id,
            provider_type=provider_type,
            avg_duration_seconds=avg_duration_seconds,
            avg_throughput_mbps=avg_throughput_mbps,
            success_rate=success_rate,
            total_files_synced=total_files_synced,
            total_bytes_synced=total_bytes_synced,
        )

        sync_config_metric.additional_properties = d
        return sync_config_metric

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
