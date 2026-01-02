from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cluster_stats_extra import ClusterStatsExtra


T = TypeVar("T", bound="ClusterStats")


@_attrs_define
class ClusterStats:
    """Basic clustering quality metrics.

    Attributes:
        num_clusters (int):
        noise_points (int | None | Unset): Number of noise points (for DBSCAN, etc.)
        silhouette_score (float | None | Unset): Silhouette score (-1 to 1, higher is better)
        extra (ClusterStatsExtra | Unset):
    """

    num_clusters: int
    noise_points: int | None | Unset = UNSET
    silhouette_score: float | None | Unset = UNSET
    extra: ClusterStatsExtra | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        num_clusters = self.num_clusters

        noise_points: int | None | Unset
        if isinstance(self.noise_points, Unset):
            noise_points = UNSET
        else:
            noise_points = self.noise_points

        silhouette_score: float | None | Unset
        if isinstance(self.silhouette_score, Unset):
            silhouette_score = UNSET
        else:
            silhouette_score = self.silhouette_score

        extra: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extra, Unset):
            extra = self.extra.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "num_clusters": num_clusters,
            }
        )
        if noise_points is not UNSET:
            field_dict["noise_points"] = noise_points
        if silhouette_score is not UNSET:
            field_dict["silhouette_score"] = silhouette_score
        if extra is not UNSET:
            field_dict["extra"] = extra

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cluster_stats_extra import ClusterStatsExtra

        d = dict(src_dict)
        num_clusters = d.pop("num_clusters")

        def _parse_noise_points(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        noise_points = _parse_noise_points(d.pop("noise_points", UNSET))

        def _parse_silhouette_score(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        silhouette_score = _parse_silhouette_score(d.pop("silhouette_score", UNSET))

        _extra = d.pop("extra", UNSET)
        extra: ClusterStatsExtra | Unset
        if isinstance(_extra, Unset):
            extra = UNSET
        else:
            extra = ClusterStatsExtra.from_dict(_extra)

        cluster_stats = cls(
            num_clusters=num_clusters,
            noise_points=noise_points,
            silhouette_score=silhouette_score,
            extra=extra,
        )

        cluster_stats.additional_properties = d
        return cluster_stats

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
