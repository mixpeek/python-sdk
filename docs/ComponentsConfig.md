# ComponentsConfig

Configuration for UI components.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**show_hero** | **bool** | Whether to show the hero section with title and description | [optional] [default to True]
**show_search** | **bool** | Whether to show search input fields | [optional] [default to True]
**show_filters** | **bool** | Whether to show filters sidebar | [optional] [default to False]
**show_results_header** | **bool** | Whether to show the results header with count and sorting options | [optional] [default to True]
**result_layout** | **str** | Layout mode for results display | [optional] [default to 'grid']
**result_card** | [**ResultCardProperties**](ResultCardProperties.md) | Configuration for result card display | [optional] 

## Example

```python
from mixpeek.models.components_config import ComponentsConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ComponentsConfig from a JSON string
components_config_instance = ComponentsConfig.from_json(json)
# print the JSON string representation of the object
print(ComponentsConfig.to_json())

# convert the object into a dict
components_config_dict = components_config_instance.to_dict()
# create an instance of ComponentsConfig from a dict
components_config_from_dict = ComponentsConfig.from_dict(components_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


