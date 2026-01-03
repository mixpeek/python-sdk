# CreateTemplateFromResourceResponse

Response after creating a template from a resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_id** | **str** | ID of the created template | 
**template_name** | **str** | Name of the created template | 
**template_type** | [**TemplateType**](TemplateType.md) | Type of template created | 
**scope** | [**TemplateScope**](TemplateScope.md) | Template scope | 
**source_resource_id** | **str** | ID of the resource used to create this template | 
**created_at** | **datetime** | Timestamp when template was created | [optional] 

## Example

```python
from mixpeek.models.create_template_from_resource_response import CreateTemplateFromResourceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTemplateFromResourceResponse from a JSON string
create_template_from_resource_response_instance = CreateTemplateFromResourceResponse.from_json(json)
# print the JSON string representation of the object
print(CreateTemplateFromResourceResponse.to_json())

# convert the object into a dict
create_template_from_resource_response_dict = create_template_from_resource_response_instance.to_dict()
# create an instance of CreateTemplateFromResourceResponse from a dict
create_template_from_resource_response_from_dict = CreateTemplateFromResourceResponse.from_dict(create_template_from_resource_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


