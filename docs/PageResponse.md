# PageResponse

Response model for a Page.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_id** | **str** |  | 
**slug** | **str** |  | 
**template** | **str** |  | 
**sections** | [**List[SectionConfig]**](SectionConfig.md) |  | 
**custom_html** | **str** |  | 
**meta** | [**PageMeta**](PageMeta.md) |  | 
**hero** | [**HeroConfig**](HeroConfig.md) |  | 
**theme** | [**ThemeConfig**](ThemeConfig.md) |  | 
**seo** | [**SEOConfig**](SEOConfig.md) |  | 
**stats** | [**List[StatItem]**](StatItem.md) |  | 
**featured_gallery** | [**FeaturedGalleryConfigOutput**](FeaturedGalleryConfigOutput.md) |  | 
**tabs** | [**List[PageTabOutput]**](PageTabOutput.md) |  | 
**password_protected** | **bool** |  | 
**is_active** | **bool** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from mixpeek.models.page_response import PageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PageResponse from a JSON string
page_response_instance = PageResponse.from_json(json)
# print the JSON string representation of the object
print(PageResponse.to_json())

# convert the object into a dict
page_response_dict = page_response_instance.to_dict()
# create an instance of PageResponse from a dict
page_response_from_dict = PageResponse.from_dict(page_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


