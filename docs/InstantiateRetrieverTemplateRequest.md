# InstantiateRetrieverTemplateRequest

Request to instantiate a retriever from a template.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retriever_name** | **str** | Name for the new retriever | 
**collection_identifiers** | **List[str]** | Collection identifiers to use for the retriever | 
**description** | **str** | Optional description override for the retriever | [optional] 
**tags** | **List[str]** | Optional tags for the retriever | [optional] 

## Example

```python
from mixpeek.models.instantiate_retriever_template_request import InstantiateRetrieverTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InstantiateRetrieverTemplateRequest from a JSON string
instantiate_retriever_template_request_instance = InstantiateRetrieverTemplateRequest.from_json(json)
# print the JSON string representation of the object
print(InstantiateRetrieverTemplateRequest.to_json())

# convert the object into a dict
instantiate_retriever_template_request_dict = instantiate_retriever_template_request_instance.to_dict()
# create an instance of InstantiateRetrieverTemplateRequest from a dict
instantiate_retriever_template_request_from_dict = InstantiateRetrieverTemplateRequest.from_dict(instantiate_retriever_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


