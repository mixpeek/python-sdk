# LLMLabelingInput

Configuration for LLM-based cluster labeling.  Supports multiple LLM providers with comprehensive model selection: - OpenAI: GPT-4o, GPT-4o-mini, GPT-4.1, O3-mini (best for quality) - Google: Gemini 2.5 Flash, Gemini 1.5 Flash (best for speed and cost) - Anthropic: Claude 3.5 Sonnet, Claude 3.5 Haiku (best for reasoning)  All models are defined as enums and validated at API level.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Whether to generate labels for clusters using LLM. When enabled, clusters will have semantic labels like &#39;High-Performance Laptops&#39; instead of generic labels like &#39;Cluster 0&#39;. | [optional] [default to False]
**labeling_inputs** | [**LLMLabelingInputInput**](LLMLabelingInputInput.md) | Input configuration for LLM labeling. Supports flexible input mappings for multimodal inputs (text, images, videos, audio). Use input_mappings for advanced multimodal labeling with providers like Gemini. If not provided (null/undefined), the full document payload will be serialized as JSON and sent to the LLM, providing complete context for semantic labeling. | [optional] 
**provider** | [**LLMProvider**](LLMProvider.md) | LLM provider to use for labeling. Supported providers: - openai: GPT models (GPT-4o, GPT-4o-mini, GPT-4.1, O3-mini) - google: Gemini models (Gemini 2.5 Flash, Gemini 1.5 Flash) - anthropic: Claude models (Claude 3.5 Sonnet, Claude 3.5 Haiku)  If not specified, automatically inferred from model_name. | [optional] 
**model_name** | [**ModelName**](ModelName.md) |  | [optional] 
**include_summary** | **bool** | Whether to generate cluster summaries | [optional] [default to True]
**include_keywords** | **bool** | Whether to extract keywords for clusters | [optional] [default to True]
**max_samples_per_cluster** | **int** | Maximum representative documents to send to LLM per cluster for semantic analysis | [optional] [default to 10]
**sample_text_max_length** | **int** | Maximum characters per document sample text | [optional] [default to 200]
**use_embedding_dedup** | **bool** | Enable embedding-based label deduplication to prevent near-duplicate labels (requires sentence-transformers) | [optional] [default to False]
**embedding_similarity_threshold** | **float** | Cosine similarity threshold for duplicate label detection (labels above this are considered duplicates) | [optional] [default to 0.8]
**cache_ttl_seconds** | **int** | Time-to-live for cached labels in seconds. Labels for clusters with identical representative documents will be reused within this TTL window, reducing LLM API costs. Default: 604800 (7 days). Set to 0 to disable caching. | [optional] [default to 604800]
**custom_prompt** | **str** | OPTIONAL. Custom prompt template for LLM labeling. NOT REQUIRED - uses default discriminative prompt if not provided. When provided, completely replaces the default prompt. Your custom prompt receives cluster information but you must format it yourself. Use when:   - Need domain-specific labeling (e.g., medical, legal, technical)   - Want different label format (e.g., emoji labels, code names)   - Require specific output structure   - Have custom business logic for categorization Default prompt includes: cluster document samples, forbidden labels for uniqueness, and JSON response format. See engine/clusters/labeling/prompts.py for reference. Example: &#39;Analyze these product clusters and generate SHORT category names (2-3 words max) focusing on product type and price range. Return JSON: [{\&quot;cluster_id\&quot;: \&quot;cl_0\&quot;, \&quot;label\&quot;: \&quot;...\&quot;}]&#39; | [optional] 
**response_shape** | [**ResponseShape**](ResponseShape.md) |  | [optional] 
**parameters** | **Dict[str, object]** | Provider-specific parameters forwarded to the LLM service. For OpenAI: temperature, max_tokens, top_p, json_output, etc. For Google: temperature, top_k, max_output_tokens, json_output, etc. | [optional] 

## Example

```python
from mixpeek.models.llm_labeling_input import LLMLabelingInput

# TODO update the JSON string below
json = "{}"
# create an instance of LLMLabelingInput from a JSON string
llm_labeling_input_instance = LLMLabelingInput.from_json(json)
# print the JSON string representation of the object
print(LLMLabelingInput.to_json())

# convert the object into a dict
llm_labeling_input_dict = llm_labeling_input_instance.to_dict()
# create an instance of LLMLabelingInput from a dict
llm_labeling_input_from_dict = LLMLabelingInput.from_dict(llm_labeling_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


