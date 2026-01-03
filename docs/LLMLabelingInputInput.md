# LLMLabelingInputInput

Input configuration for LLM-based cluster labeling.  Supports flexible input mappings similar to retrievers and buckets, allowing multimodal inputs (text, images, videos, audio) for providers like Gemini that support native multimodal understanding.  Examples:     # Text-only labeling:     LLMLabelingInput(input_mappings=[         InputMapping(input_key=\"headline\", source_type=\"payload\", path=\"headline\"),         InputMapping(input_key=\"description\", source_type=\"payload\", path=\"description\")     ])      # Multimodal labeling with images:     LLMLabelingInput(input_mappings=[         InputMapping(input_key=\"text\", source_type=\"payload\", path=\"headline\"),         InputMapping(input_key=\"image_url\", source_type=\"payload\", path=\"thumbnail_url\")     ])      # Multimodal with video (for Gemini):     LLMLabelingInput(input_mappings=[         InputMapping(input_key=\"text\", source_type=\"payload\", path=\"description\"),         InputMapping(input_key=\"video_url\", source_type=\"payload\", path=\"video_url\")     ])

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_mappings** | [**List[InputMapping]**](InputMapping.md) | Flexible input mappings for constructing LLM context. Supports multimodal inputs (text, image_url, video_url, audio_url). Each mapping specifies how to extract data from document payloads. At least one input mapping is required. | 

## Example

```python
from mixpeek.models.llm_labeling_input_input import LLMLabelingInputInput

# TODO update the JSON string below
json = "{}"
# create an instance of LLMLabelingInputInput from a JSON string
llm_labeling_input_input_instance = LLMLabelingInputInput.from_json(json)
# print the JSON string representation of the object
print(LLMLabelingInputInput.to_json())

# convert the object into a dict
llm_labeling_input_input_dict = llm_labeling_input_input_instance.to_dict()
# create an instance of LLMLabelingInputInput from a dict
llm_labeling_input_input_from_dict = LLMLabelingInputInput.from_dict(llm_labeling_input_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


