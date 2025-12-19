# BatchModel

The base model for a batch.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_id** | **str** | The unique identifier of the batch. | [optional] 
**bucket_id** | **str** | The unique identifier of the bucket. | 
**status** | [**TaskStatusEnum**](TaskStatusEnum.md) | The current status of the batch. | [optional] 
**object_ids** | **List[str]** | A list of object IDs included in the batch. | [optional] 
**collection_ids** | **List[str]** | A list of collection IDs that this batch is connected to for processing. | [optional] 
**error** | **str** | The error message if the batch failed to process. | [optional] 
**type** | [**BatchType**](BatchType.md) | The type of the batch. | [optional] 
**manifest_key** | **str** | The S3 manifest key for the batch. | [optional] 
**task_id** | **str** | The task ID of the batch. | [optional] 
**loaded_object_ids** | **List[str]** | A list of object IDs that were successfully loaded into the batch. | [optional] 
**internal_metadata** | **Dict[str, object]** | Internal engine/job metadata (e.g., job_id for provider). | [optional] 

## Example

```python
from mixpeek.models.batch_model import BatchModel

# TODO update the JSON string below
json = "{}"
# create an instance of BatchModel from a JSON string
batch_model_instance = BatchModel.from_json(json)
# print the JSON string representation of the object
print(BatchModel.to_json())

# convert the object into a dict
batch_model_dict = batch_model_instance.to_dict()
# create an instance of BatchModel from a dict
batch_model_from_dict = BatchModel.from_dict(batch_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


