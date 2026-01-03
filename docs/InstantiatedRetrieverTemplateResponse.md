# InstantiatedRetrieverTemplateResponse

Response after instantiating a retriever template.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retriever_id** | **str** | ID of the created retriever | 
**retriever_name** | **str** | Name of the created retriever | 
**template_id** | **str** | ID of the template used | 
**status** | **str** | Status of the instantiation | [optional] [default to 'created']
**created_at** | **datetime** | Timestamp when retriever was created | [optional] 

## Example

```python
from mixpeek.models.instantiated_retriever_template_response import InstantiatedRetrieverTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InstantiatedRetrieverTemplateResponse from a JSON string
instantiated_retriever_template_response_instance = InstantiatedRetrieverTemplateResponse.from_json(json)
# print the JSON string representation of the object
print(InstantiatedRetrieverTemplateResponse.to_json())

# convert the object into a dict
instantiated_retriever_template_response_dict = instantiated_retriever_template_response_instance.to_dict()
# create an instance of InstantiatedRetrieverTemplateResponse from a dict
instantiated_retriever_template_response_from_dict = InstantiatedRetrieverTemplateResponse.from_dict(instantiated_retriever_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


