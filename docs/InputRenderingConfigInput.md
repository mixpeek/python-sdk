# InputRenderingConfigInput

Configuration for how to render an input field in the public UI.  Maps to BucketSchemaField structure for consistency with how we define input types across the system.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_name** | **str** | Name of the input field (matches retriever input_schema key) | 
**field_schema** | [**RetrieverInputSchemaFieldInput**](RetrieverInputSchemaFieldInput.md) | Schema definition for this input field. Defines type, description, examples, and validation rules. Supports all bucket types (string, number, image, etc.) plus document_reference. Frontend uses this to render the appropriate input component (text input, image upload, dropdown, etc.) | 
**input_type** | **str** | UI input component type. Determines how the input is rendered: text (single line), select (dropdown), file (upload), multiselect (multiple choice) | [optional] [default to 'text']
**label** | **str** | Human-readable label for the input | 
**placeholder** | **str** | Placeholder text for the input | [optional] 
**helper_text** | **str** | Helper text displayed below the input to guide users | [optional] 
**suggestions** | **List[str]** | Pre-filled suggestion chips that users can click to populate the input | [optional] 
**required** | **bool** | Whether this input is required | [optional] [default to True]
**order** | **int** | Display order (lower numbers appear first) | [optional] [default to 0]

## Example

```python
from mixpeek.models.input_rendering_config_input import InputRenderingConfigInput

# TODO update the JSON string below
json = "{}"
# create an instance of InputRenderingConfigInput from a JSON string
input_rendering_config_input_instance = InputRenderingConfigInput.from_json(json)
# print the JSON string representation of the object
print(InputRenderingConfigInput.to_json())

# convert the object into a dict
input_rendering_config_input_dict = input_rendering_config_input_instance.to_dict()
# create an instance of InputRenderingConfigInput from a dict
input_rendering_config_input_from_dict = InputRenderingConfigInput.from_dict(input_rendering_config_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


