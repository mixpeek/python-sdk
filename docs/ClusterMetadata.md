# ClusterMetadata

Cluster job metadata stored in MongoDB clusters collection.  This is separate from cluster documents themselves. Tracks job-level configuration, status, and summary statistics.  Supports both vector and attribute clustering with appropriate metadata.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **str** | Unique cluster job identifier | [optional] 
**cluster_name** | **str** | Human-readable cluster name | 
**namespace_id** | **str** | Namespace this cluster belongs to | 
**input_collections** | **List[str]** | Source collection IDs that were clustered | 
**source_bucket_ids** | **List[str]** | Source bucket IDs that the input collections originated from. Enables bucket lineage tracking. | [optional] 
**filters** | **Dict[str, object]** | Optional filters that were applied to pre-filter documents before clustering | [optional] 
**cluster_type** | **str** | Type of clustering: vector (embedding-based) or attribute (metadata-based) | 
**feature_uris** | **List[str]** | Feature URIs that were clustered (mixpeek://{extractor}@{version}/{output}). Only for vector clustering. | [optional] 
**multi_feature_strategy** | **str** | Strategy used if multiple features (concatenate/independent/weighted). Only for vector clustering. | [optional] 
**learned_weights** | **Dict[str, float]** | Automatically learned feature weights (when multi_feature_strategy&#x3D;&#39;weighted&#39;). Keys are feature URIs, values are learned weights. Only populated after clustering execution completes. | [optional] 
**learning_quality_score** | **float** | Clustering quality score from weight learning (e.g., silhouette score). Only populated when multi_feature_strategy&#x3D;&#39;weighted&#39; and weights were learned. | [optional] 
**effective_feature_method** | **str** | Method for calculating cluster centroids (mean/median/medoid). Only for vector clustering. | [optional] 
**clustered_attributes** | **List[str]** | Attribute field names that were clustered. Only for attribute clustering. | [optional] 
**hierarchical_grouping** | **bool** | Whether hierarchical clustering was used. Only for attribute clustering. | [optional] 
**aggregation_method** | **str** | Method for aggregating attributes (most_frequent/first/last). Only for attribute clustering. | [optional] 
**output_collection_ids** | **List[str]** | Collection IDs where cluster documents are stored. For single output: list with one collection ID. For per-feature output: list with one collection ID per feature. | [optional] 
**output_collection_names** | **List[str]** | Names of output collections. Corresponds to output_collection_ids. | [optional] 
**algorithm** | **str** | Clustering algorithm used (hdbscan, kmeans, attribute_based, etc.) | [optional] 
**algorithm_params** | **Dict[str, object]** | Algorithm-specific parameters (not used for attribute_based) | [optional] 
**enrich_source** | **bool** | Whether source documents were enriched with cluster_id | [optional] [default to False]
**source_enrichment_config** | [**SourceEnrichmentConfig**](SourceEnrichmentConfig.md) | Configuration for source enrichment (if enrich_source&#x3D;True) | [optional] 
**llm_labeling** | [**LLMLabelingOutput**](LLMLabelingOutput.md) | Configuration for LLM-based cluster labeling (applies to all cluster types) | [optional] 
**num_clusters** | **int** | Number of clusters found (excludes noise/outliers, populated after execution) | [optional] 
**num_documents_clustered** | **int** | Total documents processed | [optional] 
**execution_time_seconds** | **float** | Time taken to complete clustering | [optional] 
**hierarchy_detected** | **bool** | Whether implicit hierarchy was detected (multi-feature independent) or created (hierarchical attributes) | [optional] [default to False]
**parent_cluster_id** | **str** | For child clusters in hierarchy | [optional] 
**child_cluster_ids** | **List[str]** | For parent clusters | [optional] 
**hierarchy_relationships** | **List[Dict[str, object]]** | Parent-child relationships detected from cluster membership overlap | [optional] 
**status** | [**TaskStatusEnum**](TaskStatusEnum.md) | Cluster job status (propagated from TaskService) | [optional] 
**last_execution_task_id** | **str** | Most recent task ID for this cluster | [optional] 
**created_at** | **datetime** | When cluster was created | [optional] 
**updated_at** | **datetime** | When cluster was last updated | [optional] 
**last_executed_at** | **datetime** | Last execution timestamp | [optional] 
**completed_at** | **datetime** | When clustering completed successfully | [optional] 
**llm_labeling_errors** | **List[str]** | List of errors encountered during LLM labeling (if any). Stored in MongoDB cluster metadata only, NOT in Qdrant cluster documents. Used to track LLM failures while allowing fallback labels to work. | [optional] 
**metadata** | **Dict[str, object]** | Additional user-defined metadata | [optional] 

## Example

```python
from mixpeek.models.cluster_metadata import ClusterMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterMetadata from a JSON string
cluster_metadata_instance = ClusterMetadata.from_json(json)
# print the JSON string representation of the object
print(ClusterMetadata.to_json())

# convert the object into a dict
cluster_metadata_dict = cluster_metadata_instance.to_dict()
# create an instance of ClusterMetadata from a dict
cluster_metadata_from_dict = ClusterMetadata.from_dict(cluster_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


