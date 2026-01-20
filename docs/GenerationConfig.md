# GenerationConfig

Configuration for generative models.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**candidate_count** | **int** | Number of candidate responses to generate for video description. | [optional] [default to 1]
**max_output_tokens** | **int** | Maximum number of tokens for the generated video description. | [optional] [default to 1024]
**temperature** | **float** | Controls randomness for video description generation. Higher is more random. | [optional] [default to 0.7]
**top_p** | **float** | Nucleus sampling (top-p) for video description generation. | [optional] [default to 0.8]
**response_mime_type** | **str** | MIME type for response (e.g., &#39;application/json&#39;) | [optional] 
**response_schema** | **object** | JSON schema for structured output | [optional] 

## Example

```python
from mixpeek.models.generation_config import GenerationConfig

# TODO update the JSON string below
json = "{}"
# create an instance of GenerationConfig from a JSON string
generation_config_instance = GenerationConfig.from_json(json)
# print the JSON string representation of the object
print(GenerationConfig.to_json())

# convert the object into a dict
generation_config_dict = generation_config_instance.to_dict()
# create an instance of GenerationConfig from a dict
generation_config_from_dict = GenerationConfig.from_dict(generation_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


