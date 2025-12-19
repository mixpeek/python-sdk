# StageInstanceConfigInput

User-provided configuration for a stage instance in a retriever pipeline.  This model is used when creating a retriever to define the specific parameters for each stage.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stage_name** | **str** |  | 
**version** | **str** |  | 
**parameters** | **Dict[str, object]** |  | 
**pre_filters** | [**LogicalOperatorInput**](LogicalOperatorInput.md) | Filters to apply to the documents *before* this stage is executed.These filters are combined with any global retriever filters. | [optional] 
**post_filters** | [**LogicalOperatorInput**](LogicalOperatorInput.md) | Filters to apply to the documents *after* this stage is executed.These filters are applied to the results of this stage before passing to the next. | [optional] 
**stats** | [**StagePerformance**](StagePerformance.md) | Performance statistics for this stage | [optional] 

## Example

```python
from mixpeek.models.stage_instance_config_input import StageInstanceConfigInput

# TODO update the JSON string below
json = "{}"
# create an instance of StageInstanceConfigInput from a JSON string
stage_instance_config_input_instance = StageInstanceConfigInput.from_json(json)
# print the JSON string representation of the object
print(StageInstanceConfigInput.to_json())

# convert the object into a dict
stage_instance_config_input_dict = stage_instance_config_input_instance.to_dict()
# create an instance of StageInstanceConfigInput from a dict
stage_instance_config_input_from_dict = StageInstanceConfigInput.from_dict(stage_instance_config_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


