from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dbscan_params_metric_params import DBSCANParamsMetricParams


T = TypeVar("T", bound="DBSCANParams")


@_attrs_define
class DBSCANParams:
    """Parameters for DBSCAN clustering algorithm.

    Attributes:
        eps (float | Unset): Maximum distance between two samples for one to be considered in the neighborhood of the
            other Default: 0.5.
        min_samples (int | Unset): Number of samples in a neighborhood for a point to be considered a core point
            Default: 5.
        metric (str | Unset): Metric to use for distance computation Default: 'euclidean'.
        metric_params (DBSCANParamsMetricParams | Unset): Additional keyword arguments for the metric function
        algorithm (str | Unset): Algorithm to compute pointwise distances and find nearest neighbors ('auto',
            'ball_tree', 'kd_tree', 'brute') Default: 'auto'.
        leaf_size (int | Unset): Leaf size passed to BallTree or KDTree Default: 30.
        p (float | Unset): The power of the Minkowski metric to be used to calculate distance between points Default:
            2.0.
        n_jobs (int | Unset): The number of parallel jobs to run (-1 means using all processors) Default: 1.
    """

    eps: float | Unset = 0.5
    min_samples: int | Unset = 5
    metric: str | Unset = "euclidean"
    metric_params: DBSCANParamsMetricParams | Unset = UNSET
    algorithm: str | Unset = "auto"
    leaf_size: int | Unset = 30
    p: float | Unset = 2.0
    n_jobs: int | Unset = 1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        eps = self.eps

        min_samples = self.min_samples

        metric = self.metric

        metric_params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metric_params, Unset):
            metric_params = self.metric_params.to_dict()

        algorithm = self.algorithm

        leaf_size = self.leaf_size

        p = self.p

        n_jobs = self.n_jobs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if eps is not UNSET:
            field_dict["eps"] = eps
        if min_samples is not UNSET:
            field_dict["min_samples"] = min_samples
        if metric is not UNSET:
            field_dict["metric"] = metric
        if metric_params is not UNSET:
            field_dict["metric_params"] = metric_params
        if algorithm is not UNSET:
            field_dict["algorithm"] = algorithm
        if leaf_size is not UNSET:
            field_dict["leaf_size"] = leaf_size
        if p is not UNSET:
            field_dict["p"] = p
        if n_jobs is not UNSET:
            field_dict["n_jobs"] = n_jobs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dbscan_params_metric_params import DBSCANParamsMetricParams

        d = dict(src_dict)
        eps = d.pop("eps", UNSET)

        min_samples = d.pop("min_samples", UNSET)

        metric = d.pop("metric", UNSET)

        _metric_params = d.pop("metric_params", UNSET)
        metric_params: DBSCANParamsMetricParams | Unset
        if isinstance(_metric_params, Unset):
            metric_params = UNSET
        else:
            metric_params = DBSCANParamsMetricParams.from_dict(_metric_params)

        algorithm = d.pop("algorithm", UNSET)

        leaf_size = d.pop("leaf_size", UNSET)

        p = d.pop("p", UNSET)

        n_jobs = d.pop("n_jobs", UNSET)

        dbscan_params = cls(
            eps=eps,
            min_samples=min_samples,
            metric=metric,
            metric_params=metric_params,
            algorithm=algorithm,
            leaf_size=leaf_size,
            p=p,
            n_jobs=n_jobs,
        )

        dbscan_params.additional_properties = d
        return dbscan_params

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
