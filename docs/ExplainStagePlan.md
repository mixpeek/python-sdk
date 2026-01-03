# ExplainStagePlan

Stage-level execution plan details for retriever explain endpoint.  Provides detailed cost, performance, and optimization information for a single stage in the retriever pipeline. Use this to understand stage behavior, identify bottlenecks, and troubleshoot performance issues.  This is analogous to a single row in MongoDB's explain plan output, showing how documents flow through the stage and what resources are consumed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stage_index** | **int** | Zero-based position of this stage in the execution pipeline. Stages execute sequentially in this order. REQUIRED. | 
**stage_name** | **str** | Human-readable name of this stage instance. Corresponds to the &#39;stage_name&#39; field in your retriever configuration. Use this to map explain plan output back to your pipeline definition. REQUIRED. | 
**stage_type** | **str** | Stage type identifier indicating the category of operation. Common types: &#39;filter&#39; (reduce documents), &#39;sort&#39; (reorder), &#39;reduce&#39; (aggregate), &#39;apply&#39; (transform/enrich). REQUIRED. | 
**estimated_input** | **int** | Estimated number of documents entering this stage. This is the output count from the previous stage (or initial collection size). Used to project document flow through the pipeline. REQUIRED. | 
**estimated_output** | **int** | Estimated number of documents leaving this stage. For filter stages, this is typically less than estimated_input. For sort/reduce stages, this may be the same or less. REQUIRED. | 
**estimated_efficiency** | **float** | Stage selectivity ratio (estimated_output / estimated_input). Values closer to 0 indicate aggressive filtering. Values closer to 1 indicate most documents pass through. Use this to identify stages that might be too restrictive or too permissive. REQUIRED. | 
**estimated_cost_credits** | **float** | Estimated credit cost for executing this stage. Credits are consumed for inference (embeddings, LLM calls), vector searches, and other computational operations. Filter/sort stages typically have near-zero cost. REQUIRED. | 
**estimated_duration_ms** | **float** | Estimated latency contribution of this stage in milliseconds. High values indicate potential bottlenecks. Sum across stages gives total estimated execution time. REQUIRED. | 
**cache_likely** | **bool** | Whether this stage is likely to hit cache based on recent execution history. True &#x3D; cache hit likely (near-zero actual latency/cost). False &#x3D; cache miss likely (full cost incurred). Use this to understand when queries will be fast vs slow. REQUIRED. | 
**optimization_notes** | **List[str]** | Human-readable notes about optimizations applied to this stage. Examples: &#39;Pushed down from stage 2&#39;, &#39;Merged with previous filter&#39;, &#39;Grouping pushed to database layer&#39;. Empty if no optimizations were applied. OPTIONAL. | [optional] 
**warnings** | **List[str]** | Performance warnings or potential issues with this stage. Examples: &#39;High cost stage - consider reducing limit&#39;, &#39;Very low efficiency - may need filter tuning&#39;, &#39;LLM stage without prior filtering - expensive&#39;. Empty if no warnings. OPTIONAL. | [optional] 

## Example

```python
from mixpeek.models.explain_stage_plan import ExplainStagePlan

# TODO update the JSON string below
json = "{}"
# create an instance of ExplainStagePlan from a JSON string
explain_stage_plan_instance = ExplainStagePlan.from_json(json)
# print the JSON string representation of the object
print(ExplainStagePlan.to_json())

# convert the object into a dict
explain_stage_plan_dict = explain_stage_plan_instance.to_dict()
# create an instance of ExplainStagePlan from a dict
explain_stage_plan_from_dict = ExplainStagePlan.from_dict(explain_stage_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


