from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AgglomerativeParams")


@_attrs_define
class AgglomerativeParams:
    """Parameters for Agglomerative clustering algorithm.

    Attributes:
        n_clusters (int | None | Unset): Number of clusters to find. Can be None if distance_threshold is not None
            Default: 2.
        affinity (str | Unset): Metric used to compute linkage. Can be 'euclidean', 'l1', 'l2', 'manhattan', 'cosine',
            or 'precomputed' Default: 'euclidean'.
        memory (None | str | Unset): Path to the caching directory
        connectivity (Any | None | Unset): Connectivity matrix. Defines which samples are neighbors
        compute_full_tree (str | Unset): Whether to compute the full tree ('auto', True, or False) Default: 'auto'.
        linkage (str | Unset): Linkage criterion ('ward', 'complete', 'average', 'single') Default: 'ward'.
        distance_threshold (float | None | Unset): The linkage distance threshold above which clusters will not be
            merged
        compute_distances (bool | Unset): Whether to compute distances between clusters Default: False.
    """

    n_clusters: int | None | Unset = 2
    affinity: str | Unset = "euclidean"
    memory: None | str | Unset = UNSET
    connectivity: Any | None | Unset = UNSET
    compute_full_tree: str | Unset = "auto"
    linkage: str | Unset = "ward"
    distance_threshold: float | None | Unset = UNSET
    compute_distances: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        n_clusters: int | None | Unset
        if isinstance(self.n_clusters, Unset):
            n_clusters = UNSET
        else:
            n_clusters = self.n_clusters

        affinity = self.affinity

        memory: None | str | Unset
        if isinstance(self.memory, Unset):
            memory = UNSET
        else:
            memory = self.memory

        connectivity: Any | None | Unset
        if isinstance(self.connectivity, Unset):
            connectivity = UNSET
        else:
            connectivity = self.connectivity

        compute_full_tree = self.compute_full_tree

        linkage = self.linkage

        distance_threshold: float | None | Unset
        if isinstance(self.distance_threshold, Unset):
            distance_threshold = UNSET
        else:
            distance_threshold = self.distance_threshold

        compute_distances = self.compute_distances

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if n_clusters is not UNSET:
            field_dict["n_clusters"] = n_clusters
        if affinity is not UNSET:
            field_dict["affinity"] = affinity
        if memory is not UNSET:
            field_dict["memory"] = memory
        if connectivity is not UNSET:
            field_dict["connectivity"] = connectivity
        if compute_full_tree is not UNSET:
            field_dict["compute_full_tree"] = compute_full_tree
        if linkage is not UNSET:
            field_dict["linkage"] = linkage
        if distance_threshold is not UNSET:
            field_dict["distance_threshold"] = distance_threshold
        if compute_distances is not UNSET:
            field_dict["compute_distances"] = compute_distances

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_n_clusters(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        n_clusters = _parse_n_clusters(d.pop("n_clusters", UNSET))

        affinity = d.pop("affinity", UNSET)

        def _parse_memory(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        memory = _parse_memory(d.pop("memory", UNSET))

        def _parse_connectivity(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        connectivity = _parse_connectivity(d.pop("connectivity", UNSET))

        compute_full_tree = d.pop("compute_full_tree", UNSET)

        linkage = d.pop("linkage", UNSET)

        def _parse_distance_threshold(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        distance_threshold = _parse_distance_threshold(d.pop("distance_threshold", UNSET))

        compute_distances = d.pop("compute_distances", UNSET)

        agglomerative_params = cls(
            n_clusters=n_clusters,
            affinity=affinity,
            memory=memory,
            connectivity=connectivity,
            compute_full_tree=compute_full_tree,
            linkage=linkage,
            distance_threshold=distance_threshold,
            compute_distances=compute_distances,
        )

        agglomerative_params.additional_properties = d
        return agglomerative_params

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
