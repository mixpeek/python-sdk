# InstantiatedTaxonomyTemplateResponse

Response after instantiating a taxonomy template.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**taxonomy_id** | **str** | ID of the created taxonomy | 
**taxonomy_name** | **str** | Name of the created taxonomy | 
**template_id** | **str** | ID of the template used | 
**status** | **str** | Status of the instantiation | [optional] [default to 'created']
**created_at** | **datetime** | Timestamp when taxonomy was created | [optional] 

## Example

```python
from mixpeek.models.instantiated_taxonomy_template_response import InstantiatedTaxonomyTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InstantiatedTaxonomyTemplateResponse from a JSON string
instantiated_taxonomy_template_response_instance = InstantiatedTaxonomyTemplateResponse.from_json(json)
# print the JSON string representation of the object
print(InstantiatedTaxonomyTemplateResponse.to_json())

# convert the object into a dict
instantiated_taxonomy_template_response_dict = instantiated_taxonomy_template_response_instance.to_dict()
# create an instance of InstantiatedTaxonomyTemplateResponse from a dict
instantiated_taxonomy_template_response_from_dict = InstantiatedTaxonomyTemplateResponse.from_dict(instantiated_taxonomy_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


