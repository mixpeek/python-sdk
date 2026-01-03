# BaseTemplateModel

Base template model with common fields for all template types.  This model is stored in MongoDB and supports three template scopes: - System: Mixpeek defaults (all orgs) - Organization: All users in the org - User: Only the creator

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_id** | **str** | Unique template identifier (e.g., &#39;tmpl_semantic_search&#39;) | 
**template_type** | [**TemplateType**](TemplateType.md) | Type of resource this template creates | 
**mode** | [**TemplateMode**](TemplateMode.md) | Template instantiation mode: clone (with data), config (empty), or scaffold (preset) | [optional] 
**scope** | [**TemplateScope**](TemplateScope.md) | Template scope (system or organization) | 
**internal_id** | **str** | Organization internal ID. For system templates, use &#39;system&#39;. For org templates, use the actual internal_id. | 
**name** | **str** | Human-readable template name | 
**description** | **str** | Detailed description of the template&#39;s purpose | 
**category** | **str** | Optional category for organizing templates | [optional] 
**configuration** | **Dict[str, object]** | Template-specific configuration (varies by template_type) | 
**tags** | **List[str]** | Tags for categorizing and filtering templates | [optional] 
**is_active** | **bool** | Whether this template is available for use | [optional] [default to True]
**is_public** | **bool** | Whether this template is publicly discoverable without authentication | [optional] [default to False]
**use_cases** | **List[str]** | List of common use cases for this template | [optional] 
**requirements** | **List[str]** | List of requirements (e.g., &#39;Requires text embeddings&#39;) | [optional] 
**created_by** | **str** | User ID who created this template (for org templates) | [optional] 
**source_resource_id** | **str** | ID of the resource this template was created from (for org templates) | [optional] 
**created_at** | **datetime** | Timestamp when template was created | [optional] 
**updated_at** | **datetime** | Timestamp when template was last updated | [optional] 

## Example

```python
from mixpeek.models.base_template_model import BaseTemplateModel

# TODO update the JSON string below
json = "{}"
# create an instance of BaseTemplateModel from a JSON string
base_template_model_instance = BaseTemplateModel.from_json(json)
# print the JSON string representation of the object
print(BaseTemplateModel.to_json())

# convert the object into a dict
base_template_model_dict = base_template_model_instance.to_dict()
# create an instance of BaseTemplateModel from a dict
base_template_model_from_dict = BaseTemplateModel.from_dict(base_template_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


