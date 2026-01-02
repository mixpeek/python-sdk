from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="SyncRunMetric")


@_attrs_define
class SyncRunMetric:
    """Single sync run metrics.

    Attributes:
        sync_run_id (str): Sync run identifier
        started_at (datetime.datetime): Sync start time
        duration_seconds (float): Sync duration in seconds
        files_discovered (int): Files discovered
        files_synced (int): Files successfully synced
        files_failed (int): Files that failed
        bytes_synced (int): Bytes synced
        throughput_mbps (float): Throughput in MB/s
        status (str): Sync status
        provider_type (str): Provider type (s3, gcs, etc)
    """

    sync_run_id: str
    started_at: datetime.datetime
    duration_seconds: float
    files_discovered: int
    files_synced: int
    files_failed: int
    bytes_synced: int
    throughput_mbps: float
    status: str
    provider_type: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sync_run_id = self.sync_run_id

        started_at = self.started_at.isoformat()

        duration_seconds = self.duration_seconds

        files_discovered = self.files_discovered

        files_synced = self.files_synced

        files_failed = self.files_failed

        bytes_synced = self.bytes_synced

        throughput_mbps = self.throughput_mbps

        status = self.status

        provider_type = self.provider_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sync_run_id": sync_run_id,
                "started_at": started_at,
                "duration_seconds": duration_seconds,
                "files_discovered": files_discovered,
                "files_synced": files_synced,
                "files_failed": files_failed,
                "bytes_synced": bytes_synced,
                "throughput_mbps": throughput_mbps,
                "status": status,
                "provider_type": provider_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sync_run_id = d.pop("sync_run_id")

        started_at = isoparse(d.pop("started_at"))

        duration_seconds = d.pop("duration_seconds")

        files_discovered = d.pop("files_discovered")

        files_synced = d.pop("files_synced")

        files_failed = d.pop("files_failed")

        bytes_synced = d.pop("bytes_synced")

        throughput_mbps = d.pop("throughput_mbps")

        status = d.pop("status")

        provider_type = d.pop("provider_type")

        sync_run_metric = cls(
            sync_run_id=sync_run_id,
            started_at=started_at,
            duration_seconds=duration_seconds,
            files_discovered=files_discovered,
            files_synced=files_synced,
            files_failed=files_failed,
            bytes_synced=bytes_synced,
            throughput_mbps=throughput_mbps,
            status=status,
            provider_type=provider_type,
        )

        sync_run_metric.additional_properties = d
        return sync_run_metric

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
