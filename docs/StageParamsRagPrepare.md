# StageParamsRagPrepare

Configuration for RAG context preparation.  **Stage Category**: APPLY  **Transformation**: N documents → 1 context document (single_context mode)                    OR N documents → N formatted documents (formatted_list mode)  **Purpose**: Prepare search results for LLM consumption by formatting documents, managing token budgets, and adding citations. This is a preparation stage that does NOT call an LLM - it prepares content for downstream LLM stages.  **When to Use**:     - Before passing search results to an LLM for RAG     - When you need to fit multiple documents into a token budget     - When you need citation tracking for source attribution     - When you need consistent document formatting  **When NOT to Use**:     - When you want the LLM to generate a summary (use summarize stage)     - When you don't need token management     - For simple pass-through of documents  **Output Modes**:     - `single_context`: Combines all documents into one context string     - `formatted_list`: Returns individually formatted documents  **Common Pipeline Position**: feature_search → rerank → rag_prepare → (external LLM call)  Examples:     Basic context preparation:         ```json         {             \"max_tokens\": 8000,             \"output_mode\": \"single_context\"         }         ```      Custom document formatting with citations:         ```json         {             \"max_tokens\": 4000,             \"document_template\": \"[{{CONTEXT.INDEX}}] {{DOC.metadata.title}}\\n{{DOC.content}}\\n\",             \"citation\": {\"style\": \"numbered\", \"include_title\": true}         }         ```      Formatted list for custom processing:         ```json         {             \"output_mode\": \"formatted_list\",             \"document_template\": \"Source: {{DOC.metadata.source}}\\n{{DOC.content}}\"         }         ```

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_tokens** | **int** | OPTIONAL. Maximum tokens for the combined context output. Documents exceeding this limit are handled by truncation_strategy. Default: 8000 (safe for most models). | [optional] [default to 8000]
**tokenizer** | **str** | OPTIONAL. Tokenizer to use for token counting. Default: &#39;cl100k_base&#39; (GPT-4/GPT-3.5 tokenizer). Options: &#39;cl100k_base&#39;, &#39;p50k_base&#39;, &#39;r50k_base&#39;, &#39;gpt2&#39; | [optional] [default to 'cl100k_base']
**truncation_strategy** | **str** | OPTIONAL. How to handle documents exceeding max_tokens: - &#39;priority_truncate&#39;: Include docs in score order, truncate last to fit - &#39;proportional&#39;: Give each doc proportional token budget based on count - &#39;drop_last&#39;: Include complete docs until limit, drop remaining | [optional] [default to 'priority_truncate']
**output_mode** | **str** | OPTIONAL. Output format: - &#39;single_context&#39;: One document with combined &#39;context&#39; string + &#39;citations&#39; - &#39;formatted_list&#39;: N documents with &#39;formatted_content&#39; field each | [optional] [default to 'single_context']
**document_template** | **str** | OPTIONAL. Template for formatting each document. Available placeholders: - {{CONTEXT.INDEX}}: 1-based position in result set (1, 2, 3...) - {{CONTEXT.CITATION}}: Citation marker based on citation.style - {{DOC.*}}: Any document field (e.g., {{DOC.content}}, {{DOC.metadata.title}}) | [optional] [default to '''[{{CONTEXT.INDEX}}] {{DOC.content}}

''']
**content_field** | **str** | Primary field to extract content from each document. | [optional] [default to 'content']
**separator** | **str** | Separator between documents in single_context mode. | [optional] [default to '''
''']
**citation** | [**CitationConfig**](CitationConfig.md) | Citation configuration for source tracking. | [optional] 
**context_field** | **str** | Field name for combined context (single_context mode). | [optional] [default to 'rag_context']
**citations_field** | **str** | Field name for citation metadata. | [optional] [default to 'citations']
**formatted_content_field** | **str** | Field name for formatted content (formatted_list mode). | [optional] [default to 'formatted_content']

## Example

```python
from mixpeek.models.stage_params_rag_prepare import StageParamsRagPrepare

# TODO update the JSON string below
json = "{}"
# create an instance of StageParamsRagPrepare from a JSON string
stage_params_rag_prepare_instance = StageParamsRagPrepare.from_json(json)
# print the JSON string representation of the object
print(StageParamsRagPrepare.to_json())

# convert the object into a dict
stage_params_rag_prepare_dict = stage_params_rag_prepare_instance.to_dict()
# create an instance of StageParamsRagPrepare from a dict
stage_params_rag_prepare_from_dict = StageParamsRagPrepare.from_dict(stage_params_rag_prepare_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


