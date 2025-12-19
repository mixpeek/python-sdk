# BaseFeatureExtractorModelOutput

Minimum feature extractor definition.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_extractor_name** | **str** | Name of the feature extractor | 
**version** | **str** | Version of the feature extractor | 
**feature_extractor_id** | **str** | Construct unique identifier for the feature extractor instance (name + version). | [readonly] 

## Example

```python
from mixpeek.models.base_feature_extractor_model_output import BaseFeatureExtractorModelOutput

# TODO update the JSON string below
json = "{}"
# create an instance of BaseFeatureExtractorModelOutput from a JSON string
base_feature_extractor_model_output_instance = BaseFeatureExtractorModelOutput.from_json(json)
# print the JSON string representation of the object
print(BaseFeatureExtractorModelOutput.to_json())

# convert the object into a dict
base_feature_extractor_model_output_dict = base_feature_extractor_model_output_instance.to_dict()
# create an instance of BaseFeatureExtractorModelOutput from a dict
base_feature_extractor_model_output_from_dict = BaseFeatureExtractorModelOutput.from_dict(base_feature_extractor_model_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


