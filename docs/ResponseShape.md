# ResponseShape

OPTIONAL. Define custom structured output for LLM labeling. NOT REQUIRED - uses default structure (label, summary, keywords) if not provided. When provided, LLM output will match this structure and be stored in cluster documents.   Two modes supported: 1. Natural language prompt (string): Describe desired output in plain English    - Service automatically infers JSON schema from your description    - Example: 'Extract cluster category, confidence score (0-1), and top 3 representative terms'    - Auto-generates schema with appropriate types (string, number, array, etc.)  2. Explicit JSON schema (dict): Provide complete JSON schema for output structure    - Full control over output structure, types, and constraints    - Example: {'type': 'object', 'properties': {'category': {'type': 'string'}, ...}}   Use when:   - Need custom metadata fields (confidence scores, sentiment, complexity)   - Want domain-specific structure (taxonomy hierarchies, entity extractions)   - Require specific data types (arrays, nested objects, enums)   - Have downstream schema requirements   Output fields are automatically added to cluster collection schema and stored in metadata. Default behavior (if not provided): label (string), summary (string), keywords (array of strings) 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from mixpeek.models.response_shape import ResponseShape

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseShape from a JSON string
response_shape_instance = ResponseShape.from_json(json)
# print the JSON string representation of the object
print(ResponseShape.to_json())

# convert the object into a dict
response_shape_dict = response_shape_instance.to_dict()
# create an instance of ResponseShape from a dict
response_shape_from_dict = ResponseShape.from_dict(response_shape_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


