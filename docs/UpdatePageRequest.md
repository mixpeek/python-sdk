# UpdatePageRequest

Request to update an existing Page (all fields optional).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | **str** |  | [optional] 
**template** | **str** |  | [optional] 
**sections** | [**List[SectionConfig]**](SectionConfig.md) |  | [optional] 
**custom_html** | **str** |  | [optional] 
**meta** | [**PageMeta**](PageMeta.md) |  | [optional] 
**hero** | [**HeroConfig**](HeroConfig.md) |  | [optional] 
**theme** | [**ThemeConfig**](ThemeConfig.md) |  | [optional] 
**seo** | [**SEOConfig**](SEOConfig.md) |  | [optional] 
**stats** | [**List[StatItem]**](StatItem.md) |  | [optional] 
**featured_gallery** | [**FeaturedGalleryConfigInput**](FeaturedGalleryConfigInput.md) |  | [optional] 
**tabs** | [**List[PageTabInput]**](PageTabInput.md) |  | [optional] 
**password_secret_name** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 

## Example

```python
from mixpeek.models.update_page_request import UpdatePageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePageRequest from a JSON string
update_page_request_instance = UpdatePageRequest.from_json(json)
# print the JSON string representation of the object
print(UpdatePageRequest.to_json())

# convert the object into a dict
update_page_request_dict = update_page_request_instance.to_dict()
# create an instance of UpdatePageRequest from a dict
update_page_request_from_dict = UpdatePageRequest.from_dict(update_page_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


