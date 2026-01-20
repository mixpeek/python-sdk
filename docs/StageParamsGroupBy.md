# StageParamsGroupBy

Configuration for grouping documents by field value.  Stage Category: REDUCE  Transformation: N documents → M groups (where M ≤ N)  Purpose: Groups documents by a common field value, aggregating chunks back to parent objects. Essential for decompose/recompose workflows where chunks are searched individually then grouped to show context.  Performance: Runs in API layer (fast stage, ~10-50ms for 100-500 docs). Integrates with optimizer for filter push-down before grouping. Future optimization will push grouping into Qdrant for 10-100x speedup.  When to Use:     - After chunk-level search to group back to objects     - To deduplicate results by a field     - To aggregate related documents     - For decompose→search→recompose workflows     - Show top N results per category/author/parent  When NOT to Use:     - For initial document retrieval (use FILTER stages: hybrid_search)     - For ordering documents (use SORT stages: sort_relevance)     - For enriching documents (use APPLY stages: document_enrich)     - For expanding documents (use APPLY 1-N stages: taxonomy_enrich)  Operational Behavior:     - Fast stage: runs in API layer (no Engine delegation)     - In-memory grouping: Python dict-based grouping     - Groups documents with same field value     - Sorts within groups by score (highest first)     - Limits documents per group (configurable)     - Reports metrics to ClickHouse for learned optimizations  Common Pipeline Position: FILTER → SORT → REDUCE (this stage)  Requirements:     - group_by_field: REQUIRED     - max_per_group: OPTIONAL, defaults to 10     - output_mode: OPTIONAL, defaults to \"all\"  Use Cases:     - Decompose/recompose: Search 50 scenes, group to 10 videos     - Deduplication: Group by unique_id, keep top match     - Analytics: Group by category, show top docs per category     - Multi-tier results: Show top 3 products per brand  Examples:     - Group video scenes back to parent videos     - Deduplicate search results by product_id     - Show top 3 articles per author     - Display best match per category

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_by_field** | **str** | Field path to group documents by using dot notation. Documents with the same field value are grouped together. Common fields: &#39;source_object_id&#39; (parent object from decomposition), &#39;root_object_id&#39; (top-level ancestor in hierarchy), &#39;metadata.category&#39; (nested categorical field), &#39;video_id&#39; (media grouping), &#39;product_id&#39; (e-commerce). Use dot notation for nested fields: &#39;metadata.user_id&#39;, &#39;lineage.source_id&#39;. Performance: Indexed fields are faster for future Qdrant native grouping optimization. Template support: Use {{inputs.group_field}} for dynamic grouping. | [optional] [default to 'source_object_id']
**max_per_group** | **int** | OPTIONAL. Maximum number of documents to keep per group. Documents are sorted by score (highest first) before limiting. Default: 10. Use 1 for deduplication (keeps only highest scoring doc per group). Use 3-5 for preview results (show top chunks per parent). Use 50+ for comprehensive results (show many chunks per parent). Performance: Lower values reduce response size and improve latency. Typical values: 1 (dedup), 5 (preview), 10 (default), 20 (detailed), 50 (comprehensive). | [optional] [default to 10]
**output_mode** | **str** | OPTIONAL. Controls what documents are returned per group. &#39;first&#39;: Return only the top document per group (deduplication, fastest).          Use for: unique results per group (e.g., one video per brand). &#39;all&#39;: Return all documents grouped by field (default, shows full context).        Use for: showing chunks within each parent object. &#39;flatten&#39;: Return all documents as flat list (loses group structure).            Use for: need all docs but don&#39;t care about grouping metadata. Default: &#39;all&#39;. Performance: &#39;first&#39; is fastest (smallest response), &#39;all&#39; preserves grouping, &#39;flatten&#39; is lightest (no group metadata). | [optional] [default to 'all']

## Example

```python
from mixpeek.models.stage_params_group_by import StageParamsGroupBy

# TODO update the JSON string below
json = "{}"
# create an instance of StageParamsGroupBy from a JSON string
stage_params_group_by_instance = StageParamsGroupBy.from_json(json)
# print the JSON string representation of the object
print(StageParamsGroupBy.to_json())

# convert the object into a dict
stage_params_group_by_dict = stage_params_group_by_instance.to_dict()
# create an instance of StageParamsGroupBy from a dict
stage_params_group_by_from_dict = StageParamsGroupBy.from_dict(stage_params_group_by_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


