# UpdateNamespaceRequest

Request schema for updating a namespace's payload indexes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**namespace_name** | **str** | Name of the namespace to update | [optional] 
**payload_indexes** | [**List[PayloadIndexConfigInput]**](PayloadIndexConfigInput.md) | Updated list of payload index configurations | [optional] 

## Example

```python
from mixpeek.models.update_namespace_request import UpdateNamespaceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateNamespaceRequest from a JSON string
update_namespace_request_instance = UpdateNamespaceRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateNamespaceRequest.to_json())

# convert the object into a dict
update_namespace_request_dict = update_namespace_request_instance.to_dict()
# create an instance of UpdateNamespaceRequest from a dict
update_namespace_request_from_dict = UpdateNamespaceRequest.from_dict(update_namespace_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


