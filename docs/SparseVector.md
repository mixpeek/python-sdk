# SparseVector

Sparse vector representation with indices and values.  Only non-zero elements are stored for efficiency.  Example: ```json {     \"indices\": [0, 2, 4],     \"values\": [0.1, 0.3, 0.5] } ```

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**indices** | [**List[RangeBucketBoundariesInner]**](RangeBucketBoundariesInner.md) | Indices of non-zero elements | 
**values** | **List[float]** | Values of non-zero elements | 

## Example

```python
from mixpeek.models.sparse_vector import SparseVector

# TODO update the JSON string below
json = "{}"
# create an instance of SparseVector from a JSON string
sparse_vector_instance = SparseVector.from_json(json)
# print the JSON string representation of the object
print(SparseVector.to_json())

# convert the object into a dict
sparse_vector_dict = sparse_vector_instance.to_dict()
# create an instance of SparseVector from a dict
sparse_vector_from_dict = SparseVector.from_dict(sparse_vector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


