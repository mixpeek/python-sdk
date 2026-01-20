# Query

REQUIRED. Input for this feature search. Can be plain text, URL with auto-detection, or base64 content. For text features: Use text mode. For image/video features: Use content mode with URL or base64. Supports template variables: {{INPUT.field_name}}, {{DOC.field_name}}, etc.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_mode** | **str** | Discriminator field. Always &#39;document&#39; for document reference queries. | [optional] [default to 'document']
**value** | **str** | Content input with auto-detection (RECOMMENDED). System auto-detects format: - http://, https://, s3:// → fetched as URL - data: → decoded as base64 data URI - Otherwise → treated as raw base64 string. Supports template variables: {{INPUT.field_name}}. | [optional] 
**text** | **str** | Legacy text field (DEPRECATED - use &#39;value&#39; instead). Supports template variables: {{INPUT.field_name}}. | [optional] 
**content** | [**ContentInput**](ContentInput.md) | Legacy content input (DEPRECATED - use &#39;value&#39; instead). Provide URL or base64 separately via ContentInput model. | [optional] 
**document_ref** | [**DocumentReference**](DocumentReference.md) | Reference to existing document&#39;s pre-computed features. The system fetches the document&#39;s feature vectors for the specified feature_uri and uses them directly without re-processing. Document must exist and have features for the specified feature_uri. | 

## Example

```python
from mixpeek.models.query import Query

# TODO update the JSON string below
json = "{}"
# create an instance of Query from a JSON string
query_instance = Query.from_json(json)
# print the JSON string representation of the object
print(Query.to_json())

# convert the object into a dict
query_dict = query_instance.to_dict()
# create an instance of Query from a dict
query_from_dict = Query.from_dict(query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


