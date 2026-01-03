# FieldFormatOptions

Format-specific options for field display.  Different format types support different options: - text: label, truncate_chars, show_empty - image: width, height, lazy_load, aspect_ratio, object_fit - date: label, date_format (iso, relative, custom) - number: label, decimals, prefix, suffix, show_empty - url: label, open_in_new_tab, show_domain - boolean: label, true_label, false_label - array: label, separator, max_items

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Display label for this field | [optional] 
**show_empty** | **bool** | Whether to show the field if value is empty/null | [optional] [default to True]
**truncate_chars** | **int** | Maximum characters before truncation (for text fields) | [optional] 
**width** | **int** | Image width in pixels | [optional] 
**height** | **int** | Image height in pixels | [optional] 
**lazy_load** | **bool** | Enable lazy loading for images (default: true) | [optional] [default to True]
**aspect_ratio** | **str** | Aspect ratio for image container | [optional] 
**object_fit** | **str** | CSS object-fit property for images | [optional] [default to 'cover']
**date_format** | **str** | Date format type: &#39;iso&#39;, &#39;relative&#39;, or custom format string | [optional] [default to 'relative']
**decimals** | **int** | Number of decimal places | [optional] 
**prefix** | **str** | Prefix for number display | [optional] 
**suffix** | **str** | Suffix for number display | [optional] 
**open_in_new_tab** | **bool** | Open URLs in new tab (default: true) | [optional] [default to True]
**show_domain** | **bool** | Show domain instead of full URL | [optional] [default to False]
**true_label** | **str** | Label for true values | [optional] [default to 'Yes']
**false_label** | **str** | Label for false values | [optional] [default to 'No']
**separator** | **str** | Separator for array items (default: &#39;, &#39;) | [optional] [default to ', ']
**max_items** | **int** | Maximum array items to display | [optional] 

## Example

```python
from mixpeek.models.field_format_options import FieldFormatOptions

# TODO update the JSON string below
json = "{}"
# create an instance of FieldFormatOptions from a JSON string
field_format_options_instance = FieldFormatOptions.from_json(json)
# print the JSON string representation of the object
print(FieldFormatOptions.to_json())

# convert the object into a dict
field_format_options_dict = field_format_options_instance.to_dict()
# create an instance of FieldFormatOptions from a dict
field_format_options_from_dict = FieldFormatOptions.from_dict(field_format_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


