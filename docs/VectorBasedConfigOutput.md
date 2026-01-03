# VectorBasedConfigOutput

Configuration for vector-based clustering.  Use canonical feature URIs to specify which vector embeddings to cluster. Feature URIs follow the format: mixpeek://{extractor}@{version}/{output}  Supports both single and multi-feature clustering: - Single feature: Provide one feature_uri for standard clustering - Multi-feature: Provide multiple feature_uris for hybrid clustering  Examples:     Single feature:     {         \"feature_uri\": \"mixpeek://multimodal_extractor@v1/vertex_multimodal_embedding\",         \"clustering_method\": \"hdbscan\",         \"sample_size\": 1000     }      Multi-feature:     {         \"feature_uris\": [             \"mixpeek://text_extractor@v1/multilingual_e5_large_instruct_v1\",             \"mixpeek://image_extractor@v1/embedding\"         ],         \"clustering_method\": \"hdbscan\",         \"multi_feature_strategy\": \"concatenate\"     }

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_uri** | **str** | DEPRECATED: Use feature_uris instead. Canonical feature URI for the vector embedding to cluster. Format: &#39;mixpeek://{extractor}@{version}/{output}&#39;. For multi-feature clustering, use feature_uris (plural) instead. | [optional] 
**feature_uris** | **List[str]** | RECOMMENDED. List of feature URIs to cluster. Format: &#39;mixpeek://{extractor}@{version}/{output}&#39;. For single-feature clustering, provide a list with one element. For multi-feature clustering, provide multiple feature URIs. Each feature must exist in all input collections. | [optional] 
**clustering_method** | [**ClusteringAlgorithm**](ClusteringAlgorithm.md) | Clustering algorithm to use | 
**sample_size** | **int** | Number of samples to use for clustering | [optional] 
**kmeans_parameters** | [**KmeansParameters**](KmeansParameters.md) |  | [optional] 
**dbscan_parameters** | [**DbscanParameters**](DbscanParameters.md) |  | [optional] 
**hdbscan_parameters** | [**HdbscanParameters**](HdbscanParameters.md) |  | [optional] 
**algorithm_params** | [**AlgorithmParams**](AlgorithmParams.md) |  | [optional] 
**multi_feature_strategy** | **str** | Strategy for handling multiple feature vectors: - concatenate: Combine embeddings into one vector, single clustering - independent: Run separate clustering per feature - weighted: Learn optimal feature weights | [optional] [default to 'concatenate']
**normalize_features** | **bool** | Apply L2 normalization to each feature block before concatenation. Prevents feature dominance when combining different modalities. Only applies when multi_feature_strategy&#x3D;&#39;concatenate&#39;. | [optional] [default to True]
**feature_weights** | **Dict[str, float]** | Optional per-feature weights (0.0-1.0) for concatenation strategy. Keys are feature URIs, values are weights. Example: {&#39;mixpeek://text@v1/emb&#39;: 0.7, &#39;mixpeek://image@v1/emb&#39;: 0.3}. Defaults to equal weights (1.0) if not specified. Only applies when multi_feature_strategy&#x3D;&#39;concatenate&#39;. If multi_feature_strategy&#x3D;&#39;weighted&#39; and this is None, weights are learned automatically using weight_learning_config. | [optional] 
**weight_learning_config** | [**WeightLearningConfig**](WeightLearningConfig.md) | Configuration for automatic feature weight learning. Only used when multi_feature_strategy&#x3D;&#39;weighted&#39; and feature_weights is None. If feature_weights is provided, manual weights are used instead of learning. If this is None when learning is needed, default WeightLearningConfig is used. | [optional] 
**output_strategy** | **str** | Output collection creation strategy: - single: Create one collection with all feature vectors - per_feature: Create separate collections for each feature (for hierarchical taxonomies) | [optional] [default to 'single']
**effective_feature_method** | **str** | Method for calculating cluster centroids: - mean: Average of all vectors in cluster - median: Median vector (robust to outliers) - medoid: Actual cluster member closest to centroid | [optional] [default to 'mean']
**enrich_source** | **bool** | Whether to enrich source documents with cluster_id | [optional] [default to False]

## Example

```python
from mixpeek.models.vector_based_config_output import VectorBasedConfigOutput

# TODO update the JSON string below
json = "{}"
# create an instance of VectorBasedConfigOutput from a JSON string
vector_based_config_output_instance = VectorBasedConfigOutput.from_json(json)
# print the JSON string representation of the object
print(VectorBasedConfigOutput.to_json())

# convert the object into a dict
vector_based_config_output_dict = vector_based_config_output_instance.to_dict()
# create an instance of VectorBasedConfigOutput from a dict
vector_based_config_output_from_dict = VectorBasedConfigOutput.from_dict(vector_based_config_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


