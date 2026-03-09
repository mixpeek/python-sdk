# FeatureModel

Response from a feature extractor.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_extractor_id** | **str** | ID of the feature extractor that produced this response | 
**payload** | **Dict[str, object]** | Metadata of the feature | [optional] 
**vectors** | [**Vectors**](Vectors.md) |  | [optional] 

## Example

```python
from mixpeek.models.feature_model import FeatureModel

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureModel from a JSON string
feature_model_instance = FeatureModel.from_json(json)
# print the JSON string representation of the object
print(FeatureModel.to_json())

# convert the object into a dict
feature_model_dict = feature_model_instance.to_dict()
# create an instance of FeatureModel from a dict
feature_model_from_dict = FeatureModel.from_dict(feature_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


