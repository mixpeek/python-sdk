from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClusterExecutionMetrics")


@_attrs_define
class ClusterExecutionMetrics:
    """Quality metrics for evaluating clustering execution performance.

    Provides statistical measures to assess the quality of the clustering results.
    Higher quality clusters have better cohesion (documents within clusters are similar)
    and separation (clusters are distinct from each other).

    Use Cases:
        - Compare quality across multiple clustering executions
        - Determine optimal number of clusters for a dataset
        - Validate clustering algorithm performance
        - Track clustering quality over time
        - Debug clustering issues (poor metrics indicate problems)

    Interpretation:
        - Use silhouette_score as primary quality indicator (0.5+ = good, 0.7+ = excellent)
        - Lower davies_bouldin_index indicates better-separated clusters
        - Higher calinski_harabasz_score indicates denser, better-separated clusters

    Note:
        All metrics are OPTIONAL and only present if clustering completed successfully.
        Failed executions return null for all metrics.

        Attributes:
            silhouette_score (float | None | Unset): OPTIONAL. Silhouette score measuring cluster cohesion and separation.
                Range: -1 to +1. Interpretation:   +1.0 = Perfect clustering (documents far from other clusters, close to own
                cluster).   0.0 = Overlapping clusters (documents on cluster boundaries).   -1.0 = Poor clustering (documents
                assigned to wrong clusters). Practical thresholds:   0.7 to 1.0 = Excellent clustering.   0.5 to 0.7 = Good
                clustering.   0.25 to 0.5 = Weak clustering, consider different parameters.   Below 0.25 = Poor clustering,
                reconfigure or more data needed. null = metric not calculated (too few points or clustering failed).
            davies_bouldin_index (float | None | Unset): OPTIONAL. Davies-Bouldin index measuring cluster separation. Range:
                0 to +∞ (lower is better, no upper bound). Interpretation:   0.0 = Perfect separation (impossible in practice).
                0.0 to 1.0 = Excellent separation.   1.0 to 2.0 = Good separation.   Above 2.0 = Poor separation, clusters
                overlap. Formula: Average ratio of intra-cluster to inter-cluster distances. Use when: Validating that clusters
                are distinct and well-separated. null = metric not calculated (too few points or clustering failed).
            calinski_harabasz_score (float | None | Unset): OPTIONAL. Calinski-Harabasz score (also called Variance Ratio
                Criterion). Range: 0 to +∞ (higher is better, no strict upper bound). Interpretation:   Higher values indicate
                denser, more compact clusters.   No universal threshold - compare relative values across runs.   Typical good
                values: 100-1000+ (dataset dependent). Formula: Ratio of between-cluster to within-cluster dispersion. Use when:
                Comparing different numbers of clusters for the same dataset. Note: Biased toward algorithms that produce
                spherical, equally-sized clusters. null = metric not calculated (too few points or clustering failed).
    """

    silhouette_score: float | None | Unset = UNSET
    davies_bouldin_index: float | None | Unset = UNSET
    calinski_harabasz_score: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        silhouette_score: float | None | Unset
        if isinstance(self.silhouette_score, Unset):
            silhouette_score = UNSET
        else:
            silhouette_score = self.silhouette_score

        davies_bouldin_index: float | None | Unset
        if isinstance(self.davies_bouldin_index, Unset):
            davies_bouldin_index = UNSET
        else:
            davies_bouldin_index = self.davies_bouldin_index

        calinski_harabasz_score: float | None | Unset
        if isinstance(self.calinski_harabasz_score, Unset):
            calinski_harabasz_score = UNSET
        else:
            calinski_harabasz_score = self.calinski_harabasz_score

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if silhouette_score is not UNSET:
            field_dict["silhouette_score"] = silhouette_score
        if davies_bouldin_index is not UNSET:
            field_dict["davies_bouldin_index"] = davies_bouldin_index
        if calinski_harabasz_score is not UNSET:
            field_dict["calinski_harabasz_score"] = calinski_harabasz_score

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_silhouette_score(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        silhouette_score = _parse_silhouette_score(d.pop("silhouette_score", UNSET))

        def _parse_davies_bouldin_index(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        davies_bouldin_index = _parse_davies_bouldin_index(d.pop("davies_bouldin_index", UNSET))

        def _parse_calinski_harabasz_score(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        calinski_harabasz_score = _parse_calinski_harabasz_score(d.pop("calinski_harabasz_score", UNSET))

        cluster_execution_metrics = cls(
            silhouette_score=silhouette_score,
            davies_bouldin_index=davies_bouldin_index,
            calinski_harabasz_score=calinski_harabasz_score,
        )

        cluster_execution_metrics.additional_properties = d
        return cluster_execution_metrics

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
