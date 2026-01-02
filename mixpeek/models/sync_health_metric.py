from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="SyncHealthMetric")


@_attrs_define
class SyncHealthMetric:
    """Sync health metrics per config.

    Attributes:
        sync_config_id (str): Sync config identifier
        consecutive_failures (int): Consecutive failure count
        failure_rate (float): Failure rate (0-1)
        last_success_at (datetime.datetime | None | Unset): Last successful sync
        last_failure_at (datetime.datetime | None | Unset): Last failed sync
    """

    sync_config_id: str
    consecutive_failures: int
    failure_rate: float
    last_success_at: datetime.datetime | None | Unset = UNSET
    last_failure_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sync_config_id = self.sync_config_id

        consecutive_failures = self.consecutive_failures

        failure_rate = self.failure_rate

        last_success_at: None | str | Unset
        if isinstance(self.last_success_at, Unset):
            last_success_at = UNSET
        elif isinstance(self.last_success_at, datetime.datetime):
            last_success_at = self.last_success_at.isoformat()
        else:
            last_success_at = self.last_success_at

        last_failure_at: None | str | Unset
        if isinstance(self.last_failure_at, Unset):
            last_failure_at = UNSET
        elif isinstance(self.last_failure_at, datetime.datetime):
            last_failure_at = self.last_failure_at.isoformat()
        else:
            last_failure_at = self.last_failure_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sync_config_id": sync_config_id,
                "consecutive_failures": consecutive_failures,
                "failure_rate": failure_rate,
            }
        )
        if last_success_at is not UNSET:
            field_dict["last_success_at"] = last_success_at
        if last_failure_at is not UNSET:
            field_dict["last_failure_at"] = last_failure_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sync_config_id = d.pop("sync_config_id")

        consecutive_failures = d.pop("consecutive_failures")

        failure_rate = d.pop("failure_rate")

        def _parse_last_success_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_success_at_type_0 = isoparse(data)

                return last_success_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_success_at = _parse_last_success_at(d.pop("last_success_at", UNSET))

        def _parse_last_failure_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_failure_at_type_0 = isoparse(data)

                return last_failure_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_failure_at = _parse_last_failure_at(d.pop("last_failure_at", UNSET))

        sync_health_metric = cls(
            sync_config_id=sync_config_id,
            consecutive_failures=consecutive_failures,
            failure_rate=failure_rate,
            last_success_at=last_success_at,
            last_failure_at=last_failure_at,
        )

        sync_health_metric.additional_properties = d
        return sync_health_metric

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
