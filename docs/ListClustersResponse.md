# ListClustersResponse

Response model for listing clusters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[ClusterModel]**](ClusterModel.md) | List of cluster models | 
**pagination** | [**PaginationResponse**](PaginationResponse.md) | Pagination information | 

## Example

```python
from mixpeek.models.list_clusters_response import ListClustersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListClustersResponse from a JSON string
list_clusters_response_instance = ListClustersResponse.from_json(json)
# print the JSON string representation of the object
print(ListClustersResponse.to_json())

# convert the object into a dict
list_clusters_response_dict = list_clusters_response_instance.to_dict()
# create an instance of ListClustersResponse from a dict
list_clusters_response_from_dict = ListClustersResponse.from_dict(list_clusters_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


