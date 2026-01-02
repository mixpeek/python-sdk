from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClusterOptions")


@_attrs_define
class ClusterOptions:
    """Options for cluster migration.

    Attributes:
        preserve_cluster_ids (bool | Unset): Keep same cluster IDs in target Default: True.
        preserve_assignments (bool | Unset): Keep cluster_id in documents Default: True.
        migrate_artifacts (bool | Unset): Copy parquet artifacts from S3 Default: True.
        preserve_centroids (bool | Unset): Keep centroid collections Default: True.
        recompute_clusters (bool | Unset): Recompute clusters instead of copying Default: False.
    """

    preserve_cluster_ids: bool | Unset = True
    preserve_assignments: bool | Unset = True
    migrate_artifacts: bool | Unset = True
    preserve_centroids: bool | Unset = True
    recompute_clusters: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        preserve_cluster_ids = self.preserve_cluster_ids

        preserve_assignments = self.preserve_assignments

        migrate_artifacts = self.migrate_artifacts

        preserve_centroids = self.preserve_centroids

        recompute_clusters = self.recompute_clusters

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if preserve_cluster_ids is not UNSET:
            field_dict["preserve_cluster_ids"] = preserve_cluster_ids
        if preserve_assignments is not UNSET:
            field_dict["preserve_assignments"] = preserve_assignments
        if migrate_artifacts is not UNSET:
            field_dict["migrate_artifacts"] = migrate_artifacts
        if preserve_centroids is not UNSET:
            field_dict["preserve_centroids"] = preserve_centroids
        if recompute_clusters is not UNSET:
            field_dict["recompute_clusters"] = recompute_clusters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        preserve_cluster_ids = d.pop("preserve_cluster_ids", UNSET)

        preserve_assignments = d.pop("preserve_assignments", UNSET)

        migrate_artifacts = d.pop("migrate_artifacts", UNSET)

        preserve_centroids = d.pop("preserve_centroids", UNSET)

        recompute_clusters = d.pop("recompute_clusters", UNSET)

        cluster_options = cls(
            preserve_cluster_ids=preserve_cluster_ids,
            preserve_assignments=preserve_assignments,
            migrate_artifacts=migrate_artifacts,
            preserve_centroids=preserve_centroids,
            recompute_clusters=recompute_clusters,
        )

        cluster_options.additional_properties = d
        return cluster_options

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
