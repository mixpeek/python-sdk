from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cluster_execution_list_stats_executions_by_status import ClusterExecutionListStatsExecutionsByStatus


T = TypeVar("T", bound="ClusterExecutionListStats")


@_attrs_define
class ClusterExecutionListStats:
    """Aggregate statistics calculated across all executions in the current result set.

    Provides summary metrics for the filtered/searched execution history, useful for
    dashboards, monitoring, and trend analysis. Statistics are calculated only for
    the executions returned in the current query (respects filters and pagination).

    Use Cases:
        - Display execution summary cards ("5 completed, 2 failed, 3 pending")
        - Show average execution time trend
        - Monitor clustering performance over time
        - Build execution health dashboard
        - Compare stats across different time periods (via filters)

    Important:
        Stats reflect only the current result set, not all historical executions.
        Apply filters to calculate stats for specific time ranges or statuses.

        Attributes:
            total_executions (int | Unset): OPTIONAL (always provided). Total number of executions in current result set.
                Equals length of results array. Use for:   - Display total count in UI ('Showing 10 of 100 executions').   -
                Validate pagination (total should match page_size × pages).   - Check if filters returned any results (0 = no
                matches). Note: This is the count in the current page, not all executions. Default: 0.
            executions_by_status (ClusterExecutionListStatsExecutionsByStatus | Unset): OPTIONAL (always provided). Count of
                executions grouped by status. Keys: 'pending', 'processing', 'completed', 'failed'. Values: Number of executions
                in each status. Use for:   - Status distribution chart (pie/bar chart).   - Health monitoring (high failed count
                = problem).   - Progress tracking (pending + processing = in-flight jobs). Example: {'completed': 45, 'failed':
                3, 'processing': 2, 'pending': 0}. Empty dict {} if no executions in result set.
            avg_execution_time_ms (float | Unset): OPTIONAL (always provided). Average execution duration in milliseconds.
                Calculated as: mean(completed_at - created_at) for completed/failed executions. Excludes pending/processing
                executions (no completed_at yet). Use for:   - Performance monitoring ('Average: 5.2 seconds').   - Trend
                analysis (is clustering getting slower over time?).   - Capacity planning (estimate time for future runs). 0.0
                if: No completed/failed executions in result set. Typical values:   - Small datasets (< 100 docs): 1000-5000ms
                (1-5 seconds).   - Medium datasets (100-1000 docs): 5000-30000ms (5-30 seconds).   - Large datasets (1000+
                docs): 30000-300000ms (30 seconds - 5 minutes). Default: 0.0.
            total_documents_clustered (int | Unset): OPTIONAL (always provided). Total documents processed across all
                executions. Calculated as: sum(num_points) for all executions in result set. Use for:   - Volume tracking
                ('Processed 10,000 documents').   - Cost estimation (larger datasets = more compute).   - Data growth monitoring
                (compare over time). 0 if: No executions in result set. Note: Same document may be counted multiple times if re-
                clustered. Default: 0.
            avg_num_clusters (float | Unset): OPTIONAL (always provided). Average number of clusters found per execution.
                Calculated as: mean(num_clusters) for all executions in result set. Use for:   - Clustering consistency check
                (stable avg = consistent results).   - Algorithm tuning (avg too high/low may need parameter adjustment).   -
                Trend analysis (is clustering finding more/fewer clusters over time?). 0.0 if: No executions in result set.
                Typical values:   - Under-clustering: < 3 clusters (data may be too diverse).   - Good clustering: 3-20 clusters
                (manageable, meaningful groups).   - Over-clustering: > 20 clusters (too granular, hard to interpret). Default:
                0.0.
    """

    total_executions: int | Unset = 0
    executions_by_status: ClusterExecutionListStatsExecutionsByStatus | Unset = UNSET
    avg_execution_time_ms: float | Unset = 0.0
    total_documents_clustered: int | Unset = 0
    avg_num_clusters: float | Unset = 0.0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_executions = self.total_executions

        executions_by_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.executions_by_status, Unset):
            executions_by_status = self.executions_by_status.to_dict()

        avg_execution_time_ms = self.avg_execution_time_ms

        total_documents_clustered = self.total_documents_clustered

        avg_num_clusters = self.avg_num_clusters

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_executions is not UNSET:
            field_dict["total_executions"] = total_executions
        if executions_by_status is not UNSET:
            field_dict["executions_by_status"] = executions_by_status
        if avg_execution_time_ms is not UNSET:
            field_dict["avg_execution_time_ms"] = avg_execution_time_ms
        if total_documents_clustered is not UNSET:
            field_dict["total_documents_clustered"] = total_documents_clustered
        if avg_num_clusters is not UNSET:
            field_dict["avg_num_clusters"] = avg_num_clusters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cluster_execution_list_stats_executions_by_status import (
            ClusterExecutionListStatsExecutionsByStatus,
        )

        d = dict(src_dict)
        total_executions = d.pop("total_executions", UNSET)

        _executions_by_status = d.pop("executions_by_status", UNSET)
        executions_by_status: ClusterExecutionListStatsExecutionsByStatus | Unset
        if isinstance(_executions_by_status, Unset):
            executions_by_status = UNSET
        else:
            executions_by_status = ClusterExecutionListStatsExecutionsByStatus.from_dict(_executions_by_status)

        avg_execution_time_ms = d.pop("avg_execution_time_ms", UNSET)

        total_documents_clustered = d.pop("total_documents_clustered", UNSET)

        avg_num_clusters = d.pop("avg_num_clusters", UNSET)

        cluster_execution_list_stats = cls(
            total_executions=total_executions,
            executions_by_status=executions_by_status,
            avg_execution_time_ms=avg_execution_time_ms,
            total_documents_clustered=total_documents_clustered,
            avg_num_clusters=avg_num_clusters,
        )

        cluster_execution_list_stats.additional_properties = d
        return cluster_execution_list_stats

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
