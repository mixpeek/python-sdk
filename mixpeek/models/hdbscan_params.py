from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HDBSCANParams")


@_attrs_define
class HDBSCANParams:
    """Parameters for HDBSCAN clustering algorithm.

    Attributes:
        min_cluster_size (int | Unset): Minimum number of samples in a cluster Default: 5.
        min_samples (int | None | Unset): Number of samples in a neighborhood for a point to be considered a core point.
            Defaults to min_cluster_size if None
        cluster_selection_epsilon (float | Unset): A distance threshold for cluster selection. Clusters below this value
            will be merged Default: 0.0.
        max_cluster_size (int | None | Unset): Maximum number of samples in a cluster. Clusters above this size will be
            split
        metric (str | Unset): Metric to use for distance computation Default: 'euclidean'.
        alpha (float | Unset): A distance scaling parameter Default: 1.0.
        cluster_selection_method (str | Unset): Method to select clusters from the condensed tree ('eom' or 'leaf')
            Default: 'eom'.
        allow_single_cluster (bool | Unset): Allow HDBSCAN to find only a single cluster Default: False.
        prediction_data (bool | Unset): Whether to generate extra data for predicting cluster membership Default: False.
        match_reference_implementation (bool | Unset): Whether to match the reference implementation exactly Default:
            False.
    """

    min_cluster_size: int | Unset = 5
    min_samples: int | None | Unset = UNSET
    cluster_selection_epsilon: float | Unset = 0.0
    max_cluster_size: int | None | Unset = UNSET
    metric: str | Unset = "euclidean"
    alpha: float | Unset = 1.0
    cluster_selection_method: str | Unset = "eom"
    allow_single_cluster: bool | Unset = False
    prediction_data: bool | Unset = False
    match_reference_implementation: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        min_cluster_size = self.min_cluster_size

        min_samples: int | None | Unset
        if isinstance(self.min_samples, Unset):
            min_samples = UNSET
        else:
            min_samples = self.min_samples

        cluster_selection_epsilon = self.cluster_selection_epsilon

        max_cluster_size: int | None | Unset
        if isinstance(self.max_cluster_size, Unset):
            max_cluster_size = UNSET
        else:
            max_cluster_size = self.max_cluster_size

        metric = self.metric

        alpha = self.alpha

        cluster_selection_method = self.cluster_selection_method

        allow_single_cluster = self.allow_single_cluster

        prediction_data = self.prediction_data

        match_reference_implementation = self.match_reference_implementation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if min_cluster_size is not UNSET:
            field_dict["min_cluster_size"] = min_cluster_size
        if min_samples is not UNSET:
            field_dict["min_samples"] = min_samples
        if cluster_selection_epsilon is not UNSET:
            field_dict["cluster_selection_epsilon"] = cluster_selection_epsilon
        if max_cluster_size is not UNSET:
            field_dict["max_cluster_size"] = max_cluster_size
        if metric is not UNSET:
            field_dict["metric"] = metric
        if alpha is not UNSET:
            field_dict["alpha"] = alpha
        if cluster_selection_method is not UNSET:
            field_dict["cluster_selection_method"] = cluster_selection_method
        if allow_single_cluster is not UNSET:
            field_dict["allow_single_cluster"] = allow_single_cluster
        if prediction_data is not UNSET:
            field_dict["prediction_data"] = prediction_data
        if match_reference_implementation is not UNSET:
            field_dict["match_reference_implementation"] = match_reference_implementation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        min_cluster_size = d.pop("min_cluster_size", UNSET)

        def _parse_min_samples(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        min_samples = _parse_min_samples(d.pop("min_samples", UNSET))

        cluster_selection_epsilon = d.pop("cluster_selection_epsilon", UNSET)

        def _parse_max_cluster_size(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_cluster_size = _parse_max_cluster_size(d.pop("max_cluster_size", UNSET))

        metric = d.pop("metric", UNSET)

        alpha = d.pop("alpha", UNSET)

        cluster_selection_method = d.pop("cluster_selection_method", UNSET)

        allow_single_cluster = d.pop("allow_single_cluster", UNSET)

        prediction_data = d.pop("prediction_data", UNSET)

        match_reference_implementation = d.pop("match_reference_implementation", UNSET)

        hdbscan_params = cls(
            min_cluster_size=min_cluster_size,
            min_samples=min_samples,
            cluster_selection_epsilon=cluster_selection_epsilon,
            max_cluster_size=max_cluster_size,
            metric=metric,
            alpha=alpha,
            cluster_selection_method=cluster_selection_method,
            allow_single_cluster=allow_single_cluster,
            prediction_data=prediction_data,
            match_reference_implementation=match_reference_implementation,
        )

        hdbscan_params.additional_properties = d
        return hdbscan_params

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
