# StructuredDataConfig

Schema.org structured data configuration for search engines.  Enables rich search results and better understanding of the page content.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Schema.org type for structured data | [optional] [default to 'WebApplication']
**additional_properties** | **object** | Additional Schema.org properties | [optional] 

## Example

```python
from mixpeek.models.structured_data_config import StructuredDataConfig

# TODO update the JSON string below
json = "{}"
# create an instance of StructuredDataConfig from a JSON string
structured_data_config_instance = StructuredDataConfig.from_json(json)
# print the JSON string representation of the object
print(StructuredDataConfig.to_json())

# convert the object into a dict
structured_data_config_dict = structured_data_config_instance.to_dict()
# create an instance of StructuredDataConfig from a dict
structured_data_config_from_dict = StructuredDataConfig.from_dict(structured_data_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


