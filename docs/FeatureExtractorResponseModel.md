# FeatureExtractorResponseModel

Feature extractor response model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_extractor_name** | **str** |  | 
**version** | **str** |  | 
**feature_extractor_id** | **str** |  | 
**description** | **str** |  | 
**input_schema** | **Dict[str, object]** |  | 
**output_schema** | **Dict[str, object]** |  | 
**parameter_schema** | **Dict[str, object]** |  | 
**supported_input_types** | **List[str]** |  | 
**max_inputs** | **Dict[str, int]** |  | 
**default_parameters** | **Dict[str, object]** |  | 
**document_output_type** | [**DocumentOutputType**](DocumentOutputType.md) |  | 
**document_input_handling** | [**DocumentInputHandling**](DocumentInputHandling.md) |  | 
**required_vector_indexes** | [**List[VectorIndexDefinition]**](VectorIndexDefinition.md) |  | 
**required_payload_indexes** | [**List[PayloadIndexConfigOutput]**](PayloadIndexConfigOutput.md) |  | 

## Example

```python
from mixpeek.models.feature_extractor_response_model import FeatureExtractorResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureExtractorResponseModel from a JSON string
feature_extractor_response_model_instance = FeatureExtractorResponseModel.from_json(json)
# print the JSON string representation of the object
print(FeatureExtractorResponseModel.to_json())

# convert the object into a dict
feature_extractor_response_model_dict = feature_extractor_response_model_instance.to_dict()
# create an instance of FeatureExtractorResponseModel from a dict
feature_extractor_response_model_from_dict = FeatureExtractorResponseModel.from_dict(feature_extractor_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


