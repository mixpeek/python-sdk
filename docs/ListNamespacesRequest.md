# ListNamespacesRequest

Request schema for listing namespaces.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | **Dict[str, object]** | Optional filters to apply to the namespace list. | [optional] 
**sort** | **Dict[str, object]** | Optional sort criteria for the namespace list. | [optional] 
**search** | **str** | Search term for wildcard search across all text fields. | [optional] 
**case_sensitive** | **bool** | If True, filters and search will be case-sensitive | [optional] [default to False]

## Example

```python
from mixpeek.models.list_namespaces_request import ListNamespacesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListNamespacesRequest from a JSON string
list_namespaces_request_instance = ListNamespacesRequest.from_json(json)
# print the JSON string representation of the object
print(ListNamespacesRequest.to_json())

# convert the object into a dict
list_namespaces_request_dict = list_namespaces_request_instance.to_dict()
# create an instance of ListNamespacesRequest from a dict
list_namespaces_request_from_dict = ListNamespacesRequest.from_dict(list_namespaces_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


