from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.object_list_stats import ObjectListStats
    from ..models.object_response import ObjectResponse
    from ..models.pagination_response import PaginationResponse


T = TypeVar("T", bound="ListObjectsResponse")


@_attrs_define
class ListObjectsResponse:
    """Response model for listing objects in a bucket.

    Attributes:
        results (list[ObjectResponse]): List of objects matching the query
        pagination (PaginationResponse): PaginationResponse.

            Cursor-based pagination response:
            - Use next_cursor for navigation
            - Total count fields only populated when include_total=true
        stats (None | ObjectListStats | Unset): Aggregate statistics across all objects in the result
    """

    results: list[ObjectResponse]
    pagination: PaginationResponse
    stats: None | ObjectListStats | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.object_list_stats import ObjectListStats

        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        pagination = self.pagination.to_dict()

        stats: dict[str, Any] | None | Unset
        if isinstance(self.stats, Unset):
            stats = UNSET
        elif isinstance(self.stats, ObjectListStats):
            stats = self.stats.to_dict()
        else:
            stats = self.stats

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "results": results,
                "pagination": pagination,
            }
        )
        if stats is not UNSET:
            field_dict["stats"] = stats

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.object_list_stats import ObjectListStats
        from ..models.object_response import ObjectResponse
        from ..models.pagination_response import PaginationResponse

        d = dict(src_dict)
        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = ObjectResponse.from_dict(results_item_data)

            results.append(results_item)

        pagination = PaginationResponse.from_dict(d.pop("pagination"))

        def _parse_stats(data: object) -> None | ObjectListStats | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                stats_type_0 = ObjectListStats.from_dict(data)

                return stats_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ObjectListStats | Unset, data)

        stats = _parse_stats(d.pop("stats", UNSET))

        list_objects_response = cls(
            results=results,
            pagination=pagination,
            stats=stats,
        )

        list_objects_response.additional_properties = d
        return list_objects_response

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
