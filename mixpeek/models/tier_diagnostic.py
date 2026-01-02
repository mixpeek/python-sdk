from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.task_progress import TaskProgress


T = TypeVar("T", bound="TierDiagnostic")


@_attrs_define
class TierDiagnostic:
    """Diagnostic information for a single tier.

    Attributes:
        tier_num (int): Tier number
        status (str): Tier status (PENDING, PROCESSING, COMPLETED, FAILED)
        task_id (None | str | Unset): Task ID for this tier
        started_at (datetime.datetime | None | Unset): When tier started
        completed_at (datetime.datetime | None | Unset): When tier completed
        duration_seconds (float | None | Unset): Duration in seconds
        progress (None | TaskProgress | Unset): Progress information
        ray_job_id (None | str | Unset): Ray job ID
        ray_dashboard_url (None | str | Unset): Link to Ray dashboard
        error (None | str | Unset): Error message if failed
        error_type (None | str | Unset): Error type if failed
    """

    tier_num: int
    status: str
    task_id: None | str | Unset = UNSET
    started_at: datetime.datetime | None | Unset = UNSET
    completed_at: datetime.datetime | None | Unset = UNSET
    duration_seconds: float | None | Unset = UNSET
    progress: None | TaskProgress | Unset = UNSET
    ray_job_id: None | str | Unset = UNSET
    ray_dashboard_url: None | str | Unset = UNSET
    error: None | str | Unset = UNSET
    error_type: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.task_progress import TaskProgress

        tier_num = self.tier_num

        status = self.status

        task_id: None | str | Unset
        if isinstance(self.task_id, Unset):
            task_id = UNSET
        else:
            task_id = self.task_id

        started_at: None | str | Unset
        if isinstance(self.started_at, Unset):
            started_at = UNSET
        elif isinstance(self.started_at, datetime.datetime):
            started_at = self.started_at.isoformat()
        else:
            started_at = self.started_at

        completed_at: None | str | Unset
        if isinstance(self.completed_at, Unset):
            completed_at = UNSET
        elif isinstance(self.completed_at, datetime.datetime):
            completed_at = self.completed_at.isoformat()
        else:
            completed_at = self.completed_at

        duration_seconds: float | None | Unset
        if isinstance(self.duration_seconds, Unset):
            duration_seconds = UNSET
        else:
            duration_seconds = self.duration_seconds

        progress: dict[str, Any] | None | Unset
        if isinstance(self.progress, Unset):
            progress = UNSET
        elif isinstance(self.progress, TaskProgress):
            progress = self.progress.to_dict()
        else:
            progress = self.progress

        ray_job_id: None | str | Unset
        if isinstance(self.ray_job_id, Unset):
            ray_job_id = UNSET
        else:
            ray_job_id = self.ray_job_id

        ray_dashboard_url: None | str | Unset
        if isinstance(self.ray_dashboard_url, Unset):
            ray_dashboard_url = UNSET
        else:
            ray_dashboard_url = self.ray_dashboard_url

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        error_type: None | str | Unset
        if isinstance(self.error_type, Unset):
            error_type = UNSET
        else:
            error_type = self.error_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tier_num": tier_num,
                "status": status,
            }
        )
        if task_id is not UNSET:
            field_dict["task_id"] = task_id
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if duration_seconds is not UNSET:
            field_dict["duration_seconds"] = duration_seconds
        if progress is not UNSET:
            field_dict["progress"] = progress
        if ray_job_id is not UNSET:
            field_dict["ray_job_id"] = ray_job_id
        if ray_dashboard_url is not UNSET:
            field_dict["ray_dashboard_url"] = ray_dashboard_url
        if error is not UNSET:
            field_dict["error"] = error
        if error_type is not UNSET:
            field_dict["error_type"] = error_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.task_progress import TaskProgress

        d = dict(src_dict)
        tier_num = d.pop("tier_num")

        status = d.pop("status")

        def _parse_task_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        task_id = _parse_task_id(d.pop("task_id", UNSET))

        def _parse_started_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                started_at_type_0 = isoparse(data)

                return started_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        started_at = _parse_started_at(d.pop("started_at", UNSET))

        def _parse_completed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completed_at_type_0 = isoparse(data)

                return completed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        completed_at = _parse_completed_at(d.pop("completed_at", UNSET))

        def _parse_duration_seconds(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        duration_seconds = _parse_duration_seconds(d.pop("duration_seconds", UNSET))

        def _parse_progress(data: object) -> None | TaskProgress | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                progress_type_0 = TaskProgress.from_dict(data)

                return progress_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TaskProgress | Unset, data)

        progress = _parse_progress(d.pop("progress", UNSET))

        def _parse_ray_job_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ray_job_id = _parse_ray_job_id(d.pop("ray_job_id", UNSET))

        def _parse_ray_dashboard_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ray_dashboard_url = _parse_ray_dashboard_url(d.pop("ray_dashboard_url", UNSET))

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        def _parse_error_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_type = _parse_error_type(d.pop("error_type", UNSET))

        tier_diagnostic = cls(
            tier_num=tier_num,
            status=status,
            task_id=task_id,
            started_at=started_at,
            completed_at=completed_at,
            duration_seconds=duration_seconds,
            progress=progress,
            ray_job_id=ray_job_id,
            ray_dashboard_url=ray_dashboard_url,
            error=error,
            error_type=error_type,
        )

        tier_diagnostic.additional_properties = d
        return tier_diagnostic

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
