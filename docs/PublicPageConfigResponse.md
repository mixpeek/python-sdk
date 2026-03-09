# PublicPageConfigResponse

Public page configuration (strips internal fields).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | **str** |  | 
**template** | **str** |  | 
**sections** | [**List[SectionConfig]**](SectionConfig.md) |  | [optional] 
**custom_html** | **str** |  | [optional] 
**meta** | [**PageMeta**](PageMeta.md) |  | 
**hero** | [**HeroConfig**](HeroConfig.md) |  | 
**theme** | [**ThemeConfig**](ThemeConfig.md) |  | 
**seo** | [**SEOConfig**](SEOConfig.md) |  | 
**stats** | [**List[StatItem]**](StatItem.md) |  | 
**featured_gallery** | [**FeaturedGalleryConfigOutput**](FeaturedGalleryConfigOutput.md) |  | 
**tabs** | [**List[PageTabOutput]**](PageTabOutput.md) |  | 
**is_active** | **bool** |  | 
**password_protected** | **bool** |  | 

## Example

```python
from mixpeek.models.public_page_config_response import PublicPageConfigResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PublicPageConfigResponse from a JSON string
public_page_config_response_instance = PublicPageConfigResponse.from_json(json)
# print the JSON string representation of the object
print(PublicPageConfigResponse.to_json())

# convert the object into a dict
public_page_config_response_dict = public_page_config_response_instance.to_dict()
# create an instance of PublicPageConfigResponse from a dict
public_page_config_response_from_dict = PublicPageConfigResponse.from_dict(public_page_config_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


