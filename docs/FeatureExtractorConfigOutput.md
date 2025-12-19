# FeatureExtractorConfigOutput

Configuration for a feature extractor.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_extractor_name** | **str** | Name of the feature extractor | 
**version** | **str** | Version of the feature extractor | 
**parameters** | [**Dict[str, ParametersValue]**](ParametersValue.md) | Parameters for the feature extractor | [optional] 
**input_mappings** | [**InputMappings**](InputMappings.md) |  | [optional] 
**feature_extractor_id** | **str** | Construct unique identifier for the feature extractor instance (name + version). | [readonly] 

## Example

```python
from mixpeek.models.feature_extractor_config_output import FeatureExtractorConfigOutput

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureExtractorConfigOutput from a JSON string
feature_extractor_config_output_instance = FeatureExtractorConfigOutput.from_json(json)
# print the JSON string representation of the object
print(FeatureExtractorConfigOutput.to_json())

# convert the object into a dict
feature_extractor_config_output_dict = feature_extractor_config_output_instance.to_dict()
# create an instance of FeatureExtractorConfigOutput from a dict
feature_extractor_config_output_from_dict = FeatureExtractorConfigOutput.from_dict(feature_extractor_config_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


