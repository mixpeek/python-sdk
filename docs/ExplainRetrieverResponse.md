# ExplainRetrieverResponse

Execution plan analysis for a retriever.  Provides comprehensive diagnostics about retriever execution characteristics without actually running the query. Similar to MongoDB's explain plan or SQL's EXPLAIN command, this helps troubleshoot performance, estimate costs, and understand optimizer behavior.  Use Cases:     - Identify bottleneck stages before execution     - Estimate costs for budget planning     - Debug slow retrievers by analyzing stage efficiency     - Understand optimizer transformations     - Compare different retriever configurations     - Troubleshoot accuracy issues via document flow analysis

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retriever_id** | **str** | Unique identifier of the retriever being explained. REQUIRED. | 
**retriever_name** | **str** | Human-readable name of the retriever. REQUIRED. | 
**estimated_cost** | **Dict[str, float]** | Estimated total cost breakdown for executing this retriever. Contains: &#39;total_credits&#39; (credit cost), &#39;total_duration_ms&#39; (latency). Sum of all stage costs. Use for budget planning. REQUIRED. | 
**execution_plan** | [**List[ExplainStagePlan]**](ExplainStagePlan.md) | Ordered list of stage execution plans showing the OPTIMIZED pipeline. Each entry shows cost, latency, document flow, and warnings for one stage. Stages execute in this order. REQUIRED (may be empty for invalid retrievers). | [optional] 
**optimization_suggestions** | **List[Dict[str, object]]** | Actionable suggestions for improving retriever performance. Each suggestion includes: &#39;type&#39; (suggestion category), &#39;stage&#39; (affected stage name), &#39;message&#39; (human-readable description). Common types: &#39;reduce_limit&#39;, &#39;add_filter&#39;, &#39;reorder_stages&#39;, &#39;enable_cache&#39;. OPTIONAL (empty if no suggestions). | [optional] 
**total_estimated_stages** | **int** | Total number of stages in the optimized execution plan. This may differ from your original stage count if optimizations were applied. Compare with optimization_details.original_stage_count to see reduction. REQUIRED. | 
**bottleneck_stages** | **List[str]** | Names of stages expected to dominate execution time. Includes stages with duration &gt;&#x3D; 80%% of the slowest stage. Focus optimization efforts on these stages. OPTIONAL (empty if all stages have similar duration). | [optional] 
**optimization_level** | **str** | Optimization level applied by the optimizer. Values: &#39;none&#39; (no optimization), &#39;mvp&#39; (basic optimizations), &#39;advanced&#39; (all optimizations). REQUIRED. | [optional] [default to 'mvp']
**optimization_applied** | **bool** | Whether automatic pipeline optimizations were applied. When true, execution_plan shows OPTIMIZED stages (after transformations like filter push-down, stage fusion, grouping optimization). When false, execution_plan matches your original configuration. Check optimization_details to see what changed. REQUIRED. | [optional] [default to False]
**optimization_details** | **Dict[str, object]** | Detailed breakdown of optimization transformations applied. Only present when optimization_applied&#x3D;true.   Fields: - original_stage_count: Stage count before optimization - optimized_stage_count: Stage count after optimization - optimization_time_ms: Time spent on optimization (typically &lt;100ms) - stage_reduction_pct: Percentage reduction in stage count - decisions: Array of optimization decisions   Each decision contains: - rule_type: Optimization rule that fired - applied: Whether the rule was applied - reason: Human-readable explanation - stages_before/after: Stage counts before/after this rule   Common rule types: - push_down_filters: Move filters earlier to reduce downstream work - group_by_push_down: Push grouping to database layer (10-100x faster) - merge_consecutive_filters: Combine adjacent filters - eliminate_redundant_sorts: Remove duplicate sort operations   OPTIONAL (null when optimization_applied&#x3D;false). | [optional] 

## Example

```python
from mixpeek.models.explain_retriever_response import ExplainRetrieverResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExplainRetrieverResponse from a JSON string
explain_retriever_response_instance = ExplainRetrieverResponse.from_json(json)
# print the JSON string representation of the object
print(ExplainRetrieverResponse.to_json())

# convert the object into a dict
explain_retriever_response_dict = explain_retriever_response_instance.to_dict()
# create an instance of ExplainRetrieverResponse from a dict
explain_retriever_response_from_dict = ExplainRetrieverResponse.from_dict(explain_retriever_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


