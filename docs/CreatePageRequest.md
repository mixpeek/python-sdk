# CreatePageRequest

Request to create a new Page.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | **str** | URL-safe slug (globally unique, lowercase + hyphens) | 
**template** | **str** |  | [optional] [default to 'generic']
**sections** | [**List[SectionConfig]**](SectionConfig.md) |  | [optional] 
**custom_html** | **str** |  | [optional] 
**meta** | [**PageMeta**](PageMeta.md) |  | 
**hero** | [**HeroConfig**](HeroConfig.md) |  | [optional] 
**theme** | [**ThemeConfig**](ThemeConfig.md) |  | [optional] 
**seo** | [**SEOConfig**](SEOConfig.md) |  | [optional] 
**stats** | [**List[StatItem]**](StatItem.md) |  | [optional] 
**featured_gallery** | [**FeaturedGalleryConfigInput**](FeaturedGalleryConfigInput.md) |  | [optional] 
**tabs** | [**List[PageTabInput]**](PageTabInput.md) |  | [optional] 
**password_secret_name** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] [default to True]

## Example

```python
from mixpeek.models.create_page_request import CreatePageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePageRequest from a JSON string
create_page_request_instance = CreatePageRequest.from_json(json)
# print the JSON string representation of the object
print(CreatePageRequest.to_json())

# convert the object into a dict
create_page_request_dict = create_page_request_instance.to_dict()
# create an instance of CreatePageRequest from a dict
create_page_request_from_dict = CreatePageRequest.from_dict(create_page_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


