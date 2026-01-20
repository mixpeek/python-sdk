# ContentQueryInput1

Content-based query input with automatic format detection.  System auto-detects content format: - http://, https://, s3:// → fetched as URL - data:... → decoded as base64 data URI - Otherwise → treated as raw base64 string  Use Cases:     - Visual search with image/video URLs     - Reverse image search     - Multimodal search with content     - Template-based content queries  Examples:     Image URL (auto-detected):         ```json         {\"input_mode\": \"content\", \"value\": \"https://example.com/image.jpg\"}         ```      Base64 data URI (auto-detected):         ```json         {\"input_mode\": \"content\", \"value\": \"data:image/jpeg;base64,/9j/...\"}         ```      Template-based:         ```json         {\"input_mode\": \"content\", \"value\": \"{{INPUT.image_url}}\"}         ```      Legacy syntax (backward compatible):         ```json         {\"input_mode\": \"content\", \"content\": {\"url\": \"https://...\"}}         ```

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_mode** | **str** | Discriminator field. Always &#39;content&#39; for content-based queries. | [optional] [default to 'content']
**value** | **str** | Content input with auto-detection (RECOMMENDED). System auto-detects format: - http://, https://, s3:// → fetched as URL - data: → decoded as base64 data URI - Otherwise → treated as raw base64 string. Supports template variables: {{INPUT.field_name}}. | [optional] 
**content** | [**ContentInput**](ContentInput.md) | Legacy content input (DEPRECATED - use &#39;value&#39; instead). Provide URL or base64 separately via ContentInput model. | [optional] 

## Example

```python
from mixpeek.models.content_query_input1 import ContentQueryInput1

# TODO update the JSON string below
json = "{}"
# create an instance of ContentQueryInput1 from a JSON string
content_query_input1_instance = ContentQueryInput1.from_json(json)
# print the JSON string representation of the object
print(ContentQueryInput1.to_json())

# convert the object into a dict
content_query_input1_dict = content_query_input1_instance.to_dict()
# create an instance of ContentQueryInput1 from a dict
content_query_input1_from_dict = ContentQueryInput1.from_dict(content_query_input1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


