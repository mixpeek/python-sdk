from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.covariate_config_binning_strategy_type_0 import CovariateConfigBinningStrategyType0
from ..models.covariate_config_clustering_method_type_0 import CovariateConfigClusteringMethodType0
from ..models.covariate_type import CovariateType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CovariateConfig")


@_attrs_define
class CovariateConfig:
    """Configuration for a single covariate/predictor variable in step analytics.

    Covariates are used to identify which features predict conversion from one step
    to another. The system computes "lift" for each covariate value, showing whether
    it increases or decreases conversion likelihood.

    Attributes:
        field_path: JSONPath to the field in document or metadata (e.g., "sender_domain")
        covariate_type: How to analyze this covariate (categorical, numeric, embedding, cluster)
        name: Human-readable name for analytics results
        binning_strategy: For NUMERIC types, how to bin values (quartiles, deciles)
        clustering_method: For EMBEDDING types, algorithm to use (kmeans, hdbscan)
        n_clusters: For EMBEDDING types, number of clusters to create

    Examples:
        ```python
        # Analyze sender domains (categorical)
        CovariateConfig(
            field_path="sender_domain",
            covariate_type="categorical",
            name="Email Domain"
        )

        # Analyze email length (numeric with quartile binning)
        CovariateConfig(
            field_path="word_count",
            covariate_type="numeric",
            name="Word Count",
            binning_strategy="quartiles"
        )

        # Analyze visual similarity (embedding clustering)
        CovariateConfig(
            field_path="features.clip_embedding",
            covariate_type="embedding",
            name="Visual Cluster",
            clustering_method="kmeans",
            n_clusters=10
        )
        ```

        Attributes:
            field_path (str): Dot-notation path to covariate field (e.g., 'sender_domain', 'metadata.priority')
            covariate_type (CovariateType): Type of covariate/predictor variable for conversion analysis.

                Different types enable different analysis strategies:
                - CATEGORICAL: String values, analyzed via grouping (e.g., sender_domain, priority)
                - NUMERIC: Continuous values, binned into quartiles/deciles (e.g., word_count, price)
                - EMBEDDING: Dense vectors, clustered for semantic analysis (e.g., CLIP embeddings)
                - CLUSTER_ID: Pre-computed cluster identifiers (e.g., topic_cluster, visual_cluster)

                Examples:
                    ```python
                    # Categorical: Which email domains convert better?
                    CovariateConfig(field_path="sender_domain", covariate_type="categorical")

                    # Numeric: Do longer emails convert faster?
                    CovariateConfig(field_path="word_count", covariate_type="numeric")

                    # Embedding: Do visually similar images follow similar paths?
                    CovariateConfig(field_path="features.clip", covariate_type="embedding")

                    # Cluster: Which topic clusters have highest conversion?
                    CovariateConfig(field_path="metadata.topic_id", covariate_type="cluster_id")
                    ```
            name (str): Human-readable name for this covariate in analytics results
            binning_strategy (CovariateConfigBinningStrategyType0 | None | Unset): How to bin numeric values for lift
                analysis (only used for NUMERIC type) Default: CovariateConfigBinningStrategyType0.QUARTILES.
            clustering_method (CovariateConfigClusteringMethodType0 | None | Unset): Clustering algorithm for embedding
                analysis (only used for EMBEDDING type) Default: CovariateConfigClusteringMethodType0.KMEANS.
            n_clusters (int | None | Unset): Number of clusters for embedding-based predictors (only used for EMBEDDING
                type) Default: 10.
    """

    field_path: str
    covariate_type: CovariateType
    name: str
    binning_strategy: CovariateConfigBinningStrategyType0 | None | Unset = CovariateConfigBinningStrategyType0.QUARTILES
    clustering_method: CovariateConfigClusteringMethodType0 | None | Unset = CovariateConfigClusteringMethodType0.KMEANS
    n_clusters: int | None | Unset = 10
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_path = self.field_path

        covariate_type = self.covariate_type.value

        name = self.name

        binning_strategy: None | str | Unset
        if isinstance(self.binning_strategy, Unset):
            binning_strategy = UNSET
        elif isinstance(self.binning_strategy, CovariateConfigBinningStrategyType0):
            binning_strategy = self.binning_strategy.value
        else:
            binning_strategy = self.binning_strategy

        clustering_method: None | str | Unset
        if isinstance(self.clustering_method, Unset):
            clustering_method = UNSET
        elif isinstance(self.clustering_method, CovariateConfigClusteringMethodType0):
            clustering_method = self.clustering_method.value
        else:
            clustering_method = self.clustering_method

        n_clusters: int | None | Unset
        if isinstance(self.n_clusters, Unset):
            n_clusters = UNSET
        else:
            n_clusters = self.n_clusters

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "field_path": field_path,
                "covariate_type": covariate_type,
                "name": name,
            }
        )
        if binning_strategy is not UNSET:
            field_dict["binning_strategy"] = binning_strategy
        if clustering_method is not UNSET:
            field_dict["clustering_method"] = clustering_method
        if n_clusters is not UNSET:
            field_dict["n_clusters"] = n_clusters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_path = d.pop("field_path")

        covariate_type = CovariateType(d.pop("covariate_type"))

        name = d.pop("name")

        def _parse_binning_strategy(data: object) -> CovariateConfigBinningStrategyType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                binning_strategy_type_0 = CovariateConfigBinningStrategyType0(data)

                return binning_strategy_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CovariateConfigBinningStrategyType0 | None | Unset, data)

        binning_strategy = _parse_binning_strategy(d.pop("binning_strategy", UNSET))

        def _parse_clustering_method(data: object) -> CovariateConfigClusteringMethodType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                clustering_method_type_0 = CovariateConfigClusteringMethodType0(data)

                return clustering_method_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CovariateConfigClusteringMethodType0 | None | Unset, data)

        clustering_method = _parse_clustering_method(d.pop("clustering_method", UNSET))

        def _parse_n_clusters(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        n_clusters = _parse_n_clusters(d.pop("n_clusters", UNSET))

        covariate_config = cls(
            field_path=field_path,
            covariate_type=covariate_type,
            name=name,
            binning_strategy=binning_strategy,
            clustering_method=clustering_method,
            n_clusters=n_clusters,
        )

        covariate_config.additional_properties = d
        return covariate_config

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
