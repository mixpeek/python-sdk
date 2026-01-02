from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cluster_execution_list_stats import ClusterExecutionListStats
    from ..models.cluster_execution_result import ClusterExecutionResult
    from ..models.pagination_response import PaginationResponse


T = TypeVar("T", bound="ListClusterExecutionsResponse")


@_attrs_define
class ListClusterExecutionsResponse:
    """Complete response for cluster execution history listing endpoint.

    Returns paginated execution history with filtering, sorting, and aggregate statistics.
    Use to build execution history UIs, monitoring dashboards, and performance analytics.

    Response Structure:
        - results: Array of execution details (paginated)
        - pagination: Page navigation info (current page, total pages, etc.)
        - total_count: Total matching executions (across all pages)
        - stats: Aggregated metrics for current result set

    Use Cases:
        - Build execution history table with pagination
        - Display execution status dashboard with charts
        - Monitor clustering performance trends
        - Debug failed executions
        - Compare quality metrics across runs

    Pagination Behavior:
        - Default: 10 executions per page
        - Use query params: ?page=1&page_size=20
        - results contains current page only
        - total_count shows all matching executions
        - pagination provides navigation links

    Example Workflow:
        1. Request: POST /clusters/{id}/executions/list with filters
        2. Response: 50 total executions, showing page 1 (10 results)
        3. Display: Show 10 results + "Page 1 of 5" + aggregate stats
        4. Navigate: Use pagination.next_page for next 10 results

        Attributes:
            results (list[ClusterExecutionResult]): REQUIRED. Array of cluster execution results for the current page.
                Length: 0 to page_size (default 10, max typically 100). Empty array [] if:   - No executions exist for this
                cluster.   - Filters matched no results.   - Requested page beyond available pages. Sorted by: created_at
                descending (newest first) by default. Override with sort parameter in request. Each item contains:   - run_id:
                Unique execution identifier.   - status: pending/processing/completed/failed.   - num_clusters: Clusters found.
                - metrics: Quality scores (if available).   - centroids: Cluster labels and summaries (if available).   -
                created_at/completed_at: Timestamps.   - error_message: Error details (if failed). Use for: Rendering execution
                history table rows.
            pagination (PaginationResponse): PaginationResponse.

                Cursor-based pagination response:
                - Use next_cursor for navigation
                - Total count fields only populated when include_total=true
            total_count (int): REQUIRED. Total number of executions matching the query across ALL pages. Use for:   -
                Display total count ('Found 127 executions').   - Calculate pagination ('Showing 1-10 of 127').   - Validate
                filters (0 = no matches, refine query). Behavior:   - Includes all filtered results, not just current page.   -
                Changes when filters are applied.   - Equals len(results) only if all results fit on one page. Example:   -
                Query returns 127 executions total.   - Page size = 10.   - Current page (1) shows results[0:10].   -
                total_count = 127 (not 10).
            stats (ClusterExecutionListStats | None | Unset): OPTIONAL. Aggregate statistics for executions in current
                result set. NOT REQUIRED - may be null if stats calculation disabled. Typically always provided for execution
                listing. Contains:   - total_executions: Count in current page.   - executions_by_status: Status distribution
                {'completed': 45, 'failed': 3}.   - avg_execution_time_ms: Mean duration.   - total_documents_clustered: Sum of
                all processed documents.   - avg_num_clusters: Mean clusters per execution. Use for:   - Summary cards above
                table.   - Status pie chart.   - Performance metrics dashboard. Note:   - Stats calculated for current page only
                (or all if no pagination).   - Respects filters (stats for filtered subset).
    """

    results: list[ClusterExecutionResult]
    pagination: PaginationResponse
    total_count: int
    stats: ClusterExecutionListStats | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.cluster_execution_list_stats import ClusterExecutionListStats

        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        pagination = self.pagination.to_dict()

        total_count = self.total_count

        stats: dict[str, Any] | None | Unset
        if isinstance(self.stats, Unset):
            stats = UNSET
        elif isinstance(self.stats, ClusterExecutionListStats):
            stats = self.stats.to_dict()
        else:
            stats = self.stats

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "results": results,
                "pagination": pagination,
                "total_count": total_count,
            }
        )
        if stats is not UNSET:
            field_dict["stats"] = stats

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cluster_execution_list_stats import ClusterExecutionListStats
        from ..models.cluster_execution_result import ClusterExecutionResult
        from ..models.pagination_response import PaginationResponse

        d = dict(src_dict)
        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = ClusterExecutionResult.from_dict(results_item_data)

            results.append(results_item)

        pagination = PaginationResponse.from_dict(d.pop("pagination"))

        total_count = d.pop("total_count")

        def _parse_stats(data: object) -> ClusterExecutionListStats | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                stats_type_0 = ClusterExecutionListStats.from_dict(data)

                return stats_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ClusterExecutionListStats | None | Unset, data)

        stats = _parse_stats(d.pop("stats", UNSET))

        list_cluster_executions_response = cls(
            results=results,
            pagination=pagination,
            total_count=total_count,
            stats=stats,
        )

        list_cluster_executions_response.additional_properties = d
        return list_cluster_executions_response

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
