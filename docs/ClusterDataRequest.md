# ClusterDataRequest

Request to stream cluster data from parquet files.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **str** | Cluster ID to fetch data for | [optional] 
**include_centroids** | **bool** | Include cluster centroids | [optional] [default to True]
**include_members** | **bool** | Include cluster members | [optional] [default to False]
**limit** | **int** | Limit number of records | [optional] 
**offset** | **int** | Offset for pagination | [optional] [default to 0]

## Example

```python
from mixpeek.models.cluster_data_request import ClusterDataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterDataRequest from a JSON string
cluster_data_request_instance = ClusterDataRequest.from_json(json)
# print the JSON string representation of the object
print(ClusterDataRequest.to_json())

# convert the object into a dict
cluster_data_request_dict = cluster_data_request_instance.to_dict()
# create an instance of ClusterDataRequest from a dict
cluster_data_request_from_dict = ClusterDataRequest.from_dict(cluster_data_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


