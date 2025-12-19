# InputMapping

Declarative mapping for building inputs from various sources.  - input_key: The key used in the constructed inputs payload - source_type: Where to fetch the value (payload, literal, vector) - path: Dot-notation path when source_type is PAYLOAD or VECTOR - override: Static value when source_type is LITERAL

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_key** | **str** | Key used in the constructed inputs payload. | 
**source_type** | [**InputSourceType**](InputSourceType.md) | Source of the value (payload, literal, vector). | [optional] 
**path** | **str** | Dot-notation path inside payload/vector when source_type is PAYLOAD or VECTOR. | [optional] 
**override** | **object** |  | [optional] 

## Example

```python
from mixpeek.models.input_mapping import InputMapping

# TODO update the JSON string below
json = "{}"
# create an instance of InputMapping from a JSON string
input_mapping_instance = InputMapping.from_json(json)
# print the JSON string representation of the object
print(InputMapping.to_json())

# convert the object into a dict
input_mapping_dict = input_mapping_instance.to_dict()
# create an instance of InputMapping from a dict
input_mapping_from_dict = InputMapping.from_dict(input_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


