from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="RetrieverExecutionSummary")


@_attrs_define
class RetrieverExecutionSummary:
    """Summary document used for execution history listings.

    Attributes:
        execution_id (str): Execution identifier
        status (str): Execution status
        created_at (datetime.datetime): Creation timestamp
        duration_ms (float): Total execution time in ms
        credits_used (float): Credits consumed
        total_processed (int): Documents processed across stages
        total_returned (int): Documents returned to caller
        completed_at (datetime.datetime | None | Unset): Completion timestamp when available
        cache_hit_rate (float | None | Unset): Average cache hit rate for stages
        inputs_hash (None | str | Unset): Stable hash of retriever inputs for dedupe
        query_summary (None | str | Unset): Representative snippet of query inputs
    """

    execution_id: str
    status: str
    created_at: datetime.datetime
    duration_ms: float
    credits_used: float
    total_processed: int
    total_returned: int
    completed_at: datetime.datetime | None | Unset = UNSET
    cache_hit_rate: float | None | Unset = UNSET
    inputs_hash: None | str | Unset = UNSET
    query_summary: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        execution_id = self.execution_id

        status = self.status

        created_at = self.created_at.isoformat()

        duration_ms = self.duration_ms

        credits_used = self.credits_used

        total_processed = self.total_processed

        total_returned = self.total_returned

        completed_at: None | str | Unset
        if isinstance(self.completed_at, Unset):
            completed_at = UNSET
        elif isinstance(self.completed_at, datetime.datetime):
            completed_at = self.completed_at.isoformat()
        else:
            completed_at = self.completed_at

        cache_hit_rate: float | None | Unset
        if isinstance(self.cache_hit_rate, Unset):
            cache_hit_rate = UNSET
        else:
            cache_hit_rate = self.cache_hit_rate

        inputs_hash: None | str | Unset
        if isinstance(self.inputs_hash, Unset):
            inputs_hash = UNSET
        else:
            inputs_hash = self.inputs_hash

        query_summary: None | str | Unset
        if isinstance(self.query_summary, Unset):
            query_summary = UNSET
        else:
            query_summary = self.query_summary

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "execution_id": execution_id,
                "status": status,
                "created_at": created_at,
                "duration_ms": duration_ms,
                "credits_used": credits_used,
                "total_processed": total_processed,
                "total_returned": total_returned,
            }
        )
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if cache_hit_rate is not UNSET:
            field_dict["cache_hit_rate"] = cache_hit_rate
        if inputs_hash is not UNSET:
            field_dict["inputs_hash"] = inputs_hash
        if query_summary is not UNSET:
            field_dict["query_summary"] = query_summary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        execution_id = d.pop("execution_id")

        status = d.pop("status")

        created_at = isoparse(d.pop("created_at"))

        duration_ms = d.pop("duration_ms")

        credits_used = d.pop("credits_used")

        total_processed = d.pop("total_processed")

        total_returned = d.pop("total_returned")

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

        def _parse_cache_hit_rate(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        cache_hit_rate = _parse_cache_hit_rate(d.pop("cache_hit_rate", UNSET))

        def _parse_inputs_hash(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        inputs_hash = _parse_inputs_hash(d.pop("inputs_hash", UNSET))

        def _parse_query_summary(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        query_summary = _parse_query_summary(d.pop("query_summary", UNSET))

        retriever_execution_summary = cls(
            execution_id=execution_id,
            status=status,
            created_at=created_at,
            duration_ms=duration_ms,
            credits_used=credits_used,
            total_processed=total_processed,
            total_returned=total_returned,
            completed_at=completed_at,
            cache_hit_rate=cache_hit_rate,
            inputs_hash=inputs_hash,
            query_summary=query_summary,
        )

        retriever_execution_summary.additional_properties = d
        return retriever_execution_summary

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
