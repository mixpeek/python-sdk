# StageParamsLlmFilter

Configuration for delegating filtering decisions to an LLM.  **Stage Category**: FILTER  **Transformation**: N documents → ≤N documents (subset, same schema)  **Purpose**: Produces a subset of input documents using LLM-based reasoning. Use this when filtering criteria are too complex for simple attribute conditions and require semantic understanding, content analysis, or subjective judgment. Output documents have identical schema to input.  **When to Use**:     - After initial FILTER stages for intelligent content filtering     - When filtering criteria involve content understanding (sentiment, topic relevance)     - For subjective filtering (quality, appropriateness, brand alignment)     - When simple attribute filters aren't sufficient (complex policies, nuanced rules)     - To filter multimodal content (images, videos) based on visual criteria     - For dynamic filtering based on natural language criteria  **When NOT to Use**:     - For simple metadata filtering (use attribute_filter - much faster and cheaper)     - For reordering results (use SORT stages)     - For enriching documents (use APPLY stages)     - For aggregating documents (use REDUCE stages)     - When fast response time is critical (LLM calls are slow, 100ms-2s per batch)     - When cost is a major concern (LLM inference costs per document)  **Operational Behavior**:     - Operates on in-memory document results (no database queries)     - Produces subset of documents (removes those not meeting LLM criteria)     - Slow operation (LLM API calls, network latency)     - Processes documents in batches to optimize LLM calls     - Makes HTTP requests to Engine service for LLM inference     - Supports concurrent batching for throughput     - Output schema = Input schema (no schema changes)  **Common Pipeline Position**: FILTER (attribute_filter) → FILTER (this stage) → SORT  **Cost & Performance**:     - Expensive: LLM API costs per document evaluated     - Slow: 100ms-2s per batch depending on LLM and batch size     - Use batch_size to balance throughput vs latency     - Consider filtering with attribute_filter first to reduce LLM calls  Requirements:     - provider: OPTIONAL, LLM provider (openai, google, anthropic). Auto-inferred if not specified.     - model_name: OPTIONAL, specific model name. Uses provider default if not specified.     - criteria: OPTIONAL, natural language filtering description (defaults to empty string)       * If criteria is empty/null, stage is SKIPPED (all documents pass through)       * This saves 100ms-30s when no filtering is needed     - batch_size: OPTIONAL, defaults to 10 documents per batch     - max_concurrency: OPTIONAL, defaults to 5 concurrent requests  Use Cases:     - Content quality filtering: \"Keep only well-written, professional articles\"     - Sentiment filtering: \"Discard negative or controversial content\"     - Topic relevance: \"Keep only documents about enterprise SaaS\"     - Visual filtering: \"Keep only images with people smiling\"     - Policy compliance: \"Filter out any content mentioning competitors\"

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | [**LLMProvider**](LLMProvider.md) | LLM provider to use. Supported providers: - openai: GPT models (GPT-4o, GPT-4o-mini) - google: Gemini models (Gemini 2.0 Flash) - anthropic: Claude models (Claude 3.5 Sonnet/Haiku)  If not specified, defaults to &#39;google&#39;. Can be auto-inferred from model_name. | [optional] 
**model_name** | **str** | Specific LLM model to use. If not specified, uses provider default. Faster models recommended for filtering (gemini-2.0-flash, gpt-4o-mini). | [optional] [default to 'null']
**inference_name** | **str** | DEPRECATED: Use &#39;provider&#39; and &#39;model_name&#39; instead. Legacy format: &#39;provider:model&#39; (e.g., &#39;gemini:gemini-2.0-flash&#39;). Kept for backward compatibility only. | [optional] [default to 'null']
**criteria** | **str** | Natural language description of filtering criteria. The LLM will evaluate each document against this criteria. Be specific and clear about what to keep vs discard. If empty or null, the stage is skipped (all documents pass through). Supports template variables: - {INPUT.field}: From pipeline inputs - {DOC.field}: From current document Template expressions are evaluated per-document for dynamic filtering. Examples: &#39;Keep only...&#39;, &#39;Discard if...&#39;, &#39;Filter out...&#39; | [optional] [default to 'Keep only documents relevant to {{INPUT.query}}']
**include_reasoning** | **bool** | Whether to include LLM reasoning strings in stage metadata. | [optional] [default to False]
**api_key** | **str** | OPTIONAL. Bring Your Own Key (BYOK) - use your own LLM API key instead of Mixpeek&#39;s.  **How to use:** 1. Store your API key as an organization secret via POST /v1/organizations/secrets    Example: {\&quot;secret_name\&quot;: \&quot;openai_api_key\&quot;, \&quot;secret_value\&quot;: \&quot;sk-proj-...\&quot;}  2. Reference it here using template syntax: {{secrets.openai_api_key}}  **Benefits:** - Use your own API credits and rate limits - Keep your API keys secure in Mixpeek&#39;s encrypted vault - No changes needed to your retriever when rotating keys  If not provided, uses Mixpeek&#39;s default API keys (usage charged to your account). | [optional] [default to 'null']

## Example

```python
from mixpeek.models.stage_params_llm_filter import StageParamsLlmFilter

# TODO update the JSON string below
json = "{}"
# create an instance of StageParamsLlmFilter from a JSON string
stage_params_llm_filter_instance = StageParamsLlmFilter.from_json(json)
# print the JSON string representation of the object
print(StageParamsLlmFilter.to_json())

# convert the object into a dict
stage_params_llm_filter_dict = stage_params_llm_filter_instance.to_dict()
# create an instance of StageParamsLlmFilter from a dict
stage_params_llm_filter_from_dict = StageParamsLlmFilter.from_dict(stage_params_llm_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


