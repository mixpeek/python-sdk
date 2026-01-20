# TriggerExecutionConfig

Configuration for cluster execution when trigger fires.  Defines what clustering algorithm and parameters to use when the trigger executes.  Examples:     K-means clustering on 3 collections:         {             \"collection_ids\": [\"col_abc123\", \"col_def456\", \"col_ghi789\"],             \"config\": {                 \"algorithm\": \"kmeans\",                 \"n_clusters\": 5,                 \"min_cluster_size\": 2             }         }      HDBSCAN clustering on single collection:         {             \"collection_ids\": [\"col_products\"],             \"config\": {                 \"algorithm\": \"hdbscan\",                 \"min_cluster_size\": 10,                 \"min_samples\": 5             }         }

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_ids** | **List[str]** | REQUIRED. List of collection IDs to cluster when trigger fires. Must contain at least one collection ID. All collections will be clustered together using the specified algorithm. | 
**config** | **object** | REQUIRED. Clustering algorithm configuration. Must include &#39;algorithm&#39; field (&#39;kmeans&#39;, &#39;hdbscan&#39;, &#39;hierarchical&#39;). Additional fields depend on algorithm choice. K-means requires &#39;n_clusters&#39;. HDBSCAN requires &#39;min_cluster_size&#39;. | 

## Example

```python
from mixpeek.models.trigger_execution_config import TriggerExecutionConfig

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerExecutionConfig from a JSON string
trigger_execution_config_instance = TriggerExecutionConfig.from_json(json)
# print the JSON string representation of the object
print(TriggerExecutionConfig.to_json())

# convert the object into a dict
trigger_execution_config_dict = trigger_execution_config_instance.to_dict()
# create an instance of TriggerExecutionConfig from a dict
trigger_execution_config_from_dict = TriggerExecutionConfig.from_dict(trigger_execution_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


