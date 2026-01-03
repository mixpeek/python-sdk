# ClusterExecutionMetric

Single cluster execution metrics.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**execution_id** | **str** | Execution identifier | 
**started_at** | **datetime** | Execution start time | 
**duration_seconds** | **float** | Execution duration | 
**num_documents** | **int** | Number of documents clustered | 
**num_clusters** | **int** | Number of clusters created | 
**status** | **str** | Execution status | 
**algorithm** | **str** | Clustering algorithm used | 

## Example

```python
from mixpeek.models.cluster_execution_metric import ClusterExecutionMetric

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterExecutionMetric from a JSON string
cluster_execution_metric_instance = ClusterExecutionMetric.from_json(json)
# print the JSON string representation of the object
print(ClusterExecutionMetric.to_json())

# convert the object into a dict
cluster_execution_metric_dict = cluster_execution_metric_instance.to_dict()
# create an instance of ClusterExecutionMetric from a dict
cluster_execution_metric_from_dict = ClusterExecutionMetric.from_dict(cluster_execution_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


