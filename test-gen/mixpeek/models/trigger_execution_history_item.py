from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="TriggerExecutionHistoryItem")


@_attrs_define
class TriggerExecutionHistoryItem:
    """Single execution history item.

    Attributes:
        job_id (str): Job ID
        triggered_at (datetime.datetime): When trigger fired
        status (str): Execution status
        execution_time_ms (int | None | Unset): Execution time in milliseconds
        error (None | str | Unset): Error message if failed
        num_clusters (int | None | Unset): Number of clusters created
        num_documents (int | None | Unset): Number of documents processed
    """

    job_id: str
    triggered_at: datetime.datetime
    status: str
    execution_time_ms: int | None | Unset = UNSET
    error: None | str | Unset = UNSET
    num_clusters: int | None | Unset = UNSET
    num_documents: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job_id = self.job_id

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

        num_clusters: int | None | Unset
        if isinstance(self.num_clusters, Unset):
            num_clusters = UNSET
        else:
            num_clusters = self.num_clusters

        num_documents: int | None | Unset
        if isinstance(self.num_documents, Unset):
            num_documents = UNSET
        else:
            num_documents = self.num_documents

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "job_id": job_id,
                "triggered_at": triggered_at,
                "status": status,
            }
        )
        if execution_time_ms is not UNSET:
            field_dict["execution_time_ms"] = execution_time_ms
        if error is not UNSET:
            field_dict["error"] = error
        if num_clusters is not UNSET:
            field_dict["num_clusters"] = num_clusters
        if num_documents is not UNSET:
            field_dict["num_documents"] = num_documents

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        job_id = d.pop("job_id")

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

        def _parse_num_clusters(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        num_clusters = _parse_num_clusters(d.pop("num_clusters", UNSET))

        def _parse_num_documents(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        num_documents = _parse_num_documents(d.pop("num_documents", UNSET))

        trigger_execution_history_item = cls(
            job_id=job_id,
            triggered_at=triggered_at,
            status=status,
            execution_time_ms=execution_time_ms,
            error=error,
            num_clusters=num_clusters,
            num_documents=num_documents,
        )

        trigger_execution_history_item.additional_properties = d
        return trigger_execution_history_item

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
