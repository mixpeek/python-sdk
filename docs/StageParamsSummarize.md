# StageParamsSummarize

Configuration for multi-document summarization.  **Stage Category**: REDUCE  **Transformation**: N documents → 1 document (or N → M with group_by)  **Purpose**: Condense multiple documents into a single summary using an LLM. Unlike llm_enrich which processes each document independently, Summarize provides all documents to the LLM in a single call, enabling cross-document synthesis and comparison.  **When to Use**:     - Generate a single answer from search results (RAG output)     - Create executive summaries from multiple sources     - Synthesize information that spans multiple documents     - Reduce result set to key findings  **When NOT to Use**:     - Adding fields to each document (use llm_enrich instead)     - Simple filtering based on content (use llm_filter instead)     - When you need to preserve individual documents  **Common Pipeline Position**: feature_search → rerank → summarize  **Template Variables**:     - `{{DOCUMENTS}}`: Formatted list of all documents (required in prompt)     - `{{DOC_COUNT}}`: Number of documents being summarized     - `{{INPUT.*}}`: Access query inputs     - `{{CONTEXT.*}}`: Access execution context  Examples:     Basic summarization:         ```json         {             \"prompt\": \"Summarize these {{DOC_COUNT}} search results:\\n\\n{{DOCUMENTS}}\",             \"provider\": \"google\",             \"model_name\": \"gemini-2.0-flash\"         }         ```      Question-answering from search results:         ```json         {             \"prompt\": \"Answer this question: {{INPUT.question}}\\n\\nBased on these documents:\\n{{DOCUMENTS}}\",             \"provider\": \"openai\",             \"model_name\": \"gpt-4o\",             \"include_sources\": true         }         ```      Per-category summarization:         ```json         {             \"prompt\": \"Summarize documents about {{GROUP_VALUE}}:\\n\\n{{DOCUMENTS}}\",             \"provider\": \"openai\",             \"model_name\": \"gpt-4o-mini\",             \"group_by\": \"metadata.category\"         }         ```

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prompt** | **str** | REQUIRED. Prompt template for the LLM. Must include {{DOCUMENTS}} placeholder.   Available placeholders: - {{DOCUMENTS}}: Formatted list of all documents - {{DOC_COUNT}}: Number of documents - {{GROUP_VALUE}}: Current group value (when using group_by) - {{INPUT.*}}: Query input values - {{CONTEXT.*}}: Execution context | [optional] [default to '''Summarize the following {{DOC_COUNT}} documents concisely:

{{DOCUMENTS}}''']
**provider** | [**LLMProvider**](LLMProvider.md) | LLM provider to use. Supported providers: - openai: GPT models (GPT-4o, GPT-4o-mini) - google: Gemini models (Gemini 2.0 Flash) - anthropic: Claude models (Claude 3.5 Sonnet/Haiku)  If not specified, defaults to &#39;google&#39;. Can be auto-inferred from model_name. | [optional] 
**model_name** | **str** | Specific LLM model to use. If not specified, uses provider default. Examples: gemini-2.0-flash, gpt-4o-mini, gpt-4o | [optional] [default to 'null']
**inference_name** | **str** | DEPRECATED: Use &#39;provider&#39; and &#39;model_name&#39; instead. Legacy format: &#39;provider:model&#39; (e.g., &#39;gemini:gemini-2.0-flash&#39;). Kept for backward compatibility only. | [optional] 
**document_template** | **str** | OPTIONAL. Template for formatting each document in {{DOCUMENTS}}. Default: &#39;[{{INDEX}}] {{DOC.content}}\\n&#39;.   Available placeholders: - {{INDEX}}: 1-based document index - {{DOC.*}}: Any document field (e.g., {{DOC.content}}, {{DOC.metadata.title}}) | [optional] [default to '''[{{INDEX}}] {{DOC.content}}
''']
**content_field** | **str** | OPTIONAL. Primary field to extract content from each document. Used when {{DOC.content}} is referenced in document_template. Supports dot notation for nested fields. | [optional] [default to 'content']
**group_by** | **str** | OPTIONAL. Field to group documents by before summarization. When set, creates one summary per unique group value (N→M transformation). When not set, creates one summary for all documents (N→1 transformation).   Use cases: - &#39;metadata.category&#39;: One summary per category - &#39;metadata.source&#39;: One summary per source - &#39;metadata.date&#39;: One summary per date | [optional] [default to 'null']
**output_field** | **str** | OPTIONAL. Field name for the summary in the output document. Default: &#39;summary&#39;. | [optional] [default to 'summary']
**include_sources** | **bool** | OPTIONAL. Include source document IDs in output. When true, adds &#39;source_document_ids&#39; field to output. Useful for citation and attribution. | [optional] [default to True]
**include_metadata** | **bool** | OPTIONAL. Include metadata about summarization in output. Adds &#39;document_count&#39;, &#39;tokens_used&#39;, etc. | [optional] [default to True]
**max_input_tokens** | **int** | OPTIONAL. Maximum tokens to use for input documents. Documents exceeding this limit are truncated using truncation_strategy. Default: 8000 (safe for most models). | [optional] [default to 8000]
**truncation_strategy** | **str** | OPTIONAL. How to handle documents exceeding max_input_tokens.   Strategies: - &#39;drop_last&#39;: Include documents in order until limit, drop remaining - &#39;truncate_each&#39;: Give each document equal token budget, truncate individually - &#39;smart&#39;: Prioritize by relevance score, truncate lower-scored documents first | [optional] [default to 'drop_last']
**temperature** | **float** | OPTIONAL. LLM temperature for summary generation. Lower values (0.1-0.3) produce more focused, deterministic summaries. Higher values (0.7-1.0) produce more creative, varied summaries. Default: 0.3 (factual summarization). | [optional] [default to 0.3]
**max_output_tokens** | **int** | OPTIONAL. Maximum tokens for the summary output. Default: 1024. | [optional] [default to 1024]
**output_schema** | **object** | OPTIONAL. JSON schema for structured output. When provided, LLM output is parsed as JSON matching this schema. | [optional] 

## Example

```python
from mixpeek.models.stage_params_summarize import StageParamsSummarize

# TODO update the JSON string below
json = "{}"
# create an instance of StageParamsSummarize from a JSON string
stage_params_summarize_instance = StageParamsSummarize.from_json(json)
# print the JSON string representation of the object
print(StageParamsSummarize.to_json())

# convert the object into a dict
stage_params_summarize_dict = stage_params_summarize_instance.to_dict()
# create an instance of StageParamsSummarize from a dict
stage_params_summarize_from_dict = StageParamsSummarize.from_dict(stage_params_summarize_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


