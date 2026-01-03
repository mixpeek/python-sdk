# ListObjectsRequest

Request model for listing objects in a bucket.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**LogicalOperatorInput**](LogicalOperatorInput.md) | Filters to apply to the object list | [optional] 
**sort** | [**SortOption**](SortOption.md) | Sort options for the object list | [optional] 
**search** | **str** | Search term to filter objects by key or metadata | [optional] 
**select** | **List[str]** | OPTIONAL. List of fields to include in the response. Supports dot notation for nested fields (e.g., &#39;metadata.title&#39;, &#39;status&#39;). When specified, only the selected fields will be returned in the object results, reducing response size. System fields like &#39;object_id&#39; and &#39;bucket_id&#39; are always included. Use this to optimize response size when working with large objects. | [optional] 

## Example

```python
from mixpeek.models.list_objects_request import ListObjectsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListObjectsRequest from a JSON string
list_objects_request_instance = ListObjectsRequest.from_json(json)
# print the JSON string representation of the object
print(ListObjectsRequest.to_json())

# convert the object into a dict
list_objects_request_dict = list_objects_request_instance.to_dict()
# create an instance of ListObjectsRequest from a dict
list_objects_request_from_dict = ListObjectsRequest.from_dict(list_objects_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


