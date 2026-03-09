# PageMeta

Page-level metadata.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Page title | 
**description** | **str** | Page description | [optional] 
**logo_url** | **str** | Logo URL | [optional] 
**favicon_url** | **str** | Favicon URL | [optional] 

## Example

```python
from mixpeek.models.page_meta import PageMeta

# TODO update the JSON string below
json = "{}"
# create an instance of PageMeta from a JSON string
page_meta_instance = PageMeta.from_json(json)
# print the JSON string representation of the object
print(PageMeta.to_json())

# convert the object into a dict
page_meta_dict = page_meta_instance.to_dict()
# create an instance of PageMeta from a dict
page_meta_from_dict = PageMeta.from_dict(page_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


