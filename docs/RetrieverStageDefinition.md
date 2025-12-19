# RetrieverStageDefinition

Public definition of a retriever stage.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stage_name** | **str** | The unique name of the stage. | 
**version** | **str** | The version of the stage. | 
**description** | **str** | A description of what the stage does. | 
**parameter_schema** | **Dict[str, object]** | The schema for the parameters this stage accepts. | [optional] 

## Example

```python
from mixpeek.models.retriever_stage_definition import RetrieverStageDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieverStageDefinition from a JSON string
retriever_stage_definition_instance = RetrieverStageDefinition.from_json(json)
# print the JSON string representation of the object
print(RetrieverStageDefinition.to_json())

# convert the object into a dict
retriever_stage_definition_dict = retriever_stage_definition_instance.to_dict()
# create an instance of RetrieverStageDefinition from a dict
retriever_stage_definition_from_dict = RetrieverStageDefinition.from_dict(retriever_stage_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


