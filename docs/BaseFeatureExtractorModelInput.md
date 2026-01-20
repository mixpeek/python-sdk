# BaseFeatureExtractorModelInput

Minimum feature extractor definition.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_extractor_name** | **str** | Name of the feature extractor | 
**version** | **str** | Version of the feature extractor | 
**params** | **object** | Optional extractor parameters that affect vector index configuration. Parameters set here are locked at namespace creation and determine vector dimensions in Qdrant. Collections using this extractor must use compatible params. Example: {&#39;model&#39;: &#39;siglip_base&#39;} | [optional] 

## Example

```python
from mixpeek.models.base_feature_extractor_model_input import BaseFeatureExtractorModelInput

# TODO update the JSON string below
json = "{}"
# create an instance of BaseFeatureExtractorModelInput from a JSON string
base_feature_extractor_model_input_instance = BaseFeatureExtractorModelInput.from_json(json)
# print the JSON string representation of the object
print(BaseFeatureExtractorModelInput.to_json())

# convert the object into a dict
base_feature_extractor_model_input_dict = base_feature_extractor_model_input_instance.to_dict()
# create an instance of BaseFeatureExtractorModelInput from a dict
base_feature_extractor_model_input_from_dict = BaseFeatureExtractorModelInput.from_dict(base_feature_extractor_model_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


