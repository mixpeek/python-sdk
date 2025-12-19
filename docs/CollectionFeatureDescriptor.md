# CollectionFeatureDescriptor

Descriptor for a collection's available feature using existing models/keys.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_address** | **str** | Fully qualified feature address | 
**feature_extractor_name** | **str** | Extractor name | 
**version** | **str** | Extractor version | 
**vector_index** | [**VectorIndex**](VectorIndex.md) | Vector index configuration (name, dimensions, type, distance, inference_name) | 
**primary** | **bool** | True if this is the primary output (short address allowed) | [optional] [default to False]

## Example

```python
from mixpeek.models.collection_feature_descriptor import CollectionFeatureDescriptor

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionFeatureDescriptor from a JSON string
collection_feature_descriptor_instance = CollectionFeatureDescriptor.from_json(json)
# print the JSON string representation of the object
print(CollectionFeatureDescriptor.to_json())

# convert the object into a dict
collection_feature_descriptor_dict = collection_feature_descriptor_instance.to_dict()
# create an instance of CollectionFeatureDescriptor from a dict
collection_feature_descriptor_from_dict = CollectionFeatureDescriptor.from_dict(collection_feature_descriptor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


