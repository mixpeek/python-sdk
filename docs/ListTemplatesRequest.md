# ListTemplatesRequest

Request model for listing templates.  Provides the same filtering, sorting, and search capabilities as other list operations (list collections, list buckets, etc.).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | **Dict[str, object]** | Filters to apply when listing templates. Format: {\&quot;AND\&quot;: [{\&quot;field\&quot;: \&quot;field_name\&quot;, \&quot;operator\&quot;: \&quot;eq\&quot;, \&quot;value\&quot;: \&quot;value\&quot;}]} | [optional] 
**sort** | **Dict[str, str]** | Sort options for the results. Format: {&#39;field&#39;: &#39;name&#39;, &#39;direction&#39;: &#39;asc&#39;} | [optional] 
**search** | **str** | Search term for wildcard search across template_id, name, description, and tags | [optional] 
**scope** | [**TemplateScope**](TemplateScope.md) | Filter by scope (system, organization, or user) | [optional] 
**category** | **str** | Filter by category | [optional] 
**is_active** | **bool** | Show only active templates | [optional] [default to True]
**tags** | **List[str]** | Filter by tags (templates must have ALL specified tags) | [optional] 

## Example

```python
from mixpeek.models.list_templates_request import ListTemplatesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListTemplatesRequest from a JSON string
list_templates_request_instance = ListTemplatesRequest.from_json(json)
# print the JSON string representation of the object
print(ListTemplatesRequest.to_json())

# convert the object into a dict
list_templates_request_dict = list_templates_request_instance.to_dict()
# create an instance of ListTemplatesRequest from a dict
list_templates_request_from_dict = ListTemplatesRequest.from_dict(list_templates_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


