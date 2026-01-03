# CreateBatchRequest

Request model for creating a new batch.  Batches group bucket objects for processing into collections. When you submit a batch, all objects in the batch are processed through the collections associated with the bucket.  - object_ids: REQUIRED. List of object IDs that exist in the bucket - Collections are auto-discovered from the bucket at batch creation time  Batch Processing Flow: 1. Create batch with object_ids → Batch created in DRAFT status, collections auto-discovered 2. Submit batch → Processing begins for discovered collections 3. Collections with collection sources (tier 2/3) are processed automatically 4. Processing happens in topological order based on collection dependencies  Examples:     Single object batch:     {\"object_ids\": [\"obj_123\"]}      Multiple objects batch:     {\"object_ids\": [\"obj_123\", \"obj_456\", \"obj_789\"]}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_ids** | **List[str]** | REQUIRED. List of object IDs to include in the batch. Objects must exist in the bucket where the batch is created. Minimum 1 object, no maximum limit. All objects will be processed when the batch is submitted. Collections with collection sources (decomposition trees) are processed automatically via DAG resolution - no need to create separate batches. | 

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


