from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.search_result_item import SearchResultItem


T = TypeVar("T", bound="SearchResponse")


@_attrs_define
class SearchResponse:
    """Response model for resource search results.

    Contains paginated search results with metadata about total matches
    and pagination state. Results are sorted by relevance (exact matches first,
    then partial matches) and creation time (newest first).

    Use Cases:
        - Display search results to users
        - Implement pagination UI
        - Show total result counts
        - Navigate through large result sets

    Fields:
        - results: List of matched resources
        - total: Total number of matches (before pagination)
        - limit: Results per page (from request)
        - offset: Current pagination offset (from request)

        Attributes:
            results (list[SearchResultItem]): List of matched resources. REQUIRED. May be empty if no matches found. Sorted
                by: 1) Exact matches first, 2) Partial matches, 3) Created timestamp descending. Length is min(total - offset,
                limit). Each result contains full resource metadata for display.
            total (int): Total number of matches across all pages. REQUIRED. Count before pagination is applied. Use to
                calculate total pages: ceil(total / limit). May be 0 if no matches found. Example: total=50 with limit=20 means
                3 pages of results.
            limit (int): Results per page (from request). REQUIRED. Echo of the limit parameter from the request. Range:
                1-100.
            offset (int): Current pagination offset (from request). REQUIRED. Echo of the offset parameter from the request.
                Number of results skipped. Example: offset=20 means results start from the 21st match.
    """

    results: list[SearchResultItem]
    total: int
    limit: int
    offset: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        total = self.total

        limit = self.limit

        offset = self.offset

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "results": results,
                "total": total,
                "limit": limit,
                "offset": offset,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_result_item import SearchResultItem

        d = dict(src_dict)
        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = SearchResultItem.from_dict(results_item_data)

            results.append(results_item)

        total = d.pop("total")

        limit = d.pop("limit")

        offset = d.pop("offset")

        search_response = cls(
            results=results,
            total=total,
            limit=limit,
            offset=offset,
        )

        search_response.additional_properties = d
        return search_response

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
