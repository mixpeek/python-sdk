# TextExtractorParams

Parameters for the text extractor.  The text extractor generates dense vector embeddings optimized for semantic similarity search. It uses the E5-Large multilingual model to convert text into 1024-dimensional vectors.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extractor_type** | **str** | Discriminator field for parameter type identification. | [optional] [default to 'text_extractor']
**split_by** | [**TextSplitStrategy**](TextSplitStrategy.md) | Strategy for splitting text into multiple documents. | [optional] 
**chunk_size** | **int** | Target size for each chunk. | [optional] [default to 1000]
**chunk_overlap** | **int** | Number of units to overlap between consecutive chunks. | [optional] [default to 0]
**response_shape** | [**ResponseShape2**](ResponseShape2.md) |  | [optional] 
**llm_provider** | **str** | LLM provider for structured extraction (openai, google, anthropic). | [optional] 
**llm_model** | **str** | Specific LLM model for structured extraction. | [optional] 
**llm_api_key** | **str** | API key for LLM operations (BYOK - Bring Your Own Key). Supports: - Direct key: &#39;sk-proj-abc123...&#39; - Secret reference: &#39;{{SECRET.openai_api_key}}&#39;  When using secret reference, the key is loaded from your organization&#39;s secrets vault at runtime. Store secrets via POST /v1/organizations/secrets.  If not provided, uses Mixpeek&#39;s default API keys. | [optional] 

## Example

```python
from mixpeek.models.text_extractor_params import TextExtractorParams

# TODO update the JSON string below
json = "{}"
# create an instance of TextExtractorParams from a JSON string
text_extractor_params_instance = TextExtractorParams.from_json(json)
# print the JSON string representation of the object
print(TextExtractorParams.to_json())

# convert the object into a dict
text_extractor_params_dict = text_extractor_params_instance.to_dict()
# create an instance of TextExtractorParams from a dict
text_extractor_params_from_dict = TextExtractorParams.from_dict(text_extractor_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


