# ExplainRetrieverRequest

Request to get execution plan for a retriever.  Provides optional hypothetical inputs to tailor the execution plan estimation. The explain endpoint analyzes your retriever configuration and returns cost/latency estimates without actually executing the query.  Use Cases:     - See how plan changes with different input values     - Estimate costs for different query patterns     - Understand impact of parameter changes (e.g., top_k)     - Test stage behavior with representative inputs  Behavior:     - If inputs are provided, they're used for tailored estimation     - If inputs are not provided, default/representative values are used     - Inputs do NOT need to match your input_schema exactly     - No actual retrieval is performed (explain is analysis only)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inputs** | **Dict[str, object]** | Hypothetical inputs for tailored execution plan estimation. These values are used to analyze stage behavior and estimate costs.   NOT REQUIRED - if omitted, default/representative values are used.   Common inputs: - &#39;query&#39;: Search query text (for semantic search stages) - &#39;top_k&#39;: Number of results to return (affects search scope) - Filter parameters: Category, price range, etc.   Examples: - {&#39;query&#39;: &#39;laptop&#39;} - Simple text query - {&#39;query&#39;: &#39;laptop&#39;, &#39;top_k&#39;: 100} - Query with custom limit - {&#39;query&#39;: &#39;laptop&#39;, &#39;category&#39;: &#39;electronics&#39;, &#39;price_max&#39;: 1000} - Query with filters   Note: Inputs are for estimation only. No actual search is performed. | [optional] 

## Example

```python
from mixpeek.models.explain_retriever_request import ExplainRetrieverRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExplainRetrieverRequest from a JSON string
explain_retriever_request_instance = ExplainRetrieverRequest.from_json(json)
# print the JSON string representation of the object
print(ExplainRetrieverRequest.to_json())

# convert the object into a dict
explain_retriever_request_dict = explain_retriever_request_instance.to_dict()
# create an instance of ExplainRetrieverRequest from a dict
explain_retriever_request_from_dict = ExplainRetrieverRequest.from_dict(explain_retriever_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


