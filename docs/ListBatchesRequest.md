# ListBatchesRequest

The request model for listing batches.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**TaskStatusEnum**](TaskStatusEnum.md) | Filter batches by status. | [optional] 
**offset** | **int** | The number of batches to skip. | [optional] [default to 0]
**limit** | **int** | The maximum number of batches to return. | [optional] [default to 100]

## Example

```python
from mixpeek.models.list_batches_request import ListBatchesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListBatchesRequest from a JSON string
list_batches_request_instance = ListBatchesRequest.from_json(json)
# print the JSON string representation of the object
print(ListBatchesRequest.to_json())

# convert the object into a dict
list_batches_request_dict = list_batches_request_instance.to_dict()
# create an instance of ListBatchesRequest from a dict
list_batches_request_from_dict = ListBatchesRequest.from_dict(list_batches_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


