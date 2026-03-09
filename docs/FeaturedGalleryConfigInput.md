# FeaturedGalleryConfigInput

Configuration for the featured gallery section.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Whether the featured gallery is shown | [optional] [default to True]
**title** | **str** | Gallery section title | [optional] [default to 'Featured']
**retriever_id** | **str** | Internal retriever ID (defaults to first tab&#39;s retriever) | [optional] 
**public_name** | **str** | Marketplace catalog public_name for gallery execution | [optional] 
**default_inputs** | **Dict[str, object]** | Default inputs to auto-execute when page loads | [optional] 
**layout** | [**LayoutConfig**](LayoutConfig.md) | Layout configuration for gallery results | [optional] 
**field_config** | [**Dict[str, FieldConfig]**](FieldConfig.md) | Field display configuration for gallery results | [optional] 

## Example

```python
from mixpeek.models.featured_gallery_config_input import FeaturedGalleryConfigInput

# TODO update the JSON string below
json = "{}"
# create an instance of FeaturedGalleryConfigInput from a JSON string
featured_gallery_config_input_instance = FeaturedGalleryConfigInput.from_json(json)
# print the JSON string representation of the object
print(FeaturedGalleryConfigInput.to_json())

# convert the object into a dict
featured_gallery_config_input_dict = featured_gallery_config_input_instance.to_dict()
# create an instance of FeaturedGalleryConfigInput from a dict
featured_gallery_config_input_from_dict = FeaturedGalleryConfigInput.from_dict(featured_gallery_config_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


