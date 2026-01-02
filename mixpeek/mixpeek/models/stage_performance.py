from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="StagePerformance")


@_attrs_define
class StagePerformance:
    """Performance statistics for a retriever stage.

    Attributes:
        avg_execution_ms (float | Unset): Average execution time in milliseconds Default: 0.0.
        execution_count (int | Unset): Number of times executed Default: 0.
        error_count (int | Unset): Number of errors encountered Default: 0.
        last_executed_at (datetime.datetime | None | Unset): Last time this stage was executed
    """

    avg_execution_ms: float | Unset = 0.0
    execution_count: int | Unset = 0
    error_count: int | Unset = 0
    last_executed_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avg_execution_ms = self.avg_execution_ms

        execution_count = self.execution_count

        error_count = self.error_count

        last_executed_at: None | str | Unset
        if isinstance(self.last_executed_at, Unset):
            last_executed_at = UNSET
        elif isinstance(self.last_executed_at, datetime.datetime):
            last_executed_at = self.last_executed_at.isoformat()
        else:
            last_executed_at = self.last_executed_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avg_execution_ms is not UNSET:
            field_dict["avg_execution_ms"] = avg_execution_ms
        if execution_count is not UNSET:
            field_dict["execution_count"] = execution_count
        if error_count is not UNSET:
            field_dict["error_count"] = error_count
        if last_executed_at is not UNSET:
            field_dict["last_executed_at"] = last_executed_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        avg_execution_ms = d.pop("avg_execution_ms", UNSET)

        execution_count = d.pop("execution_count", UNSET)

        error_count = d.pop("error_count", UNSET)

        def _parse_last_executed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_executed_at_type_0 = isoparse(data)

                return last_executed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_executed_at = _parse_last_executed_at(d.pop("last_executed_at", UNSET))

        stage_performance = cls(
            avg_execution_ms=avg_execution_ms,
            execution_count=execution_count,
            error_count=error_count,
            last_executed_at=last_executed_at,
        )

        stage_performance.additional_properties = d
        return stage_performance

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
