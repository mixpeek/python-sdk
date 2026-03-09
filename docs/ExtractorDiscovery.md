# ExtractorDiscovery

Feature extractor discovery information.  Provides comprehensive information about a feature extractor for agent-driven configuration and manifest generation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Feature extractor name (e.g., &#39;multimodal_extractor&#39;) | 
**version** | **str** | Feature extractor version (e.g., &#39;v1&#39;) | 
**description** | **str** | Human-readable description of what this extractor does | 
**supported_modalities** | **List[str]** | List of supported input modalities (text, image, video, audio) | [optional] 
**output_features** | **List[Dict[str, object]]** | List of features produced by this extractor | [optional] 
**input_schema** | **Dict[str, object]** | JSON Schema for extractor input parameters | [optional] 
**example_usage** | **Dict[str, object]** | Example manifest YAML snippet showing how to use this extractor | [optional] 

## Example

```python
from mixpeek.models.extractor_discovery import ExtractorDiscovery

# TODO update the JSON string below
json = "{}"
# create an instance of ExtractorDiscovery from a JSON string
extractor_discovery_instance = ExtractorDiscovery.from_json(json)
# print the JSON string representation of the object
print(ExtractorDiscovery.to_json())

# convert the object into a dict
extractor_discovery_dict = extractor_discovery_instance.to_dict()
# create an instance of ExtractorDiscovery from a dict
extractor_discovery_from_dict = ExtractorDiscovery.from_dict(extractor_discovery_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


