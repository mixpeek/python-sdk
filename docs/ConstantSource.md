# ConstantSource

Use a constant/static value for all synced objects.  Useful for adding fixed metadata to all objects from a sync, such as: - Source system identifier - Environment tags - Default categories - Static labels  Provider Compatibility: All providers  Example mappings:     {\"type\": \"constant\", \"value\": \"tigris-cdn\"} -> All objects get \"tigris-cdn\"     {\"type\": \"constant\", \"value\": [\"tag1\", \"tag2\"]} -> All objects get this array     {\"type\": \"constant\", \"value\": {\"env\": \"prod\"}} -> All objects get this object  Attributes:     type: Must be \"constant\" to identify this source type     value: The constant value (any JSON-serializable type)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Source type identifier. Must be &#39;constant&#39; for static values. | [optional] [default to 'constant']
**value** | **object** |  | 

## Example

```python
from mixpeek.models.constant_source import ConstantSource

# TODO update the JSON string below
json = "{}"
# create an instance of ConstantSource from a JSON string
constant_source_instance = ConstantSource.from_json(json)
# print the JSON string representation of the object
print(ConstantSource.to_json())

# convert the object into a dict
constant_source_dict = constant_source_instance.to_dict()
# create an instance of ConstantSource from a dict
constant_source_from_dict = ConstantSource.from_dict(constant_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


