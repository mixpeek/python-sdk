# Vectors

Vector representation of the feature. Can be any supported vector type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**indices** | [**List[RangeBucketBoundariesInner]**](RangeBucketBoundariesInner.md) | Indices of non-zero elements | 
**values** | **List[float]** | Values of non-zero elements | 

## Example

```python
from mixpeek.models.vectors import Vectors

# TODO update the JSON string below
json = "{}"
# create an instance of Vectors from a JSON string
vectors_instance = Vectors.from_json(json)
# print the JSON string representation of the object
print(Vectors.to_json())

# convert the object into a dict
vectors_dict = vectors_instance.to_dict()
# create an instance of Vectors from a dict
vectors_from_dict = Vectors.from_dict(vectors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


