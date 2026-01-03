# FieldConfig

Configuration for how to display a specific field in results.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | [**FieldFormatType**](FieldFormatType.md) | Format type for this field (text, image, date, number, etc.) | 
**format_options** | [**FieldFormatOptions**](FieldFormatOptions.md) | Format-specific display options | [optional] 

## Example

```python
from mixpeek.models.field_config import FieldConfig

# TODO update the JSON string below
json = "{}"
# create an instance of FieldConfig from a JSON string
field_config_instance = FieldConfig.from_json(json)
# print the JSON string representation of the object
print(FieldConfig.to_json())

# convert the object into a dict
field_config_dict = field_config_instance.to_dict()
# create an instance of FieldConfig from a dict
field_config_from_dict = FieldConfig.from_dict(field_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


