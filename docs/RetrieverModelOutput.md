# RetrieverModelOutput

Retriever configuration model exposed via API.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retriever_id** | **str** | Stable retriever identifier (REQUIRED). | [optional] 
**retriever_name** | **str** | Unique retriever name within namespace (REQUIRED). | 
**description** | **str** | Detailed description of retriever behaviour (OPTIONAL). | [optional] 
**collection_ids** | **List[str]** | Collections queried by the retriever. Can be empty for query-only inference mode. | [optional] 
**stages** | [**List[StageConfig]**](StageConfig.md) | Ordered list of stage configurations (REQUIRED). | 
**input_schema** | [**Dict[str, RetrieverInputSchemaFieldOutput]**](RetrieverInputSchemaFieldOutput.md) | JSON Schema describing expected user inputs (REQUIRED). Properties must use RetrieverInputSchemaField which supports all bucket types plus document_reference. | [optional] 
**budget_limits** | [**BudgetLimits**](BudgetLimits.md) | Execution budget limits for the retriever (OPTIONAL). | [optional] 
**feature_dependencies** | [**List[FeatureAddress]**](FeatureAddress.md) | Feature addresses required by stages (OPTIONAL, aids validation). | [optional] 
**tags** | **List[str]** | Arbitrary tags to help organise retrievers (OPTIONAL). | [optional] 
**display_config** | **Dict[str, object]** | Display configuration for public retriever UI rendering (OPTIONAL). Defines how the search interface should appear when the retriever is published, including input fields, theme, layout, exposed result fields, and field formatting. This configuration is used as the default when publishing the retriever. | [optional] 
**version** | **int** | Version number that increments on each update (REQUIRED). | [optional] [default to 1]
**created_at** | **datetime** | Creation timestamp in UTC (REQUIRED). | [optional] 
**updated_at** | **datetime** | Last update timestamp in UTC (REQUIRED). | [optional] 
**created_by** | **str** | Identifier of the user who created the retriever (OPTIONAL). | [optional] 
**updated_by** | **str** | Identifier of the user who last updated the retriever (OPTIONAL). | [optional] 
**is_published** | **bool** | Whether this retriever is currently published as a public API | [optional] [default to False]

## Example

```python
from mixpeek.models.retriever_model_output import RetrieverModelOutput

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieverModelOutput from a JSON string
retriever_model_output_instance = RetrieverModelOutput.from_json(json)
# print the JSON string representation of the object
print(RetrieverModelOutput.to_json())

# convert the object into a dict
retriever_model_output_dict = retriever_model_output_instance.to_dict()
# create an instance of RetrieverModelOutput from a dict
retriever_model_output_from_dict = RetrieverModelOutput.from_dict(retriever_model_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


