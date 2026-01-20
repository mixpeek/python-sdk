# ExecutionDetail

Alias wrapper for execution detail documentation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**execution_id** | **str** | REQUIRED. Unique identifier for this execution run. Use this ID to track execution status, retrieve execution details, or query execution history. Format: &#39;exec_&#39; prefix followed by alphanumeric token. | 
**status** | **str** | REQUIRED. Execution status indicating current state. Common values: &#39;completed&#39;, &#39;failed&#39;, &#39;processing&#39;, &#39;pending&#39;. Check this field to determine if execution succeeded or requires retry. | 
**documents** | **List[object]** | REQUIRED. Final document results after retriever completion. Contains documents that passed through all retriever stages. Each document may include: document_id, payload (full document data), score (relevance score), metadata (collection-specific fields), and any fields added by enrichment/join stages. Empty array indicates no documents matched the query criteria. Note: Legacy format may use &#39;final_results&#39; instead of &#39;documents&#39;. | [optional] 
**pagination** | **object** | REQUIRED. Pagination metadata structure. Format varies by pagination method: Offset pagination: {total, limit, offset, has_next, has_previous}, Cursor pagination: {cursor, has_next, page_size}, Keyset pagination: {next_cursor, has_next}. Use this to navigate through result pages. | [optional] 
**stage_statistics** | [**RetrieverExecutionStatistics**](RetrieverExecutionStatistics.md) | REQUIRED. Per-stage execution statistics including timing, document counts, cache hit rates, and stage-specific metrics. Use this to understand retriever performance and identify bottlenecks. | [optional] 
**budget** | **object** | REQUIRED. Budget usage snapshot for this execution. Contains: credits_used (credits consumed), credits_remaining (remaining budget), time_used_ms (execution time), and budget limits. Use this to track resource consumption and enforce budget limits. | [optional] 
**error** | **str** | OPTIONAL. Retriever-level error message if execution failed. Only present when status&#x3D;&#39;failed&#39;. Contains human-readable error description to help diagnose the failure. Check stage_statistics for stage-specific errors. | [optional] 
**optimization_applied** | **bool** | OPTIONAL. Whether automatic pipeline optimizations were applied before execution. Mixpeek automatically optimizes retrieval pipelines for performance by reordering stages, merging operations, and pushing work to the database layer. Optimizations preserve logical equivalence - you get the same results, just faster. When true, see optimization_summary for details about what changed. | [optional] [default to False]
**optimization_summary** | **object** | OPTIONAL. Summary of pipeline optimizations applied before execution. Only present when optimization_applied&#x3D;true. Contains: - original_stage_count: Number of stages in your original pipeline - optimized_stage_count: Number of stages after optimization - optimization_time_ms: Time spent optimizing (typically &lt;100ms) - rules_applied: List of optimization rules that fired - stage_reduction_pct: Percentage reduction in stage count Use this to understand how the optimizer improved your pipeline. See OptimizationRuleType enum for detailed rule descriptions. | [optional] 
**created_at** | **datetime** | Timestamp when execution began | [optional] 
**completed_at** | **datetime** | Timestamp when execution finished | [optional] 
**current_stage** | **str** | Stage currently running when execution in-flight | [optional] 
**stages_completed** | **int** | Number of stages finished so far | [optional] [default to 0]
**total_stages** | **int** | Total stages configured | [optional] [default to 0]

## Example

```python
from mixpeek.models.execution_detail import ExecutionDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ExecutionDetail from a JSON string
execution_detail_instance = ExecutionDetail.from_json(json)
# print the JSON string representation of the object
print(ExecutionDetail.to_json())

# convert the object into a dict
execution_detail_dict = execution_detail_instance.to_dict()
# create an instance of ExecutionDetail from a dict
execution_detail_from_dict = ExecutionDetail.from_dict(execution_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


