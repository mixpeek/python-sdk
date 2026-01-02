from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cluster_list_stats_clusters_by_status import ClusterListStatsClustersByStatus


T = TypeVar("T", bound="ClusterListStats")


@_attrs_define
class ClusterListStats:
    """Aggregate statistics for a list of clusters.

    Attributes:
        total_clusters (int | Unset): Total number of clusters in the result Default: 0.
        total_documents (int | Unset): Total number of documents across all clusters Default: 0.
        avg_documents_per_cluster (float | Unset): Average number of documents per cluster Default: 0.0.
        clusters_by_status (ClusterListStatsClustersByStatus | Unset): Count of clusters grouped by status
    """

    total_clusters: int | Unset = 0
    total_documents: int | Unset = 0
    avg_documents_per_cluster: float | Unset = 0.0
    clusters_by_status: ClusterListStatsClustersByStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_clusters = self.total_clusters

        total_documents = self.total_documents

        avg_documents_per_cluster = self.avg_documents_per_cluster

        clusters_by_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.clusters_by_status, Unset):
            clusters_by_status = self.clusters_by_status.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_clusters is not UNSET:
            field_dict["total_clusters"] = total_clusters
        if total_documents is not UNSET:
            field_dict["total_documents"] = total_documents
        if avg_documents_per_cluster is not UNSET:
            field_dict["avg_documents_per_cluster"] = avg_documents_per_cluster
        if clusters_by_status is not UNSET:
            field_dict["clusters_by_status"] = clusters_by_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cluster_list_stats_clusters_by_status import ClusterListStatsClustersByStatus

        d = dict(src_dict)
        total_clusters = d.pop("total_clusters", UNSET)

        total_documents = d.pop("total_documents", UNSET)

        avg_documents_per_cluster = d.pop("avg_documents_per_cluster", UNSET)

        _clusters_by_status = d.pop("clusters_by_status", UNSET)
        clusters_by_status: ClusterListStatsClustersByStatus | Unset
        if isinstance(_clusters_by_status, Unset):
            clusters_by_status = UNSET
        else:
            clusters_by_status = ClusterListStatsClustersByStatus.from_dict(_clusters_by_status)

        cluster_list_stats = cls(
            total_clusters=total_clusters,
            total_documents=total_documents,
            avg_documents_per_cluster=avg_documents_per_cluster,
            clusters_by_status=clusters_by_status,
        )

        cluster_list_stats.additional_properties = d
        return cluster_list_stats

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
