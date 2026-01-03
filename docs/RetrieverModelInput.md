# RetrieverModelInput

Retriever model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retriever_id** | **str** | Unique identifier for the retriever | [optional] 
**retriever_name** | **str** | Name of the retriever | 
**description** | **str** | Description of the retriever | [optional] 
**input_schema** | [**RetrieverSchema**](RetrieverSchema.md) | Input schema for the retriever | 
**collection_ids** | **List[str]** | List of collection IDs | 
**stages** | [**List[StageInstanceConfig]**](StageInstanceConfig.md) | List of stage configurations | 
**cache_config** | [**CacheConfig**](CacheConfig.md) | Cache configuration for this retriever. If not provided, caching is disabled. | [optional] 
**created_at** | **datetime** | When the retriever was created | [optional] 
**updated_at** | **datetime** | When the retriever was last modified | [optional] 
**last_executed_at** | **datetime** | When the retriever was last executed | [optional] 
**enabled** | **bool** | Whether the retriever is enabled (can be toggled on/off) | [optional] [default to True]
**status** | [**RetrieverStatus**](RetrieverStatus.md) | Current operational status | [optional] 
**usage_stats** | [**UsageStatistics**](UsageStatistics.md) | Usage and performance statistics | [optional] 
**collections** | [**List[CollectionDetail]**](CollectionDetail.md) | Expanded collection details with names and metadata | [optional] 
**metadata** | **Dict[str, object]** | Custom key-value metadata | [optional] 
**tags** | **List[str]** | Tags for organization and filtering | [optional] 
**created_by** | [**CreatorInfo**](CreatorInfo.md) | Information about who created this retriever | [optional] 
**updated_by** | [**CreatorInfo**](CreatorInfo.md) | Information about who last updated this retriever | [optional] 
**version** | **int** | Version number (increments on each update) | [optional] [default to 1]
**revision_history** | [**List[RevisionHistoryEntry]**](RevisionHistoryEntry.md) | History of changes (optional, last N changes) | [optional] 
**health** | [**HealthCheck**](HealthCheck.md) | Health status and diagnostics | [optional] 

## Example

```python
from mixpeek.models.retriever_model_input import RetrieverModelInput

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieverModelInput from a JSON string
retriever_model_input_instance = RetrieverModelInput.from_json(json)
# print the JSON string representation of the object
print(RetrieverModelInput.to_json())

# convert the object into a dict
retriever_model_input_dict = retriever_model_input_instance.to_dict()
# create an instance of RetrieverModelInput from a dict
retriever_model_input_from_dict = RetrieverModelInput.from_dict(retriever_model_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


