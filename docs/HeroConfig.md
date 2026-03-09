# HeroConfig

Hero section configuration for a page.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**headline** | **str** | Main headline text | 
**subheadline** | **str** | Optional subheadline text | [optional] 
**background_type** | **str** | Background type | [optional] [default to 'solid']
**background_url** | **str** | URL for image or video background | [optional] 
**background_color** | **str** | Background color for solid/gradient | [optional] 
**text_color** | **str** | Hero text color | [optional] [default to '#FFFFFF']
**logo_url** | **str** | Logo URL displayed in hero | [optional] 
**height** | **str** | Hero section height | [optional] [default to '420px']
**cta_label** | **str** | Call-to-action button label | [optional] 
**cta_url** | **str** | Call-to-action button URL | [optional] 

## Example

```python
from mixpeek.models.hero_config import HeroConfig

# TODO update the JSON string below
json = "{}"
# create an instance of HeroConfig from a JSON string
hero_config_instance = HeroConfig.from_json(json)
# print the JSON string representation of the object
print(HeroConfig.to_json())

# convert the object into a dict
hero_config_dict = hero_config_instance.to_dict()
# create an instance of HeroConfig from a dict
hero_config_from_dict = HeroConfig.from_dict(hero_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


