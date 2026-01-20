# InputMappingSource

Defines how to get a value for a retriever input.  Can be a document field reference or a constant value.  Attributes:     source_type: Where the value comes from ('document_field' or 'constant')     path: JSONPath to document field (when source_type='document_field')     value: Constant value to use (when source_type='constant')

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_type** | **str** | Where the value comes from | 
**path** | **str** | JSONPath to document field (when source_type&#x3D;&#39;document_field&#39;) | [optional] 
**value** | **object** |  | [optional] 

## Example

```python
from mixpeek.models.input_mapping_source import InputMappingSource

# TODO update the JSON string below
json = "{}"
# create an instance of InputMappingSource from a JSON string
input_mapping_source_instance = InputMappingSource.from_json(json)
# print the JSON string representation of the object
print(InputMappingSource.to_json())

# convert the object into a dict
input_mapping_source_dict = input_mapping_source_instance.to_dict()
# create an instance of InputMappingSource from a dict
input_mapping_source_from_dict = InputMappingSource.from_dict(input_mapping_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


