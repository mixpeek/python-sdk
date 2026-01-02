from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UsageStatistics")


@_attrs_define
class UsageStatistics:
    """Usage statistics for a retriever.

    Attributes:
        total_queries (int | Unset): Total number of queries executed Default: 0.
        queries_last_24h (int | Unset): Number of queries in the last 24 hours Default: 0.
        avg_latency_ms (float | Unset): Average latency in milliseconds Default: 0.0.
        error_rate (float | Unset): Error rate as a fraction (0.0 - 1.0) Default: 0.0.
        last_error (None | str | Unset): Most recent error message for debugging
        cache_hit_rate (float | None | Unset): Cache hit rate if caching is enabled (0.0 - 1.0)
    """

    total_queries: int | Unset = 0
    queries_last_24h: int | Unset = 0
    avg_latency_ms: float | Unset = 0.0
    error_rate: float | Unset = 0.0
    last_error: None | str | Unset = UNSET
    cache_hit_rate: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_queries = self.total_queries

        queries_last_24h = self.queries_last_24h

        avg_latency_ms = self.avg_latency_ms

        error_rate = self.error_rate

        last_error: None | str | Unset
        if isinstance(self.last_error, Unset):
            last_error = UNSET
        else:
            last_error = self.last_error

        cache_hit_rate: float | None | Unset
        if isinstance(self.cache_hit_rate, Unset):
            cache_hit_rate = UNSET
        else:
            cache_hit_rate = self.cache_hit_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_queries is not UNSET:
            field_dict["total_queries"] = total_queries
        if queries_last_24h is not UNSET:
            field_dict["queries_last_24h"] = queries_last_24h
        if avg_latency_ms is not UNSET:
            field_dict["avg_latency_ms"] = avg_latency_ms
        if error_rate is not UNSET:
            field_dict["error_rate"] = error_rate
        if last_error is not UNSET:
            field_dict["last_error"] = last_error
        if cache_hit_rate is not UNSET:
            field_dict["cache_hit_rate"] = cache_hit_rate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_queries = d.pop("total_queries", UNSET)

        queries_last_24h = d.pop("queries_last_24h", UNSET)

        avg_latency_ms = d.pop("avg_latency_ms", UNSET)

        error_rate = d.pop("error_rate", UNSET)

        def _parse_last_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_error = _parse_last_error(d.pop("last_error", UNSET))

        def _parse_cache_hit_rate(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        cache_hit_rate = _parse_cache_hit_rate(d.pop("cache_hit_rate", UNSET))

        usage_statistics = cls(
            total_queries=total_queries,
            queries_last_24h=queries_last_24h,
            avg_latency_ms=avg_latency_ms,
            error_rate=error_rate,
            last_error=last_error,
            cache_hit_rate=cache_hit_rate,
        )

        usage_statistics.additional_properties = d
        return usage_statistics

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
