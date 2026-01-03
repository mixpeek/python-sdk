# ExternalLink

External resource link for a published retriever.  Used to link to related resources like GitHub repos, blog posts, documentation, or other relevant URLs displayed on the homepage.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Display name for the link | 
**url** | **str** | URL to the external resource | 

## Example

```python
from mixpeek.models.external_link import ExternalLink

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalLink from a JSON string
external_link_instance = ExternalLink.from_json(json)
# print the JSON string representation of the object
print(ExternalLink.to_json())

# convert the object into a dict
external_link_dict = external_link_instance.to_dict()
# create an instance of ExternalLink from a dict
external_link_from_dict = ExternalLink.from_dict(external_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


