# CreateBatchRequest

The request model for creating a new batch.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_ids** | **List[str]** | A list of object IDs to add to the batch. | 

## Example

```python
from mixpeek.models.create_batch_request import CreateBatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBatchRequest from a JSON string
create_batch_request_instance = CreateBatchRequest.from_json(json)
# print the JSON string representation of the object
print(CreateBatchRequest.to_json())

# convert the object into a dict
create_batch_request_dict = create_batch_request_instance.to_dict()
# create an instance of CreateBatchRequest from a dict
create_batch_request_from_dict = CreateBatchRequest.from_dict(create_batch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


