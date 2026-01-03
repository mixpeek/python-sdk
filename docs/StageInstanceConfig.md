# StageInstanceConfig

User-provided configuration for a stage instance in a retriever pipeline.  This model is used when creating a retriever to define the specific parameters for each stage.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stage_name** | **str** |  | 
**stage_id** | **str** | Stage implementation ID (overrides stage_name for lookups) | [optional] 
**parameters** | **Dict[str, object]** | Stage parameters | [optional] 
**pre_filters** | [**LogicalOperatorInput**](LogicalOperatorInput.md) | Filters to apply to the documents *before* this stage is executed.These filters are combined with any global retriever filters. | [optional] 
**post_filters** | [**LogicalOperatorInput**](LogicalOperatorInput.md) | Filters to apply to the documents *after* this stage is executed.These filters are applied to the results of this stage before passing to the next. | [optional] 
**stats** | [**StagePerformanceInput**](StagePerformanceInput.md) | Performance statistics for this stage | [optional] 

## Example

```python
from mixpeek.models.stage_instance_config import StageInstanceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of StageInstanceConfig from a JSON string
stage_instance_config_instance = StageInstanceConfig.from_json(json)
# print the JSON string representation of the object
print(StageInstanceConfig.to_json())

# convert the object into a dict
stage_instance_config_dict = stage_instance_config_instance.to_dict()
# create an instance of StageInstanceConfig from a dict
stage_instance_config_from_dict = StageInstanceConfig.from_dict(stage_instance_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


