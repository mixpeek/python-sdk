from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.logical_operator import LogicalOperator
    from ..models.sort_option import SortOption


T = TypeVar("T", bound="ListClusterExecutionsRequest")


@_attrs_define
class ListClusterExecutionsRequest:
    """Request parameters for listing and filtering cluster execution history.

    Provides flexible querying of historical clustering executions with filtering,
    sorting, and search capabilities. Use to build execution history UIs, compare
    runs over time, and analyze clustering performance trends.

    Use Cases:
        - Display execution history table with sorting and filtering
        - Find failed executions for debugging
        - Compare metrics across successful runs
        - Search executions by date range or status
        - Build execution timeline visualization

    Query Behavior:
        - Empty request {} returns all executions sorted by created_at (newest first)
        - Filters, sort, and search can be combined for complex queries
        - Results are paginated (use page/page_size query params)

    Note:
        All fields are OPTIONAL. Omit for default behavior (all executions, newest first).

        Attributes:
            filters (LogicalOperator | None | Unset): OPTIONAL. Complex filtering conditions for execution history. NOT
                REQUIRED - omit to return all executions. Structure: Logical operator (AND/OR) with array of conditions.
                Supported filter fields:   - status: Filter by execution status (pending/processing/completed/failed).   -
                created_at: Filter by execution start date (use gte/lte for ranges).   - num_clusters: Filter by number of
                clusters found.   - metrics.silhouette_score: Filter by quality threshold. Example filters:   - Status is
                completed: {operator: 'AND', conditions: [{field: 'status', value: 'completed', operator: '=='}]}.   - Created
                in last 7 days: {operator: 'AND', conditions: [{field: 'created_at', operator: 'gte', value:
                '2025-11-06T00:00:00Z'}]}.   - Good quality (silhouette > 0.5): {operator: 'AND', conditions: [{field:
                'metrics.silhouette_score', operator: '>', value: 0.5}]}. Combine with OR: Status completed OR failed (exclude
                in-progress).
            sort (None | SortOption | Unset): OPTIONAL. Sorting configuration for results. NOT REQUIRED - defaults to
                created_at descending (newest first). Structure: {field: 'field_name', direction: 'asc' or 'desc'}. Sortable
                fields:   - created_at: Sort by execution start time (default).   - completed_at: Sort by execution finish time.
                - num_clusters: Sort by cluster count.   - num_points: Sort by document count.   - metrics.silhouette_score:
                Sort by quality score.   - status: Sort by execution status. Common use cases:   - Newest first (default):
                {field: 'created_at', direction: 'desc'}.   - Best quality first: {field: 'metrics.silhouette_score', direction:
                'desc'}.   - Failed executions first: {field: 'status', direction: 'asc'} (alphabetical).
            search (None | str | Unset): OPTIONAL. Full-text search query across execution metadata. NOT REQUIRED - omit for
                no search filtering. Searches in:   - run_id: Search by execution identifier.   - error_message: Find executions
                with specific error text.   - centroids.label: Search by cluster label names.   - centroids.summary: Search by
                cluster descriptions. Behavior:   - Case-insensitive partial matching.   - Multiple terms are AND-ed together.
                - Combines with filters for complex queries. Examples:   - 'failed' → Find executions with 'failed' in error
                messages.   - 'product review' → Find executions with clusters about products/reviews.   - 'run_abc123' → Find
                specific execution by ID.
    """

    filters: LogicalOperator | None | Unset = UNSET
    sort: None | SortOption | Unset = UNSET
    search: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.logical_operator import LogicalOperator
        from ..models.sort_option import SortOption

        filters: dict[str, Any] | None | Unset
        if isinstance(self.filters, Unset):
            filters = UNSET
        elif isinstance(self.filters, LogicalOperator):
            filters = self.filters.to_dict()
        else:
            filters = self.filters

        sort: dict[str, Any] | None | Unset
        if isinstance(self.sort, Unset):
            sort = UNSET
        elif isinstance(self.sort, SortOption):
            sort = self.sort.to_dict()
        else:
            sort = self.sort

        search: None | str | Unset
        if isinstance(self.search, Unset):
            search = UNSET
        else:
            search = self.search

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if filters is not UNSET:
            field_dict["filters"] = filters
        if sort is not UNSET:
            field_dict["sort"] = sort
        if search is not UNSET:
            field_dict["search"] = search

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.logical_operator import LogicalOperator
        from ..models.sort_option import SortOption

        d = dict(src_dict)

        def _parse_filters(data: object) -> LogicalOperator | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                filters_type_0 = LogicalOperator.from_dict(data)

                return filters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LogicalOperator | None | Unset, data)

        filters = _parse_filters(d.pop("filters", UNSET))

        def _parse_sort(data: object) -> None | SortOption | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                sort_type_0 = SortOption.from_dict(data)

                return sort_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SortOption | Unset, data)

        sort = _parse_sort(d.pop("sort", UNSET))

        def _parse_search(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        search = _parse_search(d.pop("search", UNSET))

        list_cluster_executions_request = cls(
            filters=filters,
            sort=sort,
            search=search,
        )

        list_cluster_executions_request.additional_properties = d
        return list_cluster_executions_request

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
