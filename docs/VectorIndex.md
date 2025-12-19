# VectorIndex

Base configuration for vector indexes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | 
**dimensions** | **int** |  | 
**type** | [**VectorType**](VectorType.md) |  | 
**distance** | **str** |  | [optional] [default to 'cosine']
**datatype** | [**VectorDataType**](VectorDataType.md) | Data type of the vector. | [optional] 
**on_disk** | **bool** | If true, vectors will be stored on disk. Use for large vectors. | [optional] 
**supported_inputs** | [**List[BucketSchemaFieldType]**](BucketSchemaFieldType.md) |  | [optional] 
**inference_name** | **str** | The path to the embedding model service to use for this vector index. | [optional] 

## Example

```python
from mixpeek.models.vector_index import VectorIndex

# TODO update the JSON string below
json = "{}"
# create an instance of VectorIndex from a JSON string
vector_index_instance = VectorIndex.from_json(json)
# print the JSON string representation of the object
print(VectorIndex.to_json())

# convert the object into a dict
vector_index_dict = vector_index_instance.to_dict()
# create an instance of VectorIndex from a dict
vector_index_from_dict = VectorIndex.from_dict(vector_index_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


