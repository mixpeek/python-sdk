# SlowOperation

Details of a slow operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** | When the operation occurred | 
**stage_name** | **str** | Stage name | 
**component** | **str** | Component | 
**latency_ms** | **float** | Operation latency | 
**metadata** | **Dict[str, object]** | Additional context from profiling | [optional] 

## Example

```python
from mixpeek.models.slow_operation import SlowOperation

# TODO update the JSON string below
json = "{}"
# create an instance of SlowOperation from a JSON string
slow_operation_instance = SlowOperation.from_json(json)
# print the JSON string representation of the object
print(SlowOperation.to_json())

# convert the object into a dict
slow_operation_dict = slow_operation_instance.to_dict()
# create an instance of SlowOperation from a dict
slow_operation_from_dict = SlowOperation.from_dict(slow_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


