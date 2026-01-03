# RetrieverExecutionSummary

Summary document used for execution history listings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**execution_id** | **str** | Execution identifier | 
**status** | **str** | Execution status | 
**created_at** | **datetime** | Creation timestamp | 
**completed_at** | **datetime** | Completion timestamp when available | [optional] 
**duration_ms** | **float** | Total execution time in ms | 
**credits_used** | **float** | Credits consumed | 
**total_processed** | **int** | Documents processed across stages | 
**total_returned** | **int** | Documents returned to caller | 
**cache_hit_rate** | **float** | Average cache hit rate for stages | [optional] 
**inputs_hash** | **str** | Stable hash of retriever inputs for dedupe | [optional] 
**query_summary** | **str** | Representative snippet of query inputs | [optional] 

## Example

```python
from mixpeek.models.retriever_execution_summary import RetrieverExecutionSummary

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieverExecutionSummary from a JSON string
retriever_execution_summary_instance = RetrieverExecutionSummary.from_json(json)
# print the JSON string representation of the object
print(RetrieverExecutionSummary.to_json())

# convert the object into a dict
retriever_execution_summary_dict = retriever_execution_summary_instance.to_dict()
# create an instance of RetrieverExecutionSummary from a dict
retriever_execution_summary_from_dict = RetrieverExecutionSummary.from_dict(retriever_execution_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


