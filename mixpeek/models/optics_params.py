from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.optics_params_metric_params_type_0 import OPTICSParamsMetricParamsType0


T = TypeVar("T", bound="OPTICSParams")


@_attrs_define
class OPTICSParams:
    """Parameters for OPTICS clustering algorithm.

    Attributes:
        min_samples (int | Unset): Number of samples in a neighborhood for a point to be considered a core point
            Default: 5.
        max_eps (float | None | Unset): Maximum distance between two samples. Default (None) means no maximum distance
        metric (str | Unset): Metric to use for distance computation Default: 'minkowski'.
        p (float | Unset): Parameter for the Minkowski metric Default: 2.0.
        metric_params (None | OPTICSParamsMetricParamsType0 | Unset): Additional keyword arguments for the metric
            function
        cluster_method (str | Unset): Method to extract clusters ('xi' or 'dbscan') Default: 'xi'.
        eps (float | None | Unset): Maximum distance for DBSCAN cluster extraction method
        xi (float | Unset): Minimum steepness on the reachability plot for cluster boundary (xi method) Default: 0.05.
        predecessor_correction (bool | Unset): Correct clusters based on predecessors (xi method) Default: True.
        min_cluster_size (float | None | Unset): Minimum number of samples in a cluster. Can be a fraction if < 1.0
        algorithm (str | Unset): Algorithm to compute pointwise distances ('auto', 'ball_tree', 'kd_tree', 'brute')
            Default: 'auto'.
        leaf_size (int | Unset): Leaf size passed to BallTree or KDTree Default: 30.
        n_jobs (int | Unset): Number of parallel jobs to run (-1 means using all processors) Default: 1.
    """

    min_samples: int | Unset = 5
    max_eps: float | None | Unset = UNSET
    metric: str | Unset = "minkowski"
    p: float | Unset = 2.0
    metric_params: None | OPTICSParamsMetricParamsType0 | Unset = UNSET
    cluster_method: str | Unset = "xi"
    eps: float | None | Unset = UNSET
    xi: float | Unset = 0.05
    predecessor_correction: bool | Unset = True
    min_cluster_size: float | None | Unset = UNSET
    algorithm: str | Unset = "auto"
    leaf_size: int | Unset = 30
    n_jobs: int | Unset = 1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.optics_params_metric_params_type_0 import OPTICSParamsMetricParamsType0

        min_samples = self.min_samples

        max_eps: float | None | Unset
        if isinstance(self.max_eps, Unset):
            max_eps = UNSET
        else:
            max_eps = self.max_eps

        metric = self.metric

        p = self.p

        metric_params: dict[str, Any] | None | Unset
        if isinstance(self.metric_params, Unset):
            metric_params = UNSET
        elif isinstance(self.metric_params, OPTICSParamsMetricParamsType0):
            metric_params = self.metric_params.to_dict()
        else:
            metric_params = self.metric_params

        cluster_method = self.cluster_method

        eps: float | None | Unset
        if isinstance(self.eps, Unset):
            eps = UNSET
        else:
            eps = self.eps

        xi = self.xi

        predecessor_correction = self.predecessor_correction

        min_cluster_size: float | None | Unset
        if isinstance(self.min_cluster_size, Unset):
            min_cluster_size = UNSET
        else:
            min_cluster_size = self.min_cluster_size

        algorithm = self.algorithm

        leaf_size = self.leaf_size

        n_jobs = self.n_jobs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if min_samples is not UNSET:
            field_dict["min_samples"] = min_samples
        if max_eps is not UNSET:
            field_dict["max_eps"] = max_eps
        if metric is not UNSET:
            field_dict["metric"] = metric
        if p is not UNSET:
            field_dict["p"] = p
        if metric_params is not UNSET:
            field_dict["metric_params"] = metric_params
        if cluster_method is not UNSET:
            field_dict["cluster_method"] = cluster_method
        if eps is not UNSET:
            field_dict["eps"] = eps
        if xi is not UNSET:
            field_dict["xi"] = xi
        if predecessor_correction is not UNSET:
            field_dict["predecessor_correction"] = predecessor_correction
        if min_cluster_size is not UNSET:
            field_dict["min_cluster_size"] = min_cluster_size
        if algorithm is not UNSET:
            field_dict["algorithm"] = algorithm
        if leaf_size is not UNSET:
            field_dict["leaf_size"] = leaf_size
        if n_jobs is not UNSET:
            field_dict["n_jobs"] = n_jobs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.optics_params_metric_params_type_0 import OPTICSParamsMetricParamsType0

        d = dict(src_dict)
        min_samples = d.pop("min_samples", UNSET)

        def _parse_max_eps(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        max_eps = _parse_max_eps(d.pop("max_eps", UNSET))

        metric = d.pop("metric", UNSET)

        p = d.pop("p", UNSET)

        def _parse_metric_params(data: object) -> None | OPTICSParamsMetricParamsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metric_params_type_0 = OPTICSParamsMetricParamsType0.from_dict(data)

                return metric_params_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OPTICSParamsMetricParamsType0 | Unset, data)

        metric_params = _parse_metric_params(d.pop("metric_params", UNSET))

        cluster_method = d.pop("cluster_method", UNSET)

        def _parse_eps(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        eps = _parse_eps(d.pop("eps", UNSET))

        xi = d.pop("xi", UNSET)

        predecessor_correction = d.pop("predecessor_correction", UNSET)

        def _parse_min_cluster_size(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        min_cluster_size = _parse_min_cluster_size(d.pop("min_cluster_size", UNSET))

        algorithm = d.pop("algorithm", UNSET)

        leaf_size = d.pop("leaf_size", UNSET)

        n_jobs = d.pop("n_jobs", UNSET)

        optics_params = cls(
            min_samples=min_samples,
            max_eps=max_eps,
            metric=metric,
            p=p,
            metric_params=metric_params,
            cluster_method=cluster_method,
            eps=eps,
            xi=xi,
            predecessor_correction=predecessor_correction,
            min_cluster_size=min_cluster_size,
            algorithm=algorithm,
            leaf_size=leaf_size,
            n_jobs=n_jobs,
        )

        optics_params.additional_properties = d
        return optics_params

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
