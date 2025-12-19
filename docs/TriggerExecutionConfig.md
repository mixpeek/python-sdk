# TriggerExecutionConfig

Configuration for cluster execution when trigger fires.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_ids** | **List[str]** | Collections to cluster | 
**config** | **Dict[str, object]** | ClusteringConfig as dict | 

## Example

```python
from mixpeek.models.trigger_execution_config import TriggerExecutionConfig

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerExecutionConfig from a JSON string
trigger_execution_config_instance = TriggerExecutionConfig.from_json(json)
# print the JSON string representation of the object
print(TriggerExecutionConfig.to_json())

# convert the object into a dict
trigger_execution_config_dict = trigger_execution_config_instance.to_dict()
# create an instance of TriggerExecutionConfig from a dict
trigger_execution_config_from_dict = TriggerExecutionConfig.from_dict(trigger_execution_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


