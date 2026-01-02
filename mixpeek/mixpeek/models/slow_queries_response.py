from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.slow_query_details import SlowQueryDetails


T = TypeVar("T", bound="SlowQueriesResponse")


@_attrs_define
class SlowQueriesResponse:
    """Response for slow queries endpoint.

    Attributes:
        namespace_id (str): Namespace ID analyzed
        time_range_days (int): Number of days analyzed
        latency_threshold_ms (float): Latency threshold used
        slow_queries (list[SlowQueryDetails]): Slow query details
        total_slow_queries (int): Total slow queries found
    """

    namespace_id: str
    time_range_days: int
    latency_threshold_ms: float
    slow_queries: list[SlowQueryDetails]
    total_slow_queries: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        namespace_id = self.namespace_id

        time_range_days = self.time_range_days

        latency_threshold_ms = self.latency_threshold_ms

        slow_queries = []
        for slow_queries_item_data in self.slow_queries:
            slow_queries_item = slow_queries_item_data.to_dict()
            slow_queries.append(slow_queries_item)

        total_slow_queries = self.total_slow_queries

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "namespace_id": namespace_id,
                "time_range_days": time_range_days,
                "latency_threshold_ms": latency_threshold_ms,
                "slow_queries": slow_queries,
                "total_slow_queries": total_slow_queries,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.slow_query_details import SlowQueryDetails

        d = dict(src_dict)
        namespace_id = d.pop("namespace_id")

        time_range_days = d.pop("time_range_days")

        latency_threshold_ms = d.pop("latency_threshold_ms")

        slow_queries = []
        _slow_queries = d.pop("slow_queries")
        for slow_queries_item_data in _slow_queries:
            slow_queries_item = SlowQueryDetails.from_dict(slow_queries_item_data)

            slow_queries.append(slow_queries_item)

        total_slow_queries = d.pop("total_slow_queries")

        slow_queries_response = cls(
            namespace_id=namespace_id,
            time_range_days=time_range_days,
            latency_threshold_ms=latency_threshold_ms,
            slow_queries=slow_queries,
            total_slow_queries=total_slow_queries,
        )

        slow_queries_response.additional_properties = d
        return slow_queries_response

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
