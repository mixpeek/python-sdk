# CreateRetrieverRequest

Request to create a new retriever.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retriever_name** | **str** | Human-readable retriever name | 
**description** | **str** | Description of the retriever | [optional] 
**input_schema** | [**RetrieverSchemaInput**](RetrieverSchemaInput.md) | Schema defining the expected input format | 
**collection_ids** | **List[str]** | List of collection IDs to search in | 
**stages** | [**List[StageInstanceConfigInput]**](StageInstanceConfigInput.md) | List of stages to execute in order | 
**metadata** | **Dict[str, object]** | Custom metadata for the retriever | [optional] 
**tags** | **List[str]** | Tags for organization and filtering | [optional] 
**enabled** | **bool** | Whether the retriever should be enabled on creation | [optional] [default to True]

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


