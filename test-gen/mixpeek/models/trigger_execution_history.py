from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="TriggerExecutionHistory")


@_attrs_define
class TriggerExecutionHistory:
    """Single execution history item.

    Attributes:
        task_id (str): Task ID
        triggered_at (datetime.datetime): When trigger fired
        status (str): Execution status
        execution_time_ms (int | None | Unset): Execution time in milliseconds
        error (None | str | Unset): Error message if failed
    """

    task_id: str
    triggered_at: datetime.datetime
    status: str
    execution_time_ms: int | None | Unset = UNSET
    error: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        task_id = self.task_id

        triggered_at = self.triggered_at.isoformat()

        status = self.status

        execution_time_ms: int | None | Unset
        if isinstance(self.execution_time_ms, Unset):
            execution_time_ms = UNSET
        else:
            execution_time_ms = self.execution_time_ms

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "task_id": task_id,
                "triggered_at": triggered_at,
                "status": status,
            }
        )
        if execution_time_ms is not UNSET:
            field_dict["execution_time_ms"] = execution_time_ms
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        task_id = d.pop("task_id")

        triggered_at = isoparse(d.pop("triggered_at"))

        status = d.pop("status")

        def _parse_execution_time_ms(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        execution_time_ms = _parse_execution_time_ms(d.pop("execution_time_ms", UNSET))

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        trigger_execution_history = cls(
            task_id=task_id,
            triggered_at=triggered_at,
            status=status,
            execution_time_ms=execution_time_ms,
            error=error,
        )

        trigger_execution_history.additional_properties = d
        return trigger_execution_history

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
