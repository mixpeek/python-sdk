# CloneRetrieverRequest

Request to clone a retriever with optional modifications.  **Purpose:** Cloning creates a NEW retriever (with new ID) based on an existing one, allowing you to make changes that aren't allowed via PATCH (stages, input_schema, collections). This is the recommended way to iterate on retriever designs.  **Clone vs Template vs Version:** - **Clone**: Copy THIS retriever and modify it (for iteration/fixes) - **Template**: Create retriever from a reusable pattern (for new projects) - **Version**: (Not implemented) - Use clone instead  **Use Cases:** - Fix a typo in a stage name without losing execution history - Add/remove stages while keeping the original intact - Change collections while preserving the original retriever - Test modifications before replacing production retriever - Create variants (e.g., \"strict\" vs \"relaxed\" versions)  **All fields are OPTIONAL:** - Omit a field to keep the original value - Provide a field to override the original value - retriever_name is REQUIRED (clones must have unique names)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retriever_name** | **str** | REQUIRED. Name for the cloned retriever. Must be unique and different from the source retriever. | 
**description** | **str** | OPTIONAL. Description override. If omitted, copies from source retriever. | [optional] 
**collection_identifiers** | **List[str]** | OPTIONAL. Override target collections. If omitted, copies from source retriever. This allows you to apply the same retriever logic to different collections. | [optional] 
**stages** | [**List[StageConfig]**](StageConfig.md) | OPTIONAL. Override stage configurations. If omitted, copies from source retriever. This is where you&#39;d fix typos, add stages, or tweak parameters. | [optional] 
**input_schema** | [**Dict[str, RetrieverInputSchemaFieldInput]**](RetrieverInputSchemaFieldInput.md) | OPTIONAL. Override input schema. If omitted, copies from source retriever. | [optional] 
**budget_limits** | [**BudgetLimits**](BudgetLimits.md) | OPTIONAL. Override budget limits. If omitted, copies from source retriever. | [optional] 
**tags** | **List[str]** | OPTIONAL. Override tags. If omitted, copies from source retriever. | [optional] 
**display_config** | [**DisplayConfigInput**](DisplayConfigInput.md) | OPTIONAL. Override display configuration. If omitted, copies from source retriever. | [optional] 

## Example

```python
from mixpeek.models.clone_retriever_request import CloneRetrieverRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CloneRetrieverRequest from a JSON string
clone_retriever_request_instance = CloneRetrieverRequest.from_json(json)
# print the JSON string representation of the object
print(CloneRetrieverRequest.to_json())

# convert the object into a dict
clone_retriever_request_dict = clone_retriever_request_instance.to_dict()
# create an instance of CloneRetrieverRequest from a dict
clone_retriever_request_from_dict = CloneRetrieverRequest.from_dict(clone_retriever_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


