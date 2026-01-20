# TextQueryInput1

Text-based query input for text embedding search.  Plain text is always treated as literal text, even if it looks like a URL. Perfect for searching text that happens to contain URLs or special characters.  Use Cases:     - Semantic text search     - Question answering     - Document search by description     - Template-based text queries  Examples:     Simple text:         ```json         {\"input_mode\": \"text\", \"value\": \"machine learning best practices\"}         ```      Template-based:         ```json         {\"input_mode\": \"text\", \"value\": \"{{INPUT.user_query}}\"}         ```      Legacy syntax (backward compatible):         ```json         {\"input_mode\": \"text\", \"text\": \"machine learning\"}         ```

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_mode** | **str** | Discriminator field. Always &#39;text&#39; for text-based queries. | [optional] [default to 'text']
**value** | **str** | Plain text query string (RECOMMENDED). Always treated as literal text for embedding, even if it looks like a URL. Supports template variables: {{INPUT.field_name}}. Empty strings are allowed (creates zero vector for optional inputs). | [optional] 
**text** | **str** | Legacy text field (DEPRECATED - use &#39;value&#39; instead). Supports template variables: {{INPUT.field_name}}. | [optional] 

## Example

```python
from mixpeek.models.text_query_input1 import TextQueryInput1

# TODO update the JSON string below
json = "{}"
# create an instance of TextQueryInput1 from a JSON string
text_query_input1_instance = TextQueryInput1.from_json(json)
# print the JSON string representation of the object
print(TextQueryInput1.to_json())

# convert the object into a dict
text_query_input1_dict = text_query_input1_instance.to_dict()
# create an instance of TextQueryInput1 from a dict
text_query_input1_from_dict = TextQueryInput1.from_dict(text_query_input1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


