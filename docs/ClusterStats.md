# ClusterStats

Basic clustering quality metrics.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_clusters** | **int** |  | 
**noise_points** | **int** |  | 
**silhouette_score** | **float** |  | 
**extra** | **Dict[str, object]** |  | [optional] 

## Example

```python
from mixpeek.models.cluster_stats import ClusterStats

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterStats from a JSON string
cluster_stats_instance = ClusterStats.from_json(json)
# print the JSON string representation of the object
print(ClusterStats.to_json())

# convert the object into a dict
cluster_stats_dict = cluster_stats_instance.to_dict()
# create an instance of ClusterStats from a dict
cluster_stats_from_dict = ClusterStats.from_dict(cluster_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


