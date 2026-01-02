from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="FieldUsageStat")


@_attrs_define
class FieldUsageStat:
    """Usage statistics for a filtered field.

    Attributes:
        field_name (str): Field name
        query_count (int): Number of queries using this field
        unique_queries (int): Number of unique query executions
        is_indexed (bool): Whether field has an index
        is_protected (bool): Whether field is system-protected
        avg_latency_ms (float): Average query latency
        p95_latency_ms (float): 95th percentile latency
        first_seen (datetime.datetime): First usage timestamp
        last_seen (datetime.datetime): Most recent usage timestamp
    """

    field_name: str
    query_count: int
    unique_queries: int
    is_indexed: bool
    is_protected: bool
    avg_latency_ms: float
    p95_latency_ms: float
    first_seen: datetime.datetime
    last_seen: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_name = self.field_name

        query_count = self.query_count

        unique_queries = self.unique_queries

        is_indexed = self.is_indexed

        is_protected = self.is_protected

        avg_latency_ms = self.avg_latency_ms

        p95_latency_ms = self.p95_latency_ms

        first_seen = self.first_seen.isoformat()

        last_seen = self.last_seen.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "field_name": field_name,
                "query_count": query_count,
                "unique_queries": unique_queries,
                "is_indexed": is_indexed,
                "is_protected": is_protected,
                "avg_latency_ms": avg_latency_ms,
                "p95_latency_ms": p95_latency_ms,
                "first_seen": first_seen,
                "last_seen": last_seen,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_name = d.pop("field_name")

        query_count = d.pop("query_count")

        unique_queries = d.pop("unique_queries")

        is_indexed = d.pop("is_indexed")

        is_protected = d.pop("is_protected")

        avg_latency_ms = d.pop("avg_latency_ms")

        p95_latency_ms = d.pop("p95_latency_ms")

        first_seen = isoparse(d.pop("first_seen"))

        last_seen = isoparse(d.pop("last_seen"))

        field_usage_stat = cls(
            field_name=field_name,
            query_count=query_count,
            unique_queries=unique_queries,
            is_indexed=is_indexed,
            is_protected=is_protected,
            avg_latency_ms=avg_latency_ms,
            p95_latency_ms=p95_latency_ms,
            first_seen=first_seen,
            last_seen=last_seen,
        )

        field_usage_stat.additional_properties = d
        return field_usage_stat

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
