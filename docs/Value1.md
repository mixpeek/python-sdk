# Value1

Content input with auto-detection. System auto-detects format: - list of floats → used as raw embedding vector (no inference) - data:mime/type;base64,... → decoded as base64 data URI (RECOMMENDED for reliability) - http://, https://, s3:// → fetched as URL - Otherwise → treated as raw base64 string. NOTE: Base64 data URIs are recommended over URLs for multimodal embeddings because some URLs may fail if the embedding provider cannot fetch them directly. Supports template variables: {{INPUT.field_name}}.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from mixpeek.models.value1 import Value1

# TODO update the JSON string below
json = "{}"
# create an instance of Value1 from a JSON string
value1_instance = Value1.from_json(json)
# print the JSON string representation of the object
print(Value1.to_json())

# convert the object into a dict
value1_dict = value1_instance.to_dict()
# create an instance of Value1 from a dict
value1_from_dict = Value1.from_dict(value1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


