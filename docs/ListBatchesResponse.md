# ListBatchesResponse

The response model for listing batches.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batches** | [**List[BatchModel]**](BatchModel.md) | A list of batches. | 
**total_count** | **int** | The total number of batches found. | 

## Example

```python
from mixpeek.models.list_batches_response import ListBatchesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListBatchesResponse from a JSON string
list_batches_response_instance = ListBatchesResponse.from_json(json)
# print the JSON string representation of the object
print(ListBatchesResponse.to_json())

# convert the object into a dict
list_batches_response_dict = list_batches_response_instance.to_dict()
# create an instance of ListBatchesResponse from a dict
list_batches_response_from_dict = ListBatchesResponse.from_dict(list_batches_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


