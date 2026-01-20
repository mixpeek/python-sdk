# StageParamsSortRelevance

Configuration for re-sorting documents by relevance score.  **Stage Category**: SORT  **Transformation**: N documents → N documents (same docs, different order, same schema)  **Purpose**: Reorders documents in the pipeline based on their relevance scores. This stage does NOT add/remove documents - it only changes their order.  **When to Use**:     - After SEARCH stages to reorder results by their similarity scores     - After multiple SEARCH stages are merged to apply final relevance ordering     - When you need to sort by a custom score field (not just top-level score)     - To apply consistent ordering after filtering operations  **When NOT to Use**:     - For initial document retrieval (use FILTER stages: hybrid_search)     - For removing documents (use FILTER stages: attribute_filter, llm_filter)     - For sorting by non-score attributes (use sort_attribute instead)     - For enriching documents (use APPLY stages)  **Operational Behavior**:     - Operates on in-memory document results (no database queries)     - Maintains all documents, just changes their order     - Fast operation (simple in-memory sort)     - Does not change document count or schema  **Common Pipeline Position**: FILTER → SORT (this stage) → APPLY  Requirements:     - score_field: OPTIONAL, defaults to \"score\"     - direction: OPTIONAL, defaults to descending (highest scores first)     - feature_address: OPTIONAL, for computing similarity when scores missing     - missing_score: OPTIONAL, controls placement of documents without scores  Use Cases:     - Standard relevance ranking: Sort search results by similarity scores     - Custom scoring: Sort by model-specific scores (metadata.rerank_score)     - Multi-stage pipelines: Final ordering after complex filtering     - Hybrid search: Order fused results by combined scores

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**score_field** | **str** | OPTIONAL. Document field path to use for sorting. Defaults to top-level &#39;score&#39; field populated by SEARCH stages. Use dot notation for nested fields (e.g., &#39;metadata.rerank_score&#39;). Supports template expressions for dynamic field selection. | [optional] [default to 'score']
**direction** | [**SortDirection**](SortDirection.md) | OPTIONAL. Sort direction for relevance scores. &#39;desc&#39; (default): Highest scores first (most relevant). &#39;asc&#39;: Lowest scores first (least relevant, rarely used). | [optional] 
**feature_address** | **str** | OPTIONAL. Feature address to compute similarity when scores are missing. If a document lacks the score_field, the system can compute similarity using this feature and the query embedding from earlier SEARCH stages. Format: &#39;mixpeek://extractor@version/output&#39;. NOT REQUIRED - only use when expecting missing scores and want to compute them. | [optional] [default to 'null']
**missing_score** | **str** | OPTIONAL. How to handle documents without a score_field value. &#39;bottom&#39; (default): Place at end of results (lowest priority). &#39;top&#39;: Place at start of results (highest priority, rarely used). &#39;preserve&#39;: Keep in original position (maintain insertion order). | [optional] [default to 'bottom']

## Example

```python
from mixpeek.models.stage_params_sort_relevance import StageParamsSortRelevance

# TODO update the JSON string below
json = "{}"
# create an instance of StageParamsSortRelevance from a JSON string
stage_params_sort_relevance_instance = StageParamsSortRelevance.from_json(json)
# print the JSON string representation of the object
print(StageParamsSortRelevance.to_json())

# convert the object into a dict
stage_params_sort_relevance_dict = stage_params_sort_relevance_instance.to_dict()
# create an instance of StageParamsSortRelevance from a dict
stage_params_sort_relevance_from_dict = StageParamsSortRelevance.from_dict(stage_params_sort_relevance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


