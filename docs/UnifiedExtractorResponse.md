# UnifiedExtractorResponse

Unified extractor response combining builtin and custom plugins.  This model provides a consistent view of all extractors available to a namespace, regardless of whether they are builtin or custom.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_extractor_name** | **str** | Name of the feature extractor | 
**version** | **str** | Version of the feature extractor | 
**feature_extractor_id** | **str** | Unique identifier (name_version) | 
**source** | [**ExtractorSource**](ExtractorSource.md) | Origin of this extractor: &#39;builtin&#39; (shipped with Mixpeek), &#39;custom&#39; (user-uploaded plugin), or &#39;community&#39; (marketplace) | 
**description** | **str** | Human-readable description | 
**icon** | **str** | Lucide-react icon name for frontend rendering | [optional] [default to 'box']
**input_schema** | **object** | JSON schema for input data | 
**output_schema** | **object** | JSON schema for output data | 
**parameter_schema** | **object** | JSON schema for parameters | [optional] 
**supported_input_types** | **List[str]** | Supported input types (video, image, text, etc.) | [optional] 
**max_inputs** | **Dict[str, int]** | Maximum number of inputs per type | [optional] 
**default_parameters** | **object** | Default parameter values | [optional] 
**costs** | [**CostsInfo**](CostsInfo.md) | Credit cost information (builtin extractors only) | [optional] 
**required_vector_indexes** | [**List[VectorIndexDefinition]**](VectorIndexDefinition.md) | Vector indexes this extractor produces | [optional] 
**required_payload_indexes** | [**List[PayloadIndexConfigOutput]**](PayloadIndexConfigOutput.md) | Payload indexes required by this extractor | [optional] 
**position_fields** | **List[str]** | Fields that identify unique positions within output documents. Used for deterministic document ID generation. | [optional] 
**feature_uri** | **str** | Primary feature URI (e.g., mixpeek://text_extractor@v1/embedding) | [optional] 
**plugin_id** | **str** | Plugin ID (custom plugins only) | [optional] 
**deployed** | **bool** | Whether the plugin is deployed (custom plugins only) | [optional] 
**validation_status** | **str** | Validation status (custom plugins only) | [optional] 
**created_at** | **datetime** | Creation timestamp (custom plugins only) | [optional] 
**updated_at** | **datetime** | Last update timestamp (custom plugins only) | [optional] 

## Example

```python
from mixpeek.models.unified_extractor_response import UnifiedExtractorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UnifiedExtractorResponse from a JSON string
unified_extractor_response_instance = UnifiedExtractorResponse.from_json(json)
# print the JSON string representation of the object
print(UnifiedExtractorResponse.to_json())

# convert the object into a dict
unified_extractor_response_dict = unified_extractor_response_instance.to_dict()
# create an instance of UnifiedExtractorResponse from a dict
unified_extractor_response_from_dict = UnifiedExtractorResponse.from_dict(unified_extractor_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


