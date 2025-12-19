# ClusterDataResponse

Response with cluster data from parquet.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **str** |  | 
**centroids** | [**List[ClusterCentroidData]**](ClusterCentroidData.md) |  | [optional] 
**members** | [**List[ClusterMemberData]**](ClusterMemberData.md) |  | [optional] 
**total_clusters** | **int** |  | 
**total_members** | **int** |  | 

## Example

```python
from mixpeek.models.cluster_data_response import ClusterDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterDataResponse from a JSON string
cluster_data_response_instance = ClusterDataResponse.from_json(json)
# print the JSON string representation of the object
print(ClusterDataResponse.to_json())

# convert the object into a dict
cluster_data_response_dict = cluster_data_response_instance.to_dict()
# create an instance of ClusterDataResponse from a dict
cluster_data_response_from_dict = ClusterDataResponse.from_dict(cluster_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


