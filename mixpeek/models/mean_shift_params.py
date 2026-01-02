from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MeanShiftParams")


@_attrs_define
class MeanShiftParams:
    """Parameters for Mean Shift clustering algorithm.

    Attributes:
        bandwidth (float | None | Unset): Bandwidth used in the RBF kernel. If None, estimated using
            sklearn.cluster.estimate_bandwidth
        seeds (list[list[float]] | None | Unset): Seeds used to initialize kernels. If None, all points are used as
            seeds
        bin_seeding (bool | Unset): If true, initial kernel locations are discretized into a grid to speed up algorithm
            Default: False.
        min_bin_freq (int | Unset): Minimum number of seeds within a bin for the bin to be considered Default: 1.
        cluster_all (bool | Unset): If true, all points are clustered, even orphans. If false, orphans are given label
            -1 Default: True.
        n_jobs (int | Unset): Number of parallel jobs to run (-1 means using all processors) Default: 1.
        max_iter (int | Unset): Maximum number of iterations per seed point before the algorithm stops Default: 300.
    """

    bandwidth: float | None | Unset = UNSET
    seeds: list[list[float]] | None | Unset = UNSET
    bin_seeding: bool | Unset = False
    min_bin_freq: int | Unset = 1
    cluster_all: bool | Unset = True
    n_jobs: int | Unset = 1
    max_iter: int | Unset = 300
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bandwidth: float | None | Unset
        if isinstance(self.bandwidth, Unset):
            bandwidth = UNSET
        else:
            bandwidth = self.bandwidth

        seeds: list[list[float]] | None | Unset
        if isinstance(self.seeds, Unset):
            seeds = UNSET
        elif isinstance(self.seeds, list):
            seeds = []
            for seeds_type_0_item_data in self.seeds:
                seeds_type_0_item = seeds_type_0_item_data

                seeds.append(seeds_type_0_item)

        else:
            seeds = self.seeds

        bin_seeding = self.bin_seeding

        min_bin_freq = self.min_bin_freq

        cluster_all = self.cluster_all

        n_jobs = self.n_jobs

        max_iter = self.max_iter

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bandwidth is not UNSET:
            field_dict["bandwidth"] = bandwidth
        if seeds is not UNSET:
            field_dict["seeds"] = seeds
        if bin_seeding is not UNSET:
            field_dict["bin_seeding"] = bin_seeding
        if min_bin_freq is not UNSET:
            field_dict["min_bin_freq"] = min_bin_freq
        if cluster_all is not UNSET:
            field_dict["cluster_all"] = cluster_all
        if n_jobs is not UNSET:
            field_dict["n_jobs"] = n_jobs
        if max_iter is not UNSET:
            field_dict["max_iter"] = max_iter

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_bandwidth(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        bandwidth = _parse_bandwidth(d.pop("bandwidth", UNSET))

        def _parse_seeds(data: object) -> list[list[float]] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                seeds_type_0 = []
                _seeds_type_0 = data
                for seeds_type_0_item_data in _seeds_type_0:
                    seeds_type_0_item = cast(list[float], seeds_type_0_item_data)

                    seeds_type_0.append(seeds_type_0_item)

                return seeds_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[list[float]] | None | Unset, data)

        seeds = _parse_seeds(d.pop("seeds", UNSET))

        bin_seeding = d.pop("bin_seeding", UNSET)

        min_bin_freq = d.pop("min_bin_freq", UNSET)

        cluster_all = d.pop("cluster_all", UNSET)

        n_jobs = d.pop("n_jobs", UNSET)

        max_iter = d.pop("max_iter", UNSET)

        mean_shift_params = cls(
            bandwidth=bandwidth,
            seeds=seeds,
            bin_seeding=bin_seeding,
            min_bin_freq=min_bin_freq,
            cluster_all=cluster_all,
            n_jobs=n_jobs,
            max_iter=max_iter,
        )

        mean_shift_params.additional_properties = d
        return mean_shift_params

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
