# StageDefsContentQueryInput

Content-based query input with automatic format detection.  System auto-detects content format: - data:mime/type;base64,... → decoded as base64 data URI (RECOMMENDED) - http://, https://, s3:// → fetched as URL - Otherwise → treated as raw base64 string  **IMPORTANT - Base64 Data URIs Are Recommended for Reliability:** When using multimodal embeddings (e.g., Vertex AI multimodal), base64 data URIs (``data:image/jpeg;base64,...``) are the most reliable input format. Direct HTTP URLs may fail if the upstream embedding provider cannot fetch them (e.g., due to geo-restrictions, rate limiting, authentication requirements, or redirects). For best results, fetch the image/video client-side and send a base64 data URI.  Use Cases:     - Visual search with image/video content     - Reverse image search     - Multimodal search with content     - Template-based content queries  Examples:     Base64 data URI (RECOMMENDED - most reliable):         ```json         {\"input_mode\": \"content\", \"value\": \"data:image/jpeg;base64,/9j/...\"}         ```      Image URL (may fail if provider cannot fetch the URL):         ```json         {\"input_mode\": \"content\", \"value\": \"https://example.com/image.jpg\"}         ```      Template-based:         ```json         {\"input_mode\": \"content\", \"value\": \"{{INPUT.image_url}}\"}         ```      Legacy syntax (backward compatible):         ```json         {\"input_mode\": \"content\", \"content\": {\"url\": \"https://...\"}}         ```

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_mode** | **str** | Discriminator field. Always &#39;content&#39; for content-based queries. | [optional] [default to 'content']
**value** | [**Value1**](Value1.md) |  | [optional] 
**content** | [**StageDefsContentInput**](StageDefsContentInput.md) | Legacy content input (DEPRECATED - use &#39;value&#39; instead). Provide URL or base64 separately via ContentInput model. | [optional] 

## Example

```python
from mixpeek.models.stage_defs_content_query_input import StageDefsContentQueryInput

# TODO update the JSON string below
json = "{}"
# create an instance of StageDefsContentQueryInput from a JSON string
stage_defs_content_query_input_instance = StageDefsContentQueryInput.from_json(json)
# print the JSON string representation of the object
print(StageDefsContentQueryInput.to_json())

# convert the object into a dict
stage_defs_content_query_input_dict = stage_defs_content_query_input_instance.to_dict()
# create an instance of StageDefsContentQueryInput from a dict
stage_defs_content_query_input_from_dict = StageDefsContentQueryInput.from_dict(stage_defs_content_query_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


