# ClusterListStats

Aggregate statistics for a list of clusters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_clusters** | **int** | Total number of clusters in the result | [optional] [default to 0]
**total_documents** | **int** | Total number of documents across all clusters | [optional] [default to 0]
**avg_documents_per_cluster** | **float** | Average number of documents per cluster | [optional] [default to 0.0]
**clusters_by_status** | **Dict[str, int]** | Count of clusters grouped by status | [optional] 

## Example

```python
from mixpeek.models.cluster_list_stats import ClusterListStats

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterListStats from a JSON string
cluster_list_stats_instance = ClusterListStats.from_json(json)
# print the JSON string representation of the object
print(ClusterListStats.to_json())

# convert the object into a dict
cluster_list_stats_dict = cluster_list_stats_instance.to_dict()
# create an instance of ClusterListStats from a dict
cluster_list_stats_from_dict = ClusterListStats.from_dict(cluster_list_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


