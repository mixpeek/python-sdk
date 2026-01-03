# ListTemplatesResponse

Response model for listing templates.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[BaseTemplateModel]**](BaseTemplateModel.md) | List of templates | 
**total_count** | **int** | Total number of templates matching the query | 

## Example

```python
from mixpeek.models.list_templates_response import ListTemplatesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListTemplatesResponse from a JSON string
list_templates_response_instance = ListTemplatesResponse.from_json(json)
# print the JSON string representation of the object
print(ListTemplatesResponse.to_json())

# convert the object into a dict
list_templates_response_dict = list_templates_response_instance.to_dict()
# create an instance of ListTemplatesResponse from a dict
list_templates_response_from_dict = ListTemplatesResponse.from_dict(list_templates_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


