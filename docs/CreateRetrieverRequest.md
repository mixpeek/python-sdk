# CreateRetrieverRequest

Payload for creating a new retriever.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retriever_name** | **str** | Unique retriever name (REQUIRED). | 
**description** | **str** | Human readable retriever description (OPTIONAL). | [optional] 
**collection_identifiers** | **List[str]** | Collection identifiers (names or IDs) queried by the retriever (OPTIONAL). Identifiers can be collection names (e.g., &#39;my_collection&#39;) or collection IDs (e.g., &#39;col_abc123&#39;). The system will resolve names to IDs automatically. Can be empty for inference-only pipelines (e.g., LLM query analysis without document retrieval). | [optional] 
**stages** | [**List[StageConfig]**](StageConfig.md) | Ordered stage configurations (REQUIRED). | 
**input_schema** | [**Dict[str, RetrieverInputSchemaFieldInput]**](RetrieverInputSchemaFieldInput.md) | Input schema properties keyed by field name (OPTIONAL). Can be empty for static retrievers with hardcoded stage parameters. Each field can include: type, description, required, default, and examples. The &#39;examples&#39; field (list) provides sample values that will be shown to users when the retriever is published with include_metadata&#x3D;true. | [optional] 
**budget_limits** | [**BudgetLimits**](BudgetLimits.md) | Budget limits for execution (OPTIONAL). | [optional] 
**tags** | **List[str]** | Optional retriever tags for search/filters. | [optional] 
**display_config** | [**DisplayConfigInput**](DisplayConfigInput.md) | Display configuration for public retriever UI rendering (OPTIONAL). Defines how the search interface should appear when the retriever is published, including input fields, theme, layout, exposed result fields, and field formatting. This configuration is used as the default when publishing the retriever. | [optional] 

## Example

```python
from mixpeek.models.create_retriever_request import CreateRetrieverRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRetrieverRequest from a JSON string
create_retriever_request_instance = CreateRetrieverRequest.from_json(json)
# print the JSON string representation of the object
print(CreateRetrieverRequest.to_json())

# convert the object into a dict
create_retriever_request_dict = create_retriever_request_instance.to_dict()
# create an instance of CreateRetrieverRequest from a dict
create_retriever_request_from_dict = CreateRetrieverRequest.from_dict(create_retriever_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


