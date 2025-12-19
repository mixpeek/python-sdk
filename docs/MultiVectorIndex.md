# MultiVectorIndex

Configuration for multi-vector indexes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | 
**vectors** | [**Dict[str, VectorIndex]**](VectorIndex.md) |  | 

## Example

```python
from mixpeek.models.multi_vector_index import MultiVectorIndex

# TODO update the JSON string below
json = "{}"
# create an instance of MultiVectorIndex from a JSON string
multi_vector_index_instance = MultiVectorIndex.from_json(json)
# print the JSON string representation of the object
print(MultiVectorIndex.to_json())

# convert the object into a dict
multi_vector_index_dict = multi_vector_index_instance.to_dict()
# create an instance of MultiVectorIndex from a dict
multi_vector_index_from_dict = MultiVectorIndex.from_dict(multi_vector_index_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


