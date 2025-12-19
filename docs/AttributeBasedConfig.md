# AttributeBasedConfig

Configuration for attribute-based clustering.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | **List[str]** | Attributes to use for clustering | 
**hierarchical_grouping** | **bool** | Whether to create hierarchical groups | [optional] [default to False]
**aggregation_method** | **str** | Method for aggregating attributes | [optional] 

## Example

```python
from mixpeek.models.attribute_based_config import AttributeBasedConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeBasedConfig from a JSON string
attribute_based_config_instance = AttributeBasedConfig.from_json(json)
# print the JSON string representation of the object
print(AttributeBasedConfig.to_json())

# convert the object into a dict
attribute_based_config_dict = attribute_based_config_instance.to_dict()
# create an instance of AttributeBasedConfig from a dict
attribute_based_config_from_dict = AttributeBasedConfig.from_dict(attribute_based_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


