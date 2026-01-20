# InternalProcessingModel

Processing and provenance tracking information.  Consolidates all processing-related metadata including source URLs, processing history, and taxonomy enrichment lineage.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_url** | **str** | Original URL before S3 mirroring (for URL-based ingestion). | [optional] 
**object_key_source** | **str** | S3 key source identifier. | [optional] 
**detected_mime_type** | **str** | MIME type detected during canonicalization. | [optional] 
**history** | **List[object]** | Processing steps history with timestamps and operations. | [optional] 
**taxonomy_lineage** | **List[object]** | Taxonomy enrichment entries applied to this document. | [optional] 
**last_health_check** | **object** | Last health check result (for batch processing). | [optional] 

## Example

```python
from mixpeek.models.internal_processing_model import InternalProcessingModel

# TODO update the JSON string below
json = "{}"
# create an instance of InternalProcessingModel from a JSON string
internal_processing_model_instance = InternalProcessingModel.from_json(json)
# print the JSON string representation of the object
print(InternalProcessingModel.to_json())

# convert the object into a dict
internal_processing_model_dict = internal_processing_model_instance.to_dict()
# create an instance of InternalProcessingModel from a dict
internal_processing_model_from_dict = InternalProcessingModel.from_dict(internal_processing_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


