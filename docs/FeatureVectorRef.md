# FeatureVectorRef

Canonical reference to a feature vector produced by an extractor.  Use a canonical feature address: mixpeek://{extractor}@{version}/{output}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_address** | [**FeatureAddress**](FeatureAddress.md) | Canonical feature address: mixpeek://{extractor}@{version}/{output} | 

## Example

```python
from mixpeek.models.feature_vector_ref import FeatureVectorRef

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureVectorRef from a JSON string
feature_vector_ref_instance = FeatureVectorRef.from_json(json)
# print the JSON string representation of the object
print(FeatureVectorRef.to_json())

# convert the object into a dict
feature_vector_ref_dict = feature_vector_ref_instance.to_dict()
# create an instance of FeatureVectorRef from a dict
feature_vector_ref_from_dict = FeatureVectorRef.from_dict(feature_vector_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


