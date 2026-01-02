from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.aggregation_result import AggregationResult
    from ..models.object_aggregation_response_query_info import ObjectAggregationResponseQueryInfo


T = TypeVar("T", bound="ObjectAggregationResponse")


@_attrs_define
class ObjectAggregationResponse:
    """Response containing object aggregation results.

    Returns aggregated statistics grouped by specified fields.

        Attributes:
            results (list[AggregationResult]): List of aggregation results, one per group.
            total_groups (int): Total number of unique groups returned.
            query_info (ObjectAggregationResponseQueryInfo | Unset): Additional information about the query execution. May
                include pipeline stages, execution time, etc.
    """

    results: list[AggregationResult]
    total_groups: int
    query_info: ObjectAggregationResponseQueryInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        total_groups = self.total_groups

        query_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.query_info, Unset):
            query_info = self.query_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "results": results,
                "total_groups": total_groups,
            }
        )
        if query_info is not UNSET:
            field_dict["query_info"] = query_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.aggregation_result import AggregationResult
        from ..models.object_aggregation_response_query_info import ObjectAggregationResponseQueryInfo

        d = dict(src_dict)
        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = AggregationResult.from_dict(results_item_data)

            results.append(results_item)

        total_groups = d.pop("total_groups")

        _query_info = d.pop("query_info", UNSET)
        query_info: ObjectAggregationResponseQueryInfo | Unset
        if isinstance(_query_info, Unset):
            query_info = UNSET
        else:
            query_info = ObjectAggregationResponseQueryInfo.from_dict(_query_info)

        object_aggregation_response = cls(
            results=results,
            total_groups=total_groups,
            query_info=query_info,
        )

        object_aggregation_response.additional_properties = d
        return object_aggregation_response

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
