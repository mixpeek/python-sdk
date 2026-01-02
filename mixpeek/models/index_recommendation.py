from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="IndexRecommendation")


@_attrs_define
class IndexRecommendation:
    """MongoDB index recommendation.

    Attributes:
        field_name (str): Field to index
        query_count (int): Number of queries using this field
        avg_latency_ms (float): Average latency
        p95_latency_ms (float): 95th percentile latency
        slow_query_count (int): Queries slower than 500ms
        very_slow_query_count (int): Queries slower than 1000ms
        priority_score (float): Priority score for indexing
        recommendation (str): Human-readable recommendation level
        mongodb_index_command (str): Ready-to-use MongoDB index command
    """

    field_name: str
    query_count: int
    avg_latency_ms: float
    p95_latency_ms: float
    slow_query_count: int
    very_slow_query_count: int
    priority_score: float
    recommendation: str
    mongodb_index_command: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_name = self.field_name

        query_count = self.query_count

        avg_latency_ms = self.avg_latency_ms

        p95_latency_ms = self.p95_latency_ms

        slow_query_count = self.slow_query_count

        very_slow_query_count = self.very_slow_query_count

        priority_score = self.priority_score

        recommendation = self.recommendation

        mongodb_index_command = self.mongodb_index_command

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "field_name": field_name,
                "query_count": query_count,
                "avg_latency_ms": avg_latency_ms,
                "p95_latency_ms": p95_latency_ms,
                "slow_query_count": slow_query_count,
                "very_slow_query_count": very_slow_query_count,
                "priority_score": priority_score,
                "recommendation": recommendation,
                "mongodb_index_command": mongodb_index_command,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_name = d.pop("field_name")

        query_count = d.pop("query_count")

        avg_latency_ms = d.pop("avg_latency_ms")

        p95_latency_ms = d.pop("p95_latency_ms")

        slow_query_count = d.pop("slow_query_count")

        very_slow_query_count = d.pop("very_slow_query_count")

        priority_score = d.pop("priority_score")

        recommendation = d.pop("recommendation")

        mongodb_index_command = d.pop("mongodb_index_command")

        index_recommendation = cls(
            field_name=field_name,
            query_count=query_count,
            avg_latency_ms=avg_latency_ms,
            p95_latency_ms=p95_latency_ms,
            slow_query_count=slow_query_count,
            very_slow_query_count=very_slow_query_count,
            priority_score=priority_score,
            recommendation=recommendation,
            mongodb_index_command=mongodb_index_command,
        )

        index_recommendation.additional_properties = d
        return index_recommendation

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
