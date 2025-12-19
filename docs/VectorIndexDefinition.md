# VectorIndexDefinition

Complete vector index definition that can be either single or multi-vector.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | 
**type** | **str** |  | 
**index** | [**Index**](Index.md) |  | 

## Example

```python
from mixpeek.models.vector_index_definition import VectorIndexDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of VectorIndexDefinition from a JSON string
vector_index_definition_instance = VectorIndexDefinition.from_json(json)
# print the JSON string representation of the object
print(VectorIndexDefinition.to_json())

# convert the object into a dict
vector_index_definition_dict = vector_index_definition_instance.to_dict()
# create an instance of VectorIndexDefinition from a dict
vector_index_definition_from_dict = VectorIndexDefinition.from_dict(vector_index_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


