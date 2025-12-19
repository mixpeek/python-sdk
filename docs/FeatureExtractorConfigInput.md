# FeatureExtractorConfigInput

Configuration for a feature extractor.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_extractor_name** | **str** | Name of the feature extractor | 
**version** | **str** | Version of the feature extractor | 
**parameters** | [**Dict[str, ParametersValue]**](ParametersValue.md) | Parameters for the feature extractor | [optional] 
**input_mappings** | [**InputMappings**](InputMappings.md) |  | [optional] 

## Example

```python
from mixpeek.models.feature_extractor_config_input import FeatureExtractorConfigInput

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureExtractorConfigInput from a JSON string
feature_extractor_config_input_instance = FeatureExtractorConfigInput.from_json(json)
# print the JSON string representation of the object
print(FeatureExtractorConfigInput.to_json())

# convert the object into a dict
feature_extractor_config_input_dict = feature_extractor_config_input_instance.to_dict()
# create an instance of FeatureExtractorConfigInput from a dict
feature_extractor_config_input_from_dict = FeatureExtractorConfigInput.from_dict(feature_extractor_config_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


