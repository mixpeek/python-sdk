from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.clustering_algorithm import ClusteringAlgorithm
from ..models.vector_based_config_effective_feature_method import VectorBasedConfigEffectiveFeatureMethod
from ..models.vector_based_config_multi_feature_strategy import VectorBasedConfigMultiFeatureStrategy
from ..models.vector_based_config_output_strategy import VectorBasedConfigOutputStrategy
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agglomerative_params import AgglomerativeParams
    from ..models.dbscan_params import DBSCANParams
    from ..models.gaussian_mixture_params import GaussianMixtureParams
    from ..models.hdbscan_params import HDBSCANParams
    from ..models.k_means_params import KMeansParams
    from ..models.mean_shift_params import MeanShiftParams
    from ..models.optics_params import OPTICSParams
    from ..models.spectral_params import SpectralParams
    from ..models.vector_based_config_algorithm_params_type_8 import VectorBasedConfigAlgorithmParamsType8
    from ..models.vector_based_config_dbscan_parameters_type_1 import VectorBasedConfigDbscanParametersType1
    from ..models.vector_based_config_feature_weights_type_0 import VectorBasedConfigFeatureWeightsType0
    from ..models.vector_based_config_hdbscan_parameters_type_1 import VectorBasedConfigHdbscanParametersType1
    from ..models.vector_based_config_kmeans_parameters_type_1 import VectorBasedConfigKmeansParametersType1
    from ..models.weight_learning_config import WeightLearningConfig


T = TypeVar("T", bound="VectorBasedConfig")


@_attrs_define
class VectorBasedConfig:
    """Configuration for vector-based clustering.

    Use canonical feature URIs to specify which vector embeddings to cluster.
    Feature URIs follow the format: mixpeek://{extractor}@{version}/{output}

    Supports both single and multi-feature clustering:
    - Single feature: Provide one feature_uri for standard clustering
    - Multi-feature: Provide multiple feature_uris for hybrid clustering

    Examples:
        Single feature:
        {
            "feature_uri": "mixpeek://multimodal_extractor@v1/vertex_multimodal_embedding",
            "clustering_method": "hdbscan",
            "sample_size": 1000
        }

        Multi-feature:
        {
            "feature_uris": [
                "mixpeek://text_extractor@v1/multilingual_e5_large_instruct_v1",
                "mixpeek://image_extractor@v1/embedding"
            ],
            "clustering_method": "hdbscan",
            "multi_feature_strategy": "concatenate"
        }

        Attributes:
            clustering_method (ClusteringAlgorithm): Supported clustering algorithms.

                Two types of clustering are available:
                1. Vector-based: Clusters documents by embedding similarity
                2. Attribute-based: Clusters documents by metadata attributes

                Vector-based algorithms (require feature_vector):
                    - kmeans: Partitions data into K clusters by minimizing within-cluster variance
                    - dbscan: Density-based clustering, finds clusters of arbitrary shape
                    - hdbscan: Hierarchical DBSCAN, auto-determines number of clusters
                    - agglomerative: Hierarchical clustering using linkage criteria
                    - spectral: Uses graph theory to find clusters
                    - gaussian_mixture: Probabilistic model assuming Gaussian distributions
                    - mean_shift: Finds clusters by locating density maxima
                    - optics: Ordering points to identify clustering structure

                Attribute-based algorithm (requires attribute_config):
                    - attribute_based: Groups documents by metadata attributes (e.g., category, brand)
            feature_uri (None | str | Unset): DEPRECATED: Use feature_uris instead. Canonical feature URI for the vector
                embedding to cluster. Format: 'mixpeek://{extractor}@{version}/{output}'. For multi-feature clustering, use
                feature_uris (plural) instead.
            feature_uris (list[str] | None | Unset): RECOMMENDED. List of feature URIs to cluster. Format:
                'mixpeek://{extractor}@{version}/{output}'. For single-feature clustering, provide a list with one element. For
                multi-feature clustering, provide multiple feature URIs. Each feature must exist in all input collections.
            feature_extractor_name (None | str | Unset): Internal field populated from feature_uri. Do not set manually.
            version (None | str | Unset): Internal field populated from feature_uri. Do not set manually.
            output_name (None | str | Unset): Internal field populated from feature_uri. Do not set manually.
            sample_size (int | None | Unset): Number of samples to use for clustering
            kmeans_parameters (KMeansParams | None | Unset | VectorBasedConfigKmeansParametersType1): Parameters for K-means
                clustering (deprecated, use algorithm_params)
            dbscan_parameters (DBSCANParams | None | Unset | VectorBasedConfigDbscanParametersType1): Parameters for DBSCAN
                clustering (deprecated, use algorithm_params)
            hdbscan_parameters (HDBSCANParams | None | Unset | VectorBasedConfigHdbscanParametersType1): Parameters for
                HDBSCAN clustering (deprecated, use algorithm_params)
            algorithm_params (AgglomerativeParams | DBSCANParams | GaussianMixtureParams | HDBSCANParams | KMeansParams |
                MeanShiftParams | None | OPTICSParams | SpectralParams | Unset | VectorBasedConfigAlgorithmParamsType8):
                Algorithm-specific parameters
            multi_feature_strategy (VectorBasedConfigMultiFeatureStrategy | Unset): Strategy for handling multiple feature
                vectors:
                - concatenate: Combine embeddings into one vector, single clustering
                - independent: Run separate clustering per feature
                - weighted: Learn optimal feature weights Default: VectorBasedConfigMultiFeatureStrategy.CONCATENATE.
            normalize_features (bool | Unset): Apply L2 normalization to each feature block before concatenation. Prevents
                feature dominance when combining different modalities. Only applies when multi_feature_strategy='concatenate'.
                Default: True.
            feature_weights (None | Unset | VectorBasedConfigFeatureWeightsType0): Optional per-feature weights (0.0-1.0)
                for concatenation strategy. Keys are feature URIs, values are weights. Example: {'mixpeek://text@v1/emb': 0.7,
                'mixpeek://image@v1/emb': 0.3}. Defaults to equal weights (1.0) if not specified. Only applies when
                multi_feature_strategy='concatenate'. If multi_feature_strategy='weighted' and this is None, weights are learned
                automatically using weight_learning_config.
            weight_learning_config (None | Unset | WeightLearningConfig): Configuration for automatic feature weight
                learning. Only used when multi_feature_strategy='weighted' and feature_weights is None. If feature_weights is
                provided, manual weights are used instead of learning. If this is None when learning is needed, default
                WeightLearningConfig is used.
            output_strategy (VectorBasedConfigOutputStrategy | Unset): Output collection creation strategy:
                - single: Create one collection with all feature vectors
                - per_feature: Create separate collections for each feature (for hierarchical taxonomies) Default:
                VectorBasedConfigOutputStrategy.SINGLE.
            effective_feature_method (VectorBasedConfigEffectiveFeatureMethod | Unset): Method for calculating cluster
                centroids:
                - mean: Average of all vectors in cluster
                - median: Median vector (robust to outliers)
                - medoid: Actual cluster member closest to centroid Default: VectorBasedConfigEffectiveFeatureMethod.MEAN.
            enrich_source (bool | Unset): Whether to enrich source documents with cluster_id Default: False.
    """

    clustering_method: ClusteringAlgorithm
    feature_uri: None | str | Unset = UNSET
    feature_uris: list[str] | None | Unset = UNSET
    feature_extractor_name: None | str | Unset = UNSET
    version: None | str | Unset = UNSET
    output_name: None | str | Unset = UNSET
    sample_size: int | None | Unset = UNSET
    kmeans_parameters: KMeansParams | None | Unset | VectorBasedConfigKmeansParametersType1 = UNSET
    dbscan_parameters: DBSCANParams | None | Unset | VectorBasedConfigDbscanParametersType1 = UNSET
    hdbscan_parameters: HDBSCANParams | None | Unset | VectorBasedConfigHdbscanParametersType1 = UNSET
    algorithm_params: (
        AgglomerativeParams
        | DBSCANParams
        | GaussianMixtureParams
        | HDBSCANParams
        | KMeansParams
        | MeanShiftParams
        | None
        | OPTICSParams
        | SpectralParams
        | Unset
        | VectorBasedConfigAlgorithmParamsType8
    ) = UNSET
    multi_feature_strategy: VectorBasedConfigMultiFeatureStrategy | Unset = (
        VectorBasedConfigMultiFeatureStrategy.CONCATENATE
    )
    normalize_features: bool | Unset = True
    feature_weights: None | Unset | VectorBasedConfigFeatureWeightsType0 = UNSET
    weight_learning_config: None | Unset | WeightLearningConfig = UNSET
    output_strategy: VectorBasedConfigOutputStrategy | Unset = VectorBasedConfigOutputStrategy.SINGLE
    effective_feature_method: VectorBasedConfigEffectiveFeatureMethod | Unset = (
        VectorBasedConfigEffectiveFeatureMethod.MEAN
    )
    enrich_source: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.agglomerative_params import AgglomerativeParams
        from ..models.dbscan_params import DBSCANParams
        from ..models.gaussian_mixture_params import GaussianMixtureParams
        from ..models.hdbscan_params import HDBSCANParams
        from ..models.k_means_params import KMeansParams
        from ..models.mean_shift_params import MeanShiftParams
        from ..models.optics_params import OPTICSParams
        from ..models.spectral_params import SpectralParams
        from ..models.vector_based_config_algorithm_params_type_8 import VectorBasedConfigAlgorithmParamsType8
        from ..models.vector_based_config_dbscan_parameters_type_1 import VectorBasedConfigDbscanParametersType1
        from ..models.vector_based_config_feature_weights_type_0 import VectorBasedConfigFeatureWeightsType0
        from ..models.vector_based_config_hdbscan_parameters_type_1 import VectorBasedConfigHdbscanParametersType1
        from ..models.vector_based_config_kmeans_parameters_type_1 import VectorBasedConfigKmeansParametersType1
        from ..models.weight_learning_config import WeightLearningConfig

        clustering_method = self.clustering_method.value

        feature_uri: None | str | Unset
        if isinstance(self.feature_uri, Unset):
            feature_uri = UNSET
        else:
            feature_uri = self.feature_uri

        feature_uris: list[str] | None | Unset
        if isinstance(self.feature_uris, Unset):
            feature_uris = UNSET
        elif isinstance(self.feature_uris, list):
            feature_uris = self.feature_uris

        else:
            feature_uris = self.feature_uris

        feature_extractor_name: None | str | Unset
        if isinstance(self.feature_extractor_name, Unset):
            feature_extractor_name = UNSET
        else:
            feature_extractor_name = self.feature_extractor_name

        version: None | str | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        output_name: None | str | Unset
        if isinstance(self.output_name, Unset):
            output_name = UNSET
        else:
            output_name = self.output_name

        sample_size: int | None | Unset
        if isinstance(self.sample_size, Unset):
            sample_size = UNSET
        else:
            sample_size = self.sample_size

        kmeans_parameters: dict[str, Any] | None | Unset
        if isinstance(self.kmeans_parameters, Unset):
            kmeans_parameters = UNSET
        elif isinstance(self.kmeans_parameters, KMeansParams):
            kmeans_parameters = self.kmeans_parameters.to_dict()
        elif isinstance(self.kmeans_parameters, VectorBasedConfigKmeansParametersType1):
            kmeans_parameters = self.kmeans_parameters.to_dict()
        else:
            kmeans_parameters = self.kmeans_parameters

        dbscan_parameters: dict[str, Any] | None | Unset
        if isinstance(self.dbscan_parameters, Unset):
            dbscan_parameters = UNSET
        elif isinstance(self.dbscan_parameters, DBSCANParams):
            dbscan_parameters = self.dbscan_parameters.to_dict()
        elif isinstance(self.dbscan_parameters, VectorBasedConfigDbscanParametersType1):
            dbscan_parameters = self.dbscan_parameters.to_dict()
        else:
            dbscan_parameters = self.dbscan_parameters

        hdbscan_parameters: dict[str, Any] | None | Unset
        if isinstance(self.hdbscan_parameters, Unset):
            hdbscan_parameters = UNSET
        elif isinstance(self.hdbscan_parameters, HDBSCANParams):
            hdbscan_parameters = self.hdbscan_parameters.to_dict()
        elif isinstance(self.hdbscan_parameters, VectorBasedConfigHdbscanParametersType1):
            hdbscan_parameters = self.hdbscan_parameters.to_dict()
        else:
            hdbscan_parameters = self.hdbscan_parameters

        algorithm_params: dict[str, Any] | None | Unset
        if isinstance(self.algorithm_params, Unset):
            algorithm_params = UNSET
        elif isinstance(self.algorithm_params, KMeansParams):
            algorithm_params = self.algorithm_params.to_dict()
        elif isinstance(self.algorithm_params, DBSCANParams):
            algorithm_params = self.algorithm_params.to_dict()
        elif isinstance(self.algorithm_params, HDBSCANParams):
            algorithm_params = self.algorithm_params.to_dict()
        elif isinstance(self.algorithm_params, AgglomerativeParams):
            algorithm_params = self.algorithm_params.to_dict()
        elif isinstance(self.algorithm_params, SpectralParams):
            algorithm_params = self.algorithm_params.to_dict()
        elif isinstance(self.algorithm_params, GaussianMixtureParams):
            algorithm_params = self.algorithm_params.to_dict()
        elif isinstance(self.algorithm_params, MeanShiftParams):
            algorithm_params = self.algorithm_params.to_dict()
        elif isinstance(self.algorithm_params, OPTICSParams):
            algorithm_params = self.algorithm_params.to_dict()
        elif isinstance(self.algorithm_params, VectorBasedConfigAlgorithmParamsType8):
            algorithm_params = self.algorithm_params.to_dict()
        else:
            algorithm_params = self.algorithm_params

        multi_feature_strategy: str | Unset = UNSET
        if not isinstance(self.multi_feature_strategy, Unset):
            multi_feature_strategy = self.multi_feature_strategy.value

        normalize_features = self.normalize_features

        feature_weights: dict[str, Any] | None | Unset
        if isinstance(self.feature_weights, Unset):
            feature_weights = UNSET
        elif isinstance(self.feature_weights, VectorBasedConfigFeatureWeightsType0):
            feature_weights = self.feature_weights.to_dict()
        else:
            feature_weights = self.feature_weights

        weight_learning_config: dict[str, Any] | None | Unset
        if isinstance(self.weight_learning_config, Unset):
            weight_learning_config = UNSET
        elif isinstance(self.weight_learning_config, WeightLearningConfig):
            weight_learning_config = self.weight_learning_config.to_dict()
        else:
            weight_learning_config = self.weight_learning_config

        output_strategy: str | Unset = UNSET
        if not isinstance(self.output_strategy, Unset):
            output_strategy = self.output_strategy.value

        effective_feature_method: str | Unset = UNSET
        if not isinstance(self.effective_feature_method, Unset):
            effective_feature_method = self.effective_feature_method.value

        enrich_source = self.enrich_source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clustering_method": clustering_method,
            }
        )
        if feature_uri is not UNSET:
            field_dict["feature_uri"] = feature_uri
        if feature_uris is not UNSET:
            field_dict["feature_uris"] = feature_uris
        if feature_extractor_name is not UNSET:
            field_dict["feature_extractor_name"] = feature_extractor_name
        if version is not UNSET:
            field_dict["version"] = version
        if output_name is not UNSET:
            field_dict["output_name"] = output_name
        if sample_size is not UNSET:
            field_dict["sample_size"] = sample_size
        if kmeans_parameters is not UNSET:
            field_dict["kmeans_parameters"] = kmeans_parameters
        if dbscan_parameters is not UNSET:
            field_dict["dbscan_parameters"] = dbscan_parameters
        if hdbscan_parameters is not UNSET:
            field_dict["hdbscan_parameters"] = hdbscan_parameters
        if algorithm_params is not UNSET:
            field_dict["algorithm_params"] = algorithm_params
        if multi_feature_strategy is not UNSET:
            field_dict["multi_feature_strategy"] = multi_feature_strategy
        if normalize_features is not UNSET:
            field_dict["normalize_features"] = normalize_features
        if feature_weights is not UNSET:
            field_dict["feature_weights"] = feature_weights
        if weight_learning_config is not UNSET:
            field_dict["weight_learning_config"] = weight_learning_config
        if output_strategy is not UNSET:
            field_dict["output_strategy"] = output_strategy
        if effective_feature_method is not UNSET:
            field_dict["effective_feature_method"] = effective_feature_method
        if enrich_source is not UNSET:
            field_dict["enrich_source"] = enrich_source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agglomerative_params import AgglomerativeParams
        from ..models.dbscan_params import DBSCANParams
        from ..models.gaussian_mixture_params import GaussianMixtureParams
        from ..models.hdbscan_params import HDBSCANParams
        from ..models.k_means_params import KMeansParams
        from ..models.mean_shift_params import MeanShiftParams
        from ..models.optics_params import OPTICSParams
        from ..models.spectral_params import SpectralParams
        from ..models.vector_based_config_algorithm_params_type_8 import VectorBasedConfigAlgorithmParamsType8
        from ..models.vector_based_config_dbscan_parameters_type_1 import VectorBasedConfigDbscanParametersType1
        from ..models.vector_based_config_feature_weights_type_0 import VectorBasedConfigFeatureWeightsType0
        from ..models.vector_based_config_hdbscan_parameters_type_1 import VectorBasedConfigHdbscanParametersType1
        from ..models.vector_based_config_kmeans_parameters_type_1 import VectorBasedConfigKmeansParametersType1
        from ..models.weight_learning_config import WeightLearningConfig

        d = dict(src_dict)
        clustering_method = ClusteringAlgorithm(d.pop("clustering_method"))

        def _parse_feature_uri(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        feature_uri = _parse_feature_uri(d.pop("feature_uri", UNSET))

        def _parse_feature_uris(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                feature_uris_type_0 = cast(list[str], data)

                return feature_uris_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        feature_uris = _parse_feature_uris(d.pop("feature_uris", UNSET))

        def _parse_feature_extractor_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        feature_extractor_name = _parse_feature_extractor_name(d.pop("feature_extractor_name", UNSET))

        def _parse_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

        def _parse_output_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        output_name = _parse_output_name(d.pop("output_name", UNSET))

        def _parse_sample_size(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sample_size = _parse_sample_size(d.pop("sample_size", UNSET))

        def _parse_kmeans_parameters(
            data: object,
        ) -> KMeansParams | None | Unset | VectorBasedConfigKmeansParametersType1:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                kmeans_parameters_type_0 = KMeansParams.from_dict(data)

                return kmeans_parameters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                kmeans_parameters_type_1 = VectorBasedConfigKmeansParametersType1.from_dict(data)

                return kmeans_parameters_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(KMeansParams | None | Unset | VectorBasedConfigKmeansParametersType1, data)

        kmeans_parameters = _parse_kmeans_parameters(d.pop("kmeans_parameters", UNSET))

        def _parse_dbscan_parameters(
            data: object,
        ) -> DBSCANParams | None | Unset | VectorBasedConfigDbscanParametersType1:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                dbscan_parameters_type_0 = DBSCANParams.from_dict(data)

                return dbscan_parameters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                dbscan_parameters_type_1 = VectorBasedConfigDbscanParametersType1.from_dict(data)

                return dbscan_parameters_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DBSCANParams | None | Unset | VectorBasedConfigDbscanParametersType1, data)

        dbscan_parameters = _parse_dbscan_parameters(d.pop("dbscan_parameters", UNSET))

        def _parse_hdbscan_parameters(
            data: object,
        ) -> HDBSCANParams | None | Unset | VectorBasedConfigHdbscanParametersType1:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                hdbscan_parameters_type_0 = HDBSCANParams.from_dict(data)

                return hdbscan_parameters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                hdbscan_parameters_type_1 = VectorBasedConfigHdbscanParametersType1.from_dict(data)

                return hdbscan_parameters_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HDBSCANParams | None | Unset | VectorBasedConfigHdbscanParametersType1, data)

        hdbscan_parameters = _parse_hdbscan_parameters(d.pop("hdbscan_parameters", UNSET))

        def _parse_algorithm_params(
            data: object,
        ) -> (
            AgglomerativeParams
            | DBSCANParams
            | GaussianMixtureParams
            | HDBSCANParams
            | KMeansParams
            | MeanShiftParams
            | None
            | OPTICSParams
            | SpectralParams
            | Unset
            | VectorBasedConfigAlgorithmParamsType8
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                algorithm_params_type_0 = KMeansParams.from_dict(data)

                return algorithm_params_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                algorithm_params_type_1 = DBSCANParams.from_dict(data)

                return algorithm_params_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                algorithm_params_type_2 = HDBSCANParams.from_dict(data)

                return algorithm_params_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                algorithm_params_type_3 = AgglomerativeParams.from_dict(data)

                return algorithm_params_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                algorithm_params_type_4 = SpectralParams.from_dict(data)

                return algorithm_params_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                algorithm_params_type_5 = GaussianMixtureParams.from_dict(data)

                return algorithm_params_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                algorithm_params_type_6 = MeanShiftParams.from_dict(data)

                return algorithm_params_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                algorithm_params_type_7 = OPTICSParams.from_dict(data)

                return algorithm_params_type_7
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                algorithm_params_type_8 = VectorBasedConfigAlgorithmParamsType8.from_dict(data)

                return algorithm_params_type_8
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                AgglomerativeParams
                | DBSCANParams
                | GaussianMixtureParams
                | HDBSCANParams
                | KMeansParams
                | MeanShiftParams
                | None
                | OPTICSParams
                | SpectralParams
                | Unset
                | VectorBasedConfigAlgorithmParamsType8,
                data,
            )

        algorithm_params = _parse_algorithm_params(d.pop("algorithm_params", UNSET))

        _multi_feature_strategy = d.pop("multi_feature_strategy", UNSET)
        multi_feature_strategy: VectorBasedConfigMultiFeatureStrategy | Unset
        if isinstance(_multi_feature_strategy, Unset):
            multi_feature_strategy = UNSET
        else:
            multi_feature_strategy = VectorBasedConfigMultiFeatureStrategy(_multi_feature_strategy)

        normalize_features = d.pop("normalize_features", UNSET)

        def _parse_feature_weights(data: object) -> None | Unset | VectorBasedConfigFeatureWeightsType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                feature_weights_type_0 = VectorBasedConfigFeatureWeightsType0.from_dict(data)

                return feature_weights_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | VectorBasedConfigFeatureWeightsType0, data)

        feature_weights = _parse_feature_weights(d.pop("feature_weights", UNSET))

        def _parse_weight_learning_config(data: object) -> None | Unset | WeightLearningConfig:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                weight_learning_config_type_0 = WeightLearningConfig.from_dict(data)

                return weight_learning_config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | WeightLearningConfig, data)

        weight_learning_config = _parse_weight_learning_config(d.pop("weight_learning_config", UNSET))

        _output_strategy = d.pop("output_strategy", UNSET)
        output_strategy: VectorBasedConfigOutputStrategy | Unset
        if isinstance(_output_strategy, Unset):
            output_strategy = UNSET
        else:
            output_strategy = VectorBasedConfigOutputStrategy(_output_strategy)

        _effective_feature_method = d.pop("effective_feature_method", UNSET)
        effective_feature_method: VectorBasedConfigEffectiveFeatureMethod | Unset
        if isinstance(_effective_feature_method, Unset):
            effective_feature_method = UNSET
        else:
            effective_feature_method = VectorBasedConfigEffectiveFeatureMethod(_effective_feature_method)

        enrich_source = d.pop("enrich_source", UNSET)

        vector_based_config = cls(
            clustering_method=clustering_method,
            feature_uri=feature_uri,
            feature_uris=feature_uris,
            feature_extractor_name=feature_extractor_name,
            version=version,
            output_name=output_name,
            sample_size=sample_size,
            kmeans_parameters=kmeans_parameters,
            dbscan_parameters=dbscan_parameters,
            hdbscan_parameters=hdbscan_parameters,
            algorithm_params=algorithm_params,
            multi_feature_strategy=multi_feature_strategy,
            normalize_features=normalize_features,
            feature_weights=feature_weights,
            weight_learning_config=weight_learning_config,
            output_strategy=output_strategy,
            effective_feature_method=effective_feature_method,
            enrich_source=enrich_source,
        )

        vector_based_config.additional_properties = d
        return vector_based_config

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
