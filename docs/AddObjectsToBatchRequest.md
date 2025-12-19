# AddObjectsToBatchRequest

The request model for adding objects to an existing batch.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_ids** | **List[str]** | A list of object IDs to add to the batch. | 

## Example

```python
from mixpeek.models.add_objects_to_batch_request import AddObjectsToBatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddObjectsToBatchRequest from a JSON string
add_objects_to_batch_request_instance = AddObjectsToBatchRequest.from_json(json)
# print the JSON string representation of the object
print(AddObjectsToBatchRequest.to_json())

# convert the object into a dict
add_objects_to_batch_request_dict = add_objects_to_batch_request_instance.to_dict()
# create an instance of AddObjectsToBatchRequest from a dict
add_objects_to_batch_request_from_dict = AddObjectsToBatchRequest.from_dict(add_objects_to_batch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


