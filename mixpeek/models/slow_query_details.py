from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SlowQueryDetails")


@_attrs_define
class SlowQueryDetails:
    """Details of a slow query.

    Attributes:
        retriever_id (str): Retriever that executed the query
        query (str): Query input string
        latency_ms (float): Query latency in milliseconds
        results_count (int): Number of results returned
        queried_fields (list[str]): List of metadata fields queried
    """

    retriever_id: str
    query: str
    latency_ms: float
    results_count: int
    queried_fields: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        retriever_id = self.retriever_id

        query = self.query

        latency_ms = self.latency_ms

        results_count = self.results_count

        queried_fields = self.queried_fields

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "retriever_id": retriever_id,
                "query": query,
                "latency_ms": latency_ms,
                "results_count": results_count,
                "queried_fields": queried_fields,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        retriever_id = d.pop("retriever_id")

        query = d.pop("query")

        latency_ms = d.pop("latency_ms")

        results_count = d.pop("results_count")

        queried_fields = cast(list[str], d.pop("queried_fields"))

        slow_query_details = cls(
            retriever_id=retriever_id,
            query=query,
            latency_ms=latency_ms,
            results_count=results_count,
            queried_fields=queried_fields,
        )

        slow_query_details.additional_properties = d
        return slow_query_details

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
