# BatchConfirmResponse

Response from batch confirmation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** | Task ID for tracking batch confirmation progress | 
**status** | [**TaskStatusEnum**](TaskStatusEnum.md) | Task status | 
**confirmations_count** | **int** | Number of confirmations being processed | 
**task** | [**TaskResponse**](TaskResponse.md) | Full task details | 
**message** | **str** | Status message | [optional] [default to 'Batch confirmation is being processed in the background.']

## Example

```python
from mixpeek.models.batch_confirm_response import BatchConfirmResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BatchConfirmResponse from a JSON string
batch_confirm_response_instance = BatchConfirmResponse.from_json(json)
# print the JSON string representation of the object
print(BatchConfirmResponse.to_json())

# convert the object into a dict
batch_confirm_response_dict = batch_confirm_response_instance.to_dict()
# create an instance of BatchConfirmResponse from a dict
batch_confirm_response_from_dict = BatchConfirmResponse.from_dict(batch_confirm_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


