# ListClustersRequest

Request model for listing clusters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**LogicalOperatorInput**](LogicalOperatorInput.md) | Filters to apply when listing clusters | [optional] 
**sort** | [**SortOption**](SortOption.md) | Sort options for the results | [optional] 
**search** | **str** | Search term for wildcard search across cluster_id, cluster_name, description, and other text fields | [optional] 

## Example

```python
from mixpeek.models.list_clusters_request import ListClustersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListClustersRequest from a JSON string
list_clusters_request_instance = ListClustersRequest.from_json(json)
# print the JSON string representation of the object
print(ListClustersRequest.to_json())

# convert the object into a dict
list_clusters_request_dict = list_clusters_request_instance.to_dict()
# create an instance of ListClustersRequest from a dict
list_clusters_request_from_dict = ListClustersRequest.from_dict(list_clusters_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


