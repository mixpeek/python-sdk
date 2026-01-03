# InstantiatedCollectionTemplateResponse

Response after instantiating a collection template.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_id** | **str** | ID of the created collection | 
**collection_name** | **str** | Name of the created collection | 
**template_id** | **str** | ID of the template used | 
**status** | **str** | Status of the instantiation | [optional] [default to 'created']
**created_at** | **datetime** | Timestamp when collection was created | [optional] 

## Example

```python
from mixpeek.models.instantiated_collection_template_response import InstantiatedCollectionTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InstantiatedCollectionTemplateResponse from a JSON string
instantiated_collection_template_response_instance = InstantiatedCollectionTemplateResponse.from_json(json)
# print the JSON string representation of the object
print(InstantiatedCollectionTemplateResponse.to_json())

# convert the object into a dict
instantiated_collection_template_response_dict = instantiated_collection_template_response_instance.to_dict()
# create an instance of InstantiatedCollectionTemplateResponse from a dict
instantiated_collection_template_response_from_dict = InstantiatedCollectionTemplateResponse.from_dict(instantiated_collection_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


