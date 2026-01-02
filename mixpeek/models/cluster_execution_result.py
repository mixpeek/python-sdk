from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.cluster_execution_result_status import ClusterExecutionResultStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cluster_execution_centroid import ClusterExecutionCentroid
    from ..models.cluster_execution_metrics import ClusterExecutionMetrics


T = TypeVar("T", bound="ClusterExecutionResult")


@_attrs_define
class ClusterExecutionResult:
    """Complete results from a single clustering execution.

    Represents the outcome of running a clustering algorithm on a collection's documents.
    Each execution creates a snapshot of clustering results at a point in time, including
    the clusters found, quality metrics, and semantic labels.

    Use Cases:
        - Display clustering execution history in UI
        - Compare clustering quality across multiple runs
        - Track execution status for long-running jobs
        - Debug failed clustering attempts
        - View cluster summaries and labels for analysis

    Workflow:
        1. Create cluster configuration → POST /clusters
        2. Execute clustering → POST /clusters/{id}/execute
        3. Poll execution status → GET /clusters/{id}/executions
        4. View execution history → POST /clusters/{id}/executions/list

    Status Lifecycle:
        pending → processing → completed (or failed)

    Note:
        Execution results are immutable once completed. Re-running clustering
        creates a new execution result with a new run_id.

        Attributes:
            run_id (str): REQUIRED. Unique identifier for this specific clustering execution. Format: 'run_' prefix followed
                by random alphanumeric string. Used to retrieve specific execution artifacts and results. Each re-execution of
                the same cluster creates a new run_id. References execution artifacts in S3 and MongoDB.
            cluster_id (str): REQUIRED. Parent cluster configuration that was executed. Format: 'clust_' prefix followed by
                random alphanumeric string. Links this execution back to the cluster definition. Multiple executions can share
                the same cluster_id.
            status (ClusterExecutionResultStatus): REQUIRED. Current status of the clustering execution. Values:   'pending'
                = Job queued, waiting to start.   'processing' = Clustering algorithm running (may take minutes for large
                datasets).   'completed' = Clustering finished successfully, results available.   'failed' = Clustering failed,
                check error_message for details. Status changes: pending → processing → (completed OR failed). Poll this field
                to track job progress.
            num_clusters (int): REQUIRED. Number of clusters found by the clustering algorithm. Range: 1 to num_points
                (though typically much lower). Interpretation:   Too few clusters = overgeneralization, may need lower
                n_clusters param.   Too many clusters = overfitting, may need higher n_clusters param.   Optimal value depends
                on dataset and use case. Available immediately upon completion, even if metrics fail.
            num_points (int): REQUIRED. Total number of documents/points that were clustered. Equals the count of documents
                in the collection at execution time. Note: This may differ across executions if documents were added/removed.
                Used to calculate metrics and validate clustering quality. Minimum 2 points required for clustering (1 cluster
                per point otherwise).
            created_at (datetime.datetime): REQUIRED. Timestamp when the clustering execution started. ISO 8601 format with
                timezone (UTC). Used to:   - Sort executions chronologically.   - Calculate execution duration (completed_at -
                created_at).   - Filter execution history by date range. Always present, even for failed executions.
            metrics (ClusterExecutionMetrics | None | Unset): OPTIONAL. Quality metrics evaluating clustering performance.
                NOT REQUIRED - only present for successful executions. null if:   - Execution is still pending/processing.   -
                Execution failed.   - Too few points to calculate metrics (need 2+ points). Contains silhouette_score,
                davies_bouldin_index, calinski_harabasz_score. Use to compare quality across multiple executions.
            centroids (list[ClusterExecutionCentroid] | None | Unset): OPTIONAL. List of cluster centroids with semantic
                labels. NOT REQUIRED - only present for completed executions with LLM labeling enabled. Length: equals
                num_clusters. Each centroid contains:   - cluster_id: Identifier for the cluster (e.g., 'cl_0').   -
                num_members: Count of documents in this cluster.   - label: Human-readable cluster name (e.g., 'Product
                Reviews').   - summary: Brief description of cluster content.   - keywords: Array of representative terms. null
                if:   - Execution pending/processing/failed.   - LLM labeling not configured. Use for: Displaying cluster
                summaries in UI, filtering by cluster.
            completed_at (datetime.datetime | None | Unset): OPTIONAL. Timestamp when the clustering execution finished. ISO
                8601 format with timezone (UTC). NOT REQUIRED - only present for completed or failed executions. null if: status
                is 'pending' or 'processing'. Use to:   - Calculate execution duration (completed_at - created_at).   - Show
                when results became available. Present for both successful and failed executions.
            error_message (None | str | Unset): OPTIONAL. Error message if the clustering execution failed. NOT REQUIRED -
                only present when status is 'failed'. null if: execution succeeded or is still in progress. Contains:   - Human-
                readable error description.   - Possible causes and suggested fixes.   - Stack trace details (for debugging).
                Common errors:   - 'Insufficient documents for clustering' (need 2+ docs).   - 'Feature extractor not found'
                (invalid collection config).   - 'Out of memory' (dataset too large for algorithm). Use for: Debugging failed
                executions and user error messages.
            llm_labeling_errors (list[str] | None | Unset): OPTIONAL. List of errors encountered during LLM labeling. NOT
                REQUIRED - only present when LLM labeling was attempted and encountered errors. null if:   - LLM labeling was
                not enabled.   - LLM labeling succeeded for all clusters.   - Execution is still in progress. Each error is a
                JSON string containing:   - 'error': Human-readable error message.   - 'clusters': List of cluster IDs affected
                by this error. Common errors:   - 'LLM API timeout for 2 clusters' (network/API issues).   - 'OpenAI rate limit
                exceeded' (quota exhausted).   - 'Invalid model name: gpt-3.5' (config error).   - 'No representative documents
                for cluster cl_3' (empty cluster). Use for:   - Debugging why some clusters have fallback labels.   -
                Identifying LLM API issues without failing entire clustering.   - Warning users about partial labeling success.
    """

    run_id: str
    cluster_id: str
    status: ClusterExecutionResultStatus
    num_clusters: int
    num_points: int
    created_at: datetime.datetime
    metrics: ClusterExecutionMetrics | None | Unset = UNSET
    centroids: list[ClusterExecutionCentroid] | None | Unset = UNSET
    completed_at: datetime.datetime | None | Unset = UNSET
    error_message: None | str | Unset = UNSET
    llm_labeling_errors: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.cluster_execution_metrics import ClusterExecutionMetrics

        run_id = self.run_id

        cluster_id = self.cluster_id

        status = self.status.value

        num_clusters = self.num_clusters

        num_points = self.num_points

        created_at = self.created_at.isoformat()

        metrics: dict[str, Any] | None | Unset
        if isinstance(self.metrics, Unset):
            metrics = UNSET
        elif isinstance(self.metrics, ClusterExecutionMetrics):
            metrics = self.metrics.to_dict()
        else:
            metrics = self.metrics

        centroids: list[dict[str, Any]] | None | Unset
        if isinstance(self.centroids, Unset):
            centroids = UNSET
        elif isinstance(self.centroids, list):
            centroids = []
            for centroids_type_0_item_data in self.centroids:
                centroids_type_0_item = centroids_type_0_item_data.to_dict()
                centroids.append(centroids_type_0_item)

        else:
            centroids = self.centroids

        completed_at: None | str | Unset
        if isinstance(self.completed_at, Unset):
            completed_at = UNSET
        elif isinstance(self.completed_at, datetime.datetime):
            completed_at = self.completed_at.isoformat()
        else:
            completed_at = self.completed_at

        error_message: None | str | Unset
        if isinstance(self.error_message, Unset):
            error_message = UNSET
        else:
            error_message = self.error_message

        llm_labeling_errors: list[str] | None | Unset
        if isinstance(self.llm_labeling_errors, Unset):
            llm_labeling_errors = UNSET
        elif isinstance(self.llm_labeling_errors, list):
            llm_labeling_errors = self.llm_labeling_errors

        else:
            llm_labeling_errors = self.llm_labeling_errors

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "run_id": run_id,
                "cluster_id": cluster_id,
                "status": status,
                "num_clusters": num_clusters,
                "num_points": num_points,
                "created_at": created_at,
            }
        )
        if metrics is not UNSET:
            field_dict["metrics"] = metrics
        if centroids is not UNSET:
            field_dict["centroids"] = centroids
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if error_message is not UNSET:
            field_dict["error_message"] = error_message
        if llm_labeling_errors is not UNSET:
            field_dict["llm_labeling_errors"] = llm_labeling_errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cluster_execution_centroid import ClusterExecutionCentroid
        from ..models.cluster_execution_metrics import ClusterExecutionMetrics

        d = dict(src_dict)
        run_id = d.pop("run_id")

        cluster_id = d.pop("cluster_id")

        status = ClusterExecutionResultStatus(d.pop("status"))

        num_clusters = d.pop("num_clusters")

        num_points = d.pop("num_points")

        created_at = isoparse(d.pop("created_at"))

        def _parse_metrics(data: object) -> ClusterExecutionMetrics | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metrics_type_0 = ClusterExecutionMetrics.from_dict(data)

                return metrics_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ClusterExecutionMetrics | None | Unset, data)

        metrics = _parse_metrics(d.pop("metrics", UNSET))

        def _parse_centroids(data: object) -> list[ClusterExecutionCentroid] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                centroids_type_0 = []
                _centroids_type_0 = data
                for centroids_type_0_item_data in _centroids_type_0:
                    centroids_type_0_item = ClusterExecutionCentroid.from_dict(centroids_type_0_item_data)

                    centroids_type_0.append(centroids_type_0_item)

                return centroids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ClusterExecutionCentroid] | None | Unset, data)

        centroids = _parse_centroids(d.pop("centroids", UNSET))

        def _parse_completed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completed_at_type_0 = isoparse(data)

                return completed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        completed_at = _parse_completed_at(d.pop("completed_at", UNSET))

        def _parse_error_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_message = _parse_error_message(d.pop("error_message", UNSET))

        def _parse_llm_labeling_errors(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                llm_labeling_errors_type_0 = cast(list[str], data)

                return llm_labeling_errors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        llm_labeling_errors = _parse_llm_labeling_errors(d.pop("llm_labeling_errors", UNSET))

        cluster_execution_result = cls(
            run_id=run_id,
            cluster_id=cluster_id,
            status=status,
            num_clusters=num_clusters,
            num_points=num_points,
            created_at=created_at,
            metrics=metrics,
            centroids=centroids,
            completed_at=completed_at,
            error_message=error_message,
            llm_labeling_errors=llm_labeling_errors,
        )

        cluster_execution_result.additional_properties = d
        return cluster_execution_result

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
