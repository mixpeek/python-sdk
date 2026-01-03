# CreateObjectsBatchResponse

Response model for batch object creation with partial success support.  This endpoint uses partial success: valid objects are created even if some fail. Failed objects are tracked separately so users can fix and retry them.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**succeeded** | [**List[ObjectResponse]**](ObjectResponse.md) | List of successfully created objects | 
**failed** | [**List[FailedObjectError]**](FailedObjectError.md) | List of objects that failed to create with error details | 
**total_requested** | **int** | Total number of objects in the batch request | 
**succeeded_count** | **int** | Number of objects successfully created | 
**failed_count** | **int** | Number of objects that failed | 

## Example

```python
from mixpeek.models.create_objects_batch_response import CreateObjectsBatchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateObjectsBatchResponse from a JSON string
create_objects_batch_response_instance = CreateObjectsBatchResponse.from_json(json)
# print the JSON string representation of the object
print(CreateObjectsBatchResponse.to_json())

# convert the object into a dict
create_objects_batch_response_dict = create_objects_batch_response_instance.to_dict()
# create an instance of CreateObjectsBatchResponse from a dict
create_objects_batch_response_from_dict = CreateObjectsBatchResponse.from_dict(create_objects_batch_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


