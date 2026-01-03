# ResponseShape1

OPTIONAL. Define custom structured output using Gemini's JSON mode. NOT REQUIRED - by default, descriptions are stored as plain text. When provided, Gemini will extract structured data matching this schema.   Two modes supported: 1. Natural language prompt (string): Describe desired output in plain English    - Gemini automatically infers JSON schema from your description    - Example: 'Extract product names, colors, and aesthetic labels'  2. Explicit JSON schema (dict): Provide complete JSON schema for output structure    - Full control over output structure, types, and constraints    - Use response_mime_type='application/json' in generation_config    - Example: {'type': 'object', 'properties': {'products': {'type': 'array', ...}}}   Use when:   - Need to extract structured product/entity information from videos   - Want consistent, parseable output format (not free-form text)   - Require specific fields like visibility_percentage, product categories, etc.   - Building e-commerce, fashion, or product discovery applications   Output fields are automatically added to collection schema and stored in document metadata. Note: When using response_shape, set description_prompt to describe the extraction task. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from mixpeek.models.response_shape1 import ResponseShape1

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseShape1 from a JSON string
response_shape1_instance = ResponseShape1.from_json(json)
# print the JSON string representation of the object
print(ResponseShape1.to_json())

# convert the object into a dict
response_shape1_dict = response_shape1_instance.to_dict()
# create an instance of ResponseShape1 from a dict
response_shape1_from_dict = ResponseShape1.from_dict(response_shape1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


