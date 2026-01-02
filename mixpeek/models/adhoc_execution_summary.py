from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdhocExecutionSummary")


@_attrs_define
class AdhocExecutionSummary:
    """Summary of an ad-hoc retriever execution from ClickHouse.

    Provides high-level execution metadata for ad-hoc retrievers without
    full document results. Used for listing and filtering execution history.

        Attributes:
            execution_id (str): Unique execution identifier.
            execution_mode (str): Execution mode ('adhoc').
            status (str): Execution status ('completed', 'failed', etc.).
            timestamp (Any): When the execution started (UTC).
            duration_ms (float): Total execution duration in milliseconds.
            credits_used (float): Credits consumed during execution.
            total_processed (int): Total documents processed across all stages.
            total_returned (int): Number of documents returned in final results.
            stages_completed (int): Number of stages completed.
            total_stages (int): Total number of stages in the pipeline.
            cache_hit_rate (float | None | Unset): Cache hit rate across stages (0.0-1.0).
            query_summary (None | str | Unset): Brief summary of the query inputs.
            collection_ids (list[str] | Unset): Collections queried during execution.
    """

    execution_id: str
    execution_mode: str
    status: str
    timestamp: Any
    duration_ms: float
    credits_used: float
    total_processed: int
    total_returned: int
    stages_completed: int
    total_stages: int
    cache_hit_rate: float | None | Unset = UNSET
    query_summary: None | str | Unset = UNSET
    collection_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        execution_id = self.execution_id

        execution_mode = self.execution_mode

        status = self.status

        timestamp = self.timestamp

        duration_ms = self.duration_ms

        credits_used = self.credits_used

        total_processed = self.total_processed

        total_returned = self.total_returned

        stages_completed = self.stages_completed

        total_stages = self.total_stages

        cache_hit_rate: float | None | Unset
        if isinstance(self.cache_hit_rate, Unset):
            cache_hit_rate = UNSET
        else:
            cache_hit_rate = self.cache_hit_rate

        query_summary: None | str | Unset
        if isinstance(self.query_summary, Unset):
            query_summary = UNSET
        else:
            query_summary = self.query_summary

        collection_ids: list[str] | Unset = UNSET
        if not isinstance(self.collection_ids, Unset):
            collection_ids = self.collection_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "execution_id": execution_id,
                "execution_mode": execution_mode,
                "status": status,
                "timestamp": timestamp,
                "duration_ms": duration_ms,
                "credits_used": credits_used,
                "total_processed": total_processed,
                "total_returned": total_returned,
                "stages_completed": stages_completed,
                "total_stages": total_stages,
            }
        )
        if cache_hit_rate is not UNSET:
            field_dict["cache_hit_rate"] = cache_hit_rate
        if query_summary is not UNSET:
            field_dict["query_summary"] = query_summary
        if collection_ids is not UNSET:
            field_dict["collection_ids"] = collection_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        execution_id = d.pop("execution_id")

        execution_mode = d.pop("execution_mode")

        status = d.pop("status")

        timestamp = d.pop("timestamp")

        duration_ms = d.pop("duration_ms")

        credits_used = d.pop("credits_used")

        total_processed = d.pop("total_processed")

        total_returned = d.pop("total_returned")

        stages_completed = d.pop("stages_completed")

        total_stages = d.pop("total_stages")

        def _parse_cache_hit_rate(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        cache_hit_rate = _parse_cache_hit_rate(d.pop("cache_hit_rate", UNSET))

        def _parse_query_summary(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        query_summary = _parse_query_summary(d.pop("query_summary", UNSET))

        collection_ids = cast(list[str], d.pop("collection_ids", UNSET))

        adhoc_execution_summary = cls(
            execution_id=execution_id,
            execution_mode=execution_mode,
            status=status,
            timestamp=timestamp,
            duration_ms=duration_ms,
            credits_used=credits_used,
            total_processed=total_processed,
            total_returned=total_returned,
            stages_completed=stages_completed,
            total_stages=total_stages,
            cache_hit_rate=cache_hit_rate,
            query_summary=query_summary,
            collection_ids=collection_ids,
        )

        adhoc_execution_summary.additional_properties = d
        return adhoc_execution_summary

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
