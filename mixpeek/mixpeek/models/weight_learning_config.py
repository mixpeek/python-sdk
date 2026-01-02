from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.weight_learning_config_method import WeightLearningConfigMethod
from ..models.weight_learning_config_metric import WeightLearningConfigMetric
from ..types import UNSET, Unset

T = TypeVar("T", bound="WeightLearningConfig")


@_attrs_define
class WeightLearningConfig:
    """Configuration for automatic feature weight learning in multi-feature clustering.

    When multi_feature_strategy='weighted' and feature_weights is not provided,
    this configuration controls how optimal weights are automatically learned.

    The system tries different weight combinations and picks the one that
    produces the best clustering quality (measured by silhouette score, etc.).

    Examples:
        Bayesian optimization (recommended):
        {
            "method": "bayesian",
            "max_iterations": 20,
            "metric": "silhouette",
            "sample_size": 5000
        }

        Grid search (exhaustive, limited to 2-3 features):
        {
            "method": "grid_search",
            "max_iterations": 5,
            "metric": "silhouette"
        }

        Attributes:
            method (WeightLearningConfigMethod | Unset): Weight learning method:
                - bayesian: Gaussian process optimization (recommended, scales to 5+ features)
                - grid_search: Exhaustive search (limited to 2-3 features, simpler but slower) Default:
                WeightLearningConfigMethod.BAYESIAN.
            max_iterations (int | Unset): Maximum optimization iterations:
                - grid_search: Number of values to try per feature (total: max_iterations^n_features)
                - bayesian: Number of weight combinations to evaluate
                Recommended: 20 for bayesian, 5 for grid_search Default: 20.
            metric (WeightLearningConfigMetric | Unset): Clustering quality metric to optimize:
                - silhouette: Measures how similar points are to their cluster vs other clusters (range: [-1, 1], higher is
                better)
                - davies_bouldin: Ratio of within-cluster to between-cluster distances (range: [0, ∞], lower is better)
                - calinski_harabasz: Ratio of between-cluster to within-cluster variance (range: [0, ∞], higher is better)
                Recommended: silhouette (most general-purpose) Default: WeightLearningConfigMetric.SILHOUETTE.
            sample_size (int | None | Unset): Optional: Learn weights on a random sample (speeds up large datasets).
                If provided and dataset has more documents, weights are learned on sample_size random documents, then applied to
                full dataset.
                Recommended: 5000 for datasets >10k documents
            random_state (int | Unset): Random seed for reproducibility of weight learning Default: 42.
    """

    method: WeightLearningConfigMethod | Unset = WeightLearningConfigMethod.BAYESIAN
    max_iterations: int | Unset = 20
    metric: WeightLearningConfigMetric | Unset = WeightLearningConfigMetric.SILHOUETTE
    sample_size: int | None | Unset = UNSET
    random_state: int | Unset = 42
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method: str | Unset = UNSET
        if not isinstance(self.method, Unset):
            method = self.method.value

        max_iterations = self.max_iterations

        metric: str | Unset = UNSET
        if not isinstance(self.metric, Unset):
            metric = self.metric.value

        sample_size: int | None | Unset
        if isinstance(self.sample_size, Unset):
            sample_size = UNSET
        else:
            sample_size = self.sample_size

        random_state = self.random_state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if method is not UNSET:
            field_dict["method"] = method
        if max_iterations is not UNSET:
            field_dict["max_iterations"] = max_iterations
        if metric is not UNSET:
            field_dict["metric"] = metric
        if sample_size is not UNSET:
            field_dict["sample_size"] = sample_size
        if random_state is not UNSET:
            field_dict["random_state"] = random_state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _method = d.pop("method", UNSET)
        method: WeightLearningConfigMethod | Unset
        if isinstance(_method, Unset):
            method = UNSET
        else:
            method = WeightLearningConfigMethod(_method)

        max_iterations = d.pop("max_iterations", UNSET)

        _metric = d.pop("metric", UNSET)
        metric: WeightLearningConfigMetric | Unset
        if isinstance(_metric, Unset):
            metric = UNSET
        else:
            metric = WeightLearningConfigMetric(_metric)

        def _parse_sample_size(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sample_size = _parse_sample_size(d.pop("sample_size", UNSET))

        random_state = d.pop("random_state", UNSET)

        weight_learning_config = cls(
            method=method,
            max_iterations=max_iterations,
            metric=metric,
            sample_size=sample_size,
            random_state=random_state,
        )

        weight_learning_config.additional_properties = d
        return weight_learning_config

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
