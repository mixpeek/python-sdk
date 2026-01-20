# StageParamsCluster

Configuration for clustering documents from previous stage results.  Stage Category: REDUCE  Transformation: N documents → K clusters (where K < N typically)  Purpose: Dynamically clusters documents from the pipeline by their embeddings. Unlike group_by which groups by a pre-existing field, cluster discovers natural groupings in the data based on vector similarity.  Performance: Calls clustering inference service. Fast for typical retriever result sets (10-500 documents). For larger datasets, consider using pre-computed clusters with group_by instead.  When to Use:     - Discover themes/topics in search results     - Group semantically similar documents without pre-existing labels     - Analyze patterns in retrieved content     - \"Find the 3 main themes in these results\"     - Auto-categorize search results  When NOT to Use:     - When documents already have cluster/category labels (use group_by)     - For very large result sets (>1000 docs) - use pre-computed clusters     - When you need exact groupings (clustering is approximate)  Output Modes:     - \"clusters\": Returns K cluster summary documents with member lists     - \"labeled\": Returns original N documents with cluster_label added     - \"representatives\": Returns K representative documents (one per cluster)  Common Pipeline Position: FILTER → cluster (this stage) → ENRICH (summarize clusters)  Examples:     - \"Find 3 themes in 60 ads\" → cluster with n_clusters=3     - \"Group similar products\" → cluster with algorithm=hdbscan (auto K)     - \"Discover topics in articles\" → cluster with representatives output

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | **str** | Clustering algorithm to use:  - hdbscan: Auto-determines number of clusters, handles noise (DEFAULT, recommended) - kmeans: Fast, requires n_clusters, spherical clusters - dbscan: Density-based, handles noise, requires eps tuning - agglomerative: Hierarchical, good for nested structures - spectral: Graph-based, good for non-convex clusters - gaussian_mixture: Probabilistic, soft cluster assignments  Recommendation: Use &#39;hdbscan&#39; for exploratory analysis, &#39;kmeans&#39; when you know K. | [optional] [default to 'hdbscan']
**n_clusters** | **int** | Number of clusters to create. Required for kmeans, spectral, agglomerative, gaussian_mixture. Ignored for hdbscan and dbscan (auto-determined).  If not specified for algorithms that need it, auto-calculated as min(8, N/10).  Typical values: 3-5 for theme discovery, 5-10 for topic modeling, 10-20 for fine-grained categorization. | [optional] [default to null]
**min_cluster_size** | **int** | Minimum number of documents to form a cluster (HDBSCAN/DBSCAN only).  Lower values &#x3D; more clusters, may include noise. Higher values &#x3D; fewer, denser clusters.  Auto-adjusted for small datasets: min(min_cluster_size, N/3). Typical values: 3-5 for small results, 10-20 for large results. | [optional] [default to 5]
**feature_uri** | **str** | Feature URI specifying which embedding to cluster on.  OPTIONAL - if not provided, auto-detects from the upstream feature_search stage. When a feature_search stage runs before cluster, its feature_uri is automatically tracked in the pipeline state and used for clustering.  Use the mixpeek:// URI format:   mixpeek://{extractor}@{version}/{output}  Examples: - &#39;mixpeek://multimodal_extractor@v1/vertex_multimodal_embedding&#39; - &#39;mixpeek://text_extractor@v1/multilingual_e5_large_instruct_v1&#39; - &#39;mixpeek://clip_extractor@v1/image_embedding&#39;  The feature_uri is resolved to the actual embedding field name on the documents (e.g., &#39;multimodal_extractor_v1_multimodal_embedding&#39;).  Only specify explicitly if you want to cluster on a different embedding than the one used in the feature_search stage. | [optional] [default to 'null']
**output_mode** | **str** | How to format the output:  - &#39;clusters&#39;: Returns K cluster documents, each containing:   - cluster_id: Cluster identifier   - member_count: Number of documents in cluster   - members: List of member documents   - centroid: Cluster center vector   Use for: Theme analysis, cluster summaries  - &#39;labeled&#39;: Returns original N documents with added fields:   - cluster_id: Assigned cluster   - cluster_score: Distance to centroid (lower &#x3D; closer)   Use for: Downstream processing with cluster context  - &#39;representatives&#39;: Returns K documents (one per cluster):   - The document closest to each cluster centroid   Use for: Quick sampling, representative examples | [optional] [default to 'clusters']
**include_centroids** | **bool** | Whether to include centroid vectors in output. Useful for downstream similarity comparisons or visualization. Set to False to reduce response size. | [optional] [default to True]
**max_members_per_cluster** | **int** | Maximum members to include per cluster in &#39;clusters&#39; output mode. Documents are sorted by distance to centroid (closest first). Use to limit response size for large result sets. | [optional] [default to 50]

## Example

```python
from mixpeek.models.stage_params_cluster import StageParamsCluster

# TODO update the JSON string below
json = "{}"
# create an instance of StageParamsCluster from a JSON string
stage_params_cluster_instance = StageParamsCluster.from_json(json)
# print the JSON string representation of the object
print(StageParamsCluster.to_json())

# convert the object into a dict
stage_params_cluster_dict = stage_params_cluster_instance.to_dict()
# create an instance of StageParamsCluster from a dict
stage_params_cluster_from_dict = StageParamsCluster.from_dict(stage_params_cluster_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


