from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.migration_stage import MigrationStage
from ..models.migration_status import MigrationStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="StageProgress")


@_attrs_define
class StageProgress:
    """Progress tracking for a migration stage.

    Attributes:
        stage (MigrationStage): Stages of migration execution.
        status (MigrationStatus): Migration execution status.
        started_at (datetime.datetime | None | Unset): Stage start time
        completed_at (datetime.datetime | None | Unset): Stage completion time
        progress_percent (float | Unset): Progress % Default: 0.0.
        items_total (int | Unset): Total items to process Default: 0.
        items_completed (int | Unset): Items completed Default: 0.
        items_failed (int | Unset): Items failed Default: 0.
        error_message (None | str | Unset): Error if failed
    """

    stage: MigrationStage
    status: MigrationStatus
    started_at: datetime.datetime | None | Unset = UNSET
    completed_at: datetime.datetime | None | Unset = UNSET
    progress_percent: float | Unset = 0.0
    items_total: int | Unset = 0
    items_completed: int | Unset = 0
    items_failed: int | Unset = 0
    error_message: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stage = self.stage.value

        status = self.status.value

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

        progress_percent = self.progress_percent

        items_total = self.items_total

        items_completed = self.items_completed

        items_failed = self.items_failed

        error_message: None | str | Unset
        if isinstance(self.error_message, Unset):
            error_message = UNSET
        else:
            error_message = self.error_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stage": stage,
                "status": status,
            }
        )
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if progress_percent is not UNSET:
            field_dict["progress_percent"] = progress_percent
        if items_total is not UNSET:
            field_dict["items_total"] = items_total
        if items_completed is not UNSET:
            field_dict["items_completed"] = items_completed
        if items_failed is not UNSET:
            field_dict["items_failed"] = items_failed
        if error_message is not UNSET:
            field_dict["error_message"] = error_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        stage = MigrationStage(d.pop("stage"))

        status = MigrationStatus(d.pop("status"))

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

        progress_percent = d.pop("progress_percent", UNSET)

        items_total = d.pop("items_total", UNSET)

        items_completed = d.pop("items_completed", UNSET)

        items_failed = d.pop("items_failed", UNSET)

        def _parse_error_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_message = _parse_error_message(d.pop("error_message", UNSET))

        stage_progress = cls(
            stage=stage,
            status=status,
            started_at=started_at,
            completed_at=completed_at,
            progress_percent=progress_percent,
            items_total=items_total,
            items_completed=items_completed,
            items_failed=items_failed,
            error_message=error_message,
        )

        stage_progress.additional_properties = d
        return stage_progress

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
