# CreateObjectsBatchRequest

Request model for creating multiple bucket objects in a batch.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**List[CreateObjectRequest]**](CreateObjectRequest.md) | List of objects to be created in this batch. | 

## Example

```python
from mixpeek.models.create_objects_batch_request import CreateObjectsBatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateObjectsBatchRequest from a JSON string
create_objects_batch_request_instance = CreateObjectsBatchRequest.from_json(json)
# print the JSON string representation of the object
print(CreateObjectsBatchRequest.to_json())

# convert the object into a dict
create_objects_batch_request_dict = create_objects_batch_request_instance.to_dict()
# create an instance of CreateObjectsBatchRequest from a dict
create_objects_batch_request_from_dict = CreateObjectsBatchRequest.from_dict(create_objects_batch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


