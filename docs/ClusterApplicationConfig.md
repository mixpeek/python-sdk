# ClusterApplicationConfig

Configuration for automatic cluster execution on collection.  Similar to TaxonomyApplicationConfig, this attaches a cluster to a collection and defines when/how it should be automatically executed.  Used in CollectionModel.cluster_applications field.  Supports execution phase ordering for unified post-processing with taxonomies, clusters, and alerts.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **str** | ID of the cluster to execute (must exist and use this collection as input) | 
**auto_execute_on_batch** | **bool** | Automatically execute cluster when batch processing completes for this collection. If False, cluster must be executed manually via API. | [optional] [default to True]
**min_document_threshold** | **int** | Minimum number of documents required before executing cluster. If document_count &lt; threshold, clustering is skipped. Useful to avoid clustering on small datasets. | [optional] 
**cooldown_seconds** | **int** | Minimum time (in seconds) between automatic cluster executions. Prevents excessive re-clustering on frequent batch completions. Default: 3600 seconds (1 hour). | [optional] [default to 3600]
**execution_phase** | **int** | Which phase this cluster runs in. Default: 2 (CLUSTER phase, after taxonomies). Valid values: 1&#x3D;TAXONOMY, 2&#x3D;CLUSTER, 3&#x3D;ALERT. Lower phases run earlier. | [optional] [default to 2]
**priority** | **int** | Priority within the execution phase (higher &#x3D; runs first) | [optional] [default to 0]

## Example

```python
from mixpeek.models.cluster_application_config import ClusterApplicationConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterApplicationConfig from a JSON string
cluster_application_config_instance = ClusterApplicationConfig.from_json(json)
# print the JSON string representation of the object
print(ClusterApplicationConfig.to_json())

# convert the object into a dict
cluster_application_config_dict = cluster_application_config_instance.to_dict()
# create an instance of ClusterApplicationConfig from a dict
cluster_application_config_from_dict = ClusterApplicationConfig.from_dict(cluster_application_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


