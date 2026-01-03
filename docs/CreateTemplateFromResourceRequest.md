# CreateTemplateFromResourceRequest

Request to create a template from an existing resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_name** | **str** | Name for the new template | 
**description** | **str** | Description of the template&#39;s purpose (OPTIONAL) | [optional] 
**scope** | [**TemplateScope**](TemplateScope.md) | Template scope: &#39;organization&#39; (all users in org), &#39;user&#39; (only you), or &#39;system&#39; (all organizations - requires Mixpeek admin email) | [optional] 
**category** | **str** | Optional category for organizing templates | [optional] 
**tags** | **List[str]** | Optional tags for the template | [optional] 
**is_public** | **bool** | Whether this template should be publicly discoverable | [optional] [default to False]

## Example

```python
from mixpeek.models.create_template_from_resource_request import CreateTemplateFromResourceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTemplateFromResourceRequest from a JSON string
create_template_from_resource_request_instance = CreateTemplateFromResourceRequest.from_json(json)
# print the JSON string representation of the object
print(CreateTemplateFromResourceRequest.to_json())

# convert the object into a dict
create_template_from_resource_request_dict = create_template_from_resource_request_instance.to_dict()
# create an instance of CreateTemplateFromResourceRequest from a dict
create_template_from_resource_request_from_dict = CreateTemplateFromResourceRequest.from_dict(create_template_from_resource_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


