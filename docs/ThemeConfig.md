# ThemeConfig

Theme configuration for public retriever UI.  Defines colors, fonts, and visual styling for the public search interface.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary_color** | **str** | Primary brand color (hex code) | [optional] [default to '#007AFF']
**secondary_color** | **str** | Secondary/accent color (hex code) | [optional] 
**font_family** | **str** | Font family for text | [optional] [default to 'system-ui, -apple-system, sans-serif']
**background_color** | **str** | Background color (hex code) | [optional] [default to '#FFFFFF']
**text_color** | **str** | Primary text color (hex code) | [optional] [default to '#374151']
**heading_font_family** | **str** | Optional separate font family for headings | [optional] 
**surface_color** | **str** | Surface/card background color (hex code) | [optional] 
**muted_color** | **str** | Muted/secondary text color (hex code) | [optional] 
**border_color** | **str** | Border color for cards and elements (hex code) | [optional] 
**border_radius** | **str** | Default border radius for cards and elements | [optional] [default to '12px']
**card_style** | **str** | Card visual style: elevated (shadow), flat (no shadow), bordered, or glass (frosted glass effect) | [optional] [default to 'elevated']
**card_hover_effect** | **str** | Card hover animation effect: lift (move up), glow, scale, or none | [optional] [default to 'lift']

## Example

```python
from mixpeek.models.theme_config import ThemeConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ThemeConfig from a JSON string
theme_config_instance = ThemeConfig.from_json(json)
# print the JSON string representation of the object
print(ThemeConfig.to_json())

# convert the object into a dict
theme_config_dict = theme_config_instance.to_dict()
# create an instance of ThemeConfig from a dict
theme_config_from_dict = ThemeConfig.from_dict(theme_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


