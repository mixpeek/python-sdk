# CloneTaxonomyRequest

Request to clone a taxonomy with optional modifications.  **Purpose:** Cloning creates a NEW taxonomy (with new ID) based on an existing one, allowing you to make changes that aren't allowed via PATCH (config, retriever_id, collections). This is the recommended way to iterate on taxonomy designs.  **Clone vs Template vs Version:** - **Clone**: Copy THIS taxonomy and modify it (for iteration/fixes) - **Template**: Create taxonomy from a reusable pattern (for new projects) - **Version**: (Not implemented) - Use clone instead  **Use Cases:** - Fix configuration errors without losing join history - Change retriever or input mappings - Change target collections - Test modifications before replacing production taxonomy - Create variants for different datasets  **All fields are OPTIONAL:** - Omit a field to keep the original value - Provide a field to override the original value - taxonomy_name is REQUIRED (clones must have unique names)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**taxonomy_name** | **str** | REQUIRED. Name for the cloned taxonomy. Must be unique and different from the source taxonomy. | 
**description** | **str** | OPTIONAL. Description override. If omitted, copies from source taxonomy. | [optional] 
**config** | [**Config**](Config.md) |  | [optional] 

## Example

```python
from mixpeek.models.clone_taxonomy_request import CloneTaxonomyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CloneTaxonomyRequest from a JSON string
clone_taxonomy_request_instance = CloneTaxonomyRequest.from_json(json)
# print the JSON string representation of the object
print(CloneTaxonomyRequest.to_json())

# convert the object into a dict
clone_taxonomy_request_dict = clone_taxonomy_request_instance.to_dict()
# create an instance of CloneTaxonomyRequest from a dict
clone_taxonomy_request_from_dict = CloneTaxonomyRequest.from_dict(clone_taxonomy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


