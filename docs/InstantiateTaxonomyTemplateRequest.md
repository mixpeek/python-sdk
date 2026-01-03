# InstantiateTaxonomyTemplateRequest

Request to instantiate a taxonomy from a template.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**taxonomy_name** | **str** | Name for the new taxonomy | 
**collection_config** | **Dict[str, str]** | Collection configuration for the taxonomy. For flat taxonomies: {&#39;collection_id&#39;: &#39;col_xxx&#39;} For hierarchical taxonomies: maps node collection IDs to actual collection IDs, e.g., {&#39;col_template_root&#39;: &#39;col_actual_root&#39;, &#39;col_template_child&#39;: &#39;col_actual_child&#39;} | 
**description** | **str** | Optional description override for the taxonomy | [optional] 

## Example

```python
from mixpeek.models.instantiate_taxonomy_template_request import InstantiateTaxonomyTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InstantiateTaxonomyTemplateRequest from a JSON string
instantiate_taxonomy_template_request_instance = InstantiateTaxonomyTemplateRequest.from_json(json)
# print the JSON string representation of the object
print(InstantiateTaxonomyTemplateRequest.to_json())

# convert the object into a dict
instantiate_taxonomy_template_request_dict = instantiate_taxonomy_template_request_instance.to_dict()
# create an instance of InstantiateTaxonomyTemplateRequest from a dict
instantiate_taxonomy_template_request_from_dict = InstantiateTaxonomyTemplateRequest.from_dict(instantiate_taxonomy_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


