# ResponseShape2

OPTIONAL. Define custom structured output using LLM extraction. NOT REQUIRED - by default, only embeddings are generated. When provided, LLM will extract structured data matching this schema.   Two modes supported: 1. Natural language prompt (string): Describe desired output in plain English    - Service automatically infers JSON schema from your description    - Example: 'Extract key entities, sentiment (positive/negative/neutral), and main topics'    - Auto-generates schema with appropriate types (string, array, etc.)  2. Explicit JSON schema (dict): Provide complete JSON schema for output structure    - Full control over output structure, types, and constraints    - Example: {'type': 'object', 'properties': {'entities': {'type': 'array', ...}}}   Use when:   - Need to extract entities, relationships, sentiment from text   - Want structured summaries with custom fields   - Require classification into custom taxonomies   - Have domain-specific extraction requirements   Output fields are automatically added to collection schema and stored in document metadata. Note: Adds LLM latency - only use when structured extraction is needed. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from mixpeek.models.response_shape2 import ResponseShape2

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseShape2 from a JSON string
response_shape2_instance = ResponseShape2.from_json(json)
# print the JSON string representation of the object
print(ResponseShape2.to_json())

# convert the object into a dict
response_shape2_dict = response_shape2_instance.to_dict()
# create an instance of ResponseShape2 from a dict
response_shape2_from_dict = ResponseShape2.from_dict(response_shape2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


