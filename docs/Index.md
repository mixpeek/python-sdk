# Index


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
**vectors** | [**Dict[str, VectorIndex]**](VectorIndex.md) |  | 

## Example

```python
from mixpeek.models.index import Index

# TODO update the JSON string below
json = "{}"
# create an instance of Index from a JSON string
index_instance = Index.from_json(json)
# print the JSON string representation of the object
print(Index.to_json())

# convert the object into a dict
index_dict = index_instance.to_dict()
# create an instance of Index from a dict
index_from_dict = Index.from_dict(index_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


