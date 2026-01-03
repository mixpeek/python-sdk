# TriggerCollectionResponse

Response after triggering collection processing.  Use `batch_id` or `task_id` to monitor progress via GET /v1/batches/{batch_id} or GET /v1/tasks/{task_id}.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_id** | **str** | ID of the created batch for tracking progress. | 
**task_id** | **str** | Task ID for monitoring via GET /v1/tasks/{task_id}. | 
**collection_id** | **str** | ID of the collection being processed. | 
**source_bucket_ids** | **List[str]** | Bucket IDs that objects were discovered from (bucket-sourced collections). | [optional] 
**source_collection_ids** | **List[str]** | Collection IDs that documents were read from (collection-sourced collections). | [optional] 
**object_count** | **int** | Total number of objects included in the batch (bucket-sourced collections). | [optional] 
**document_count** | **int** | Total number of documents to process (collection-sourced collections). | [optional] 
**total_tiers** | **int** | Number of processing tiers in the DAG. | 
**message** | **str** | Human-readable status message. | 

## Example

```python
from mixpeek.models.trigger_collection_response import TriggerCollectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerCollectionResponse from a JSON string
trigger_collection_response_instance = TriggerCollectionResponse.from_json(json)
# print the JSON string representation of the object
print(TriggerCollectionResponse.to_json())

# convert the object into a dict
trigger_collection_response_dict = trigger_collection_response_instance.to_dict()
# create an instance of TriggerCollectionResponse from a dict
trigger_collection_response_from_dict = TriggerCollectionResponse.from_dict(trigger_collection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


