from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cluster_config_algorithm import ClusterConfigAlgorithm
from ..models.cluster_config_output_mode import ClusterConfigOutputMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="ClusterConfig")


@_attrs_define
class ClusterConfig:
    """Configuration for clustering documents from previous stage results.

    Stage Category: REDUCE

    Transformation: N documents → K clusters (where K < N typically)

    Purpose: Dynamically clusters documents from the pipeline by their embeddings.
    Unlike group_by which groups by a pre-existing field, cluster discovers
    natural groupings in the data based on vector similarity.

    Performance: Calls clustering inference service. Fast for typical retriever
    result sets (10-500 documents). For larger datasets, consider using
    pre-computed clusters with group_by instead.

    When to Use:
        - Discover themes/topics in search results
        - Group semantically similar documents without pre-existing labels
        - Analyze patterns in retrieved content
        - "Find the 3 main themes in these results"
        - Auto-categorize search results

    When NOT to Use:
        - When documents already have cluster/category labels (use group_by)
        - For very large result sets (>1000 docs) - use pre-computed clusters
        - When you need exact groupings (clustering is approximate)

    Output Modes:
        - "clusters": Returns K cluster summary documents with member lists
        - "labeled": Returns original N documents with cluster_label added
        - "representatives": Returns K representative documents (one per cluster)

    Common Pipeline Position: FILTER → cluster (this stage) → ENRICH (summarize clusters)

    Examples:
        - "Find 3 themes in 60 ads" → cluster with n_clusters=3
        - "Group similar products" → cluster with algorithm=hdbscan (auto K)
        - "Discover topics in articles" → cluster with representatives output

        Attributes:
            algorithm (ClusterConfigAlgorithm | Unset): Clustering algorithm to use:

                - hdbscan: Auto-determines number of clusters, handles noise (DEFAULT, recommended)
                - kmeans: Fast, requires n_clusters, spherical clusters
                - dbscan: Density-based, handles noise, requires eps tuning
                - agglomerative: Hierarchical, good for nested structures
                - spectral: Graph-based, good for non-convex clusters
                - gaussian_mixture: Probabilistic, soft cluster assignments

                Recommendation: Use 'hdbscan' for exploratory analysis, 'kmeans' when you know K. Default:
                ClusterConfigAlgorithm.HDBSCAN.
            n_clusters (int | None | Unset): Number of clusters to create. Required for kmeans, spectral, agglomerative,
                gaussian_mixture. Ignored for hdbscan and dbscan (auto-determined).

                If not specified for algorithms that need it, auto-calculated as min(8, N/10).

                Typical values: 3-5 for theme discovery, 5-10 for topic modeling, 10-20 for fine-grained categorization.
            min_cluster_size (int | Unset): Minimum number of documents to form a cluster (HDBSCAN/DBSCAN only).

                Lower values = more clusters, may include noise.
                Higher values = fewer, denser clusters.

                Auto-adjusted for small datasets: min(min_cluster_size, N/3).
                Typical values: 3-5 for small results, 10-20 for large results. Default: 5.
            feature_uri (None | str | Unset): Feature URI specifying which embedding to cluster on.

                OPTIONAL - if not provided, auto-detects from the upstream feature_search stage.
                When a feature_search stage runs before cluster, its feature_uri is automatically
                tracked in the pipeline state and used for clustering.

                Use the mixpeek:// URI format:
                  mixpeek://{extractor}@{version}/{output}

                Examples:
                - 'mixpeek://multimodal_extractor@v1/vertex_multimodal_embedding'
                - 'mixpeek://text_extractor@v1/multilingual_e5_large_instruct_v1'
                - 'mixpeek://clip_extractor@v1/image_embedding'

                The feature_uri is resolved to the actual embedding field name
                on the documents (e.g., 'multimodal_extractor_v1_multimodal_embedding').

                Only specify explicitly if you want to cluster on a different embedding
                than the one used in the feature_search stage.
            output_mode (ClusterConfigOutputMode | Unset): How to format the output:

                - 'clusters': Returns K cluster documents, each containing:
                  - cluster_id: Cluster identifier
                  - member_count: Number of documents in cluster
                  - members: List of member documents
                  - centroid: Cluster center vector
                  Use for: Theme analysis, cluster summaries

                - 'labeled': Returns original N documents with added fields:
                  - cluster_id: Assigned cluster
                  - cluster_score: Distance to centroid (lower = closer)
                  Use for: Downstream processing with cluster context

                - 'representatives': Returns K documents (one per cluster):
                  - The document closest to each cluster centroid
                  Use for: Quick sampling, representative examples Default: ClusterConfigOutputMode.CLUSTERS.
            include_centroids (bool | Unset): Whether to include centroid vectors in output.
                Useful for downstream similarity comparisons or visualization.
                Set to False to reduce response size. Default: True.
            max_members_per_cluster (int | Unset): Maximum members to include per cluster in 'clusters' output mode.
                Documents are sorted by distance to centroid (closest first).
                Use to limit response size for large result sets. Default: 50.
    """

    algorithm: ClusterConfigAlgorithm | Unset = ClusterConfigAlgorithm.HDBSCAN
    n_clusters: int | None | Unset = UNSET
    min_cluster_size: int | Unset = 5
    feature_uri: None | str | Unset = UNSET
    output_mode: ClusterConfigOutputMode | Unset = ClusterConfigOutputMode.CLUSTERS
    include_centroids: bool | Unset = True
    max_members_per_cluster: int | Unset = 50
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        algorithm: str | Unset = UNSET
        if not isinstance(self.algorithm, Unset):
            algorithm = self.algorithm.value

        n_clusters: int | None | Unset
        if isinstance(self.n_clusters, Unset):
            n_clusters = UNSET
        else:
            n_clusters = self.n_clusters

        min_cluster_size = self.min_cluster_size

        feature_uri: None | str | Unset
        if isinstance(self.feature_uri, Unset):
            feature_uri = UNSET
        else:
            feature_uri = self.feature_uri

        output_mode: str | Unset = UNSET
        if not isinstance(self.output_mode, Unset):
            output_mode = self.output_mode.value

        include_centroids = self.include_centroids

        max_members_per_cluster = self.max_members_per_cluster

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if algorithm is not UNSET:
            field_dict["algorithm"] = algorithm
        if n_clusters is not UNSET:
            field_dict["n_clusters"] = n_clusters
        if min_cluster_size is not UNSET:
            field_dict["min_cluster_size"] = min_cluster_size
        if feature_uri is not UNSET:
            field_dict["feature_uri"] = feature_uri
        if output_mode is not UNSET:
            field_dict["output_mode"] = output_mode
        if include_centroids is not UNSET:
            field_dict["include_centroids"] = include_centroids
        if max_members_per_cluster is not UNSET:
            field_dict["max_members_per_cluster"] = max_members_per_cluster

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _algorithm = d.pop("algorithm", UNSET)
        algorithm: ClusterConfigAlgorithm | Unset
        if isinstance(_algorithm, Unset):
            algorithm = UNSET
        else:
            algorithm = ClusterConfigAlgorithm(_algorithm)

        def _parse_n_clusters(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        n_clusters = _parse_n_clusters(d.pop("n_clusters", UNSET))

        min_cluster_size = d.pop("min_cluster_size", UNSET)

        def _parse_feature_uri(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        feature_uri = _parse_feature_uri(d.pop("feature_uri", UNSET))

        _output_mode = d.pop("output_mode", UNSET)
        output_mode: ClusterConfigOutputMode | Unset
        if isinstance(_output_mode, Unset):
            output_mode = UNSET
        else:
            output_mode = ClusterConfigOutputMode(_output_mode)

        include_centroids = d.pop("include_centroids", UNSET)

        max_members_per_cluster = d.pop("max_members_per_cluster", UNSET)

        cluster_config = cls(
            algorithm=algorithm,
            n_clusters=n_clusters,
            min_cluster_size=min_cluster_size,
            feature_uri=feature_uri,
            output_mode=output_mode,
            include_centroids=include_centroids,
            max_members_per_cluster=max_members_per_cluster,
        )

        cluster_config.additional_properties = d
        return cluster_config

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
