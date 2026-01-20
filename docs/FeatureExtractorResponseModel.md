# FeatureExtractorResponseModel

Feature extractor response model for API responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_extractor_name** | **str** |  | 
**version** | **str** |  | 
**feature_extractor_id** | **str** |  | 
**description** | **str** |  | 
**icon** | **str** |  | 
**source** | [**ExtractorSource**](ExtractorSource.md) | The origin/source of this extractor: &#39;builtin&#39; (shipped with Mixpeek), &#39;custom&#39; (user-created), or &#39;community&#39; (marketplace). | [optional] 
**input_schema** | **Dict[str, object]** |  | 
**output_schema** | **Dict[str, object]** |  | 
**parameter_schema** | **Dict[str, object]** |  | 
**supported_input_types** | **List[str]** |  | 
**max_inputs** | **Dict[str, int]** |  | 
**default_parameters** | **Dict[str, object]** |  | 
**costs** | [**CostsInfo**](CostsInfo.md) | Credit cost information for this extractor | [optional] 
**required_vector_indexes** | [**List[VectorIndexDefinition]**](VectorIndexDefinition.md) |  | 
**required_payload_indexes** | [**List[PayloadIndexConfigOutput]**](PayloadIndexConfigOutput.md) |  | 
**position_fields** | **List[str]** | Output fields that uniquely identify each document within a source object. Enables idempotent reprocessing: rerunning a batch produces the same document IDs, so existing documents are updated instead of creating duplicates. Works with bucket &#x60;unique_key&#x60; to enable fully deterministic document IDs. Empty list means single-output extractor (one document per source). Read-only (set by extractor). | [optional] 

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


