# TriggerExecutionHistoryItem

Single execution history item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** | Job ID | 
**triggered_at** | **datetime** | When trigger fired | 
**status** | **str** | Execution status | 
**execution_time_ms** | **int** | Execution time in milliseconds | [optional] 
**error** | **str** | Error message if failed | [optional] 
**num_clusters** | **int** | Number of clusters created | [optional] 
**num_documents** | **int** | Number of documents processed | [optional] 

## Example

```python
from mixpeek.models.trigger_execution_history_item import TriggerExecutionHistoryItem

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerExecutionHistoryItem from a JSON string
trigger_execution_history_item_instance = TriggerExecutionHistoryItem.from_json(json)
# print the JSON string representation of the object
print(TriggerExecutionHistoryItem.to_json())

# convert the object into a dict
trigger_execution_history_item_dict = trigger_execution_history_item_instance.to_dict()
# create an instance of TriggerExecutionHistoryItem from a dict
trigger_execution_history_item_from_dict = TriggerExecutionHistoryItem.from_dict(trigger_execution_history_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


