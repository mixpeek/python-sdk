# AdhocExecutionSummary

Summary of an ad-hoc retriever execution from ClickHouse.  Provides high-level execution metadata for ad-hoc retrievers without full document results. Used for listing and filtering execution history.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**execution_id** | **str** | Unique execution identifier. | 
**execution_mode** | **str** | Execution mode (&#39;adhoc&#39;). | 
**status** | **str** | Execution status (&#39;completed&#39;, &#39;failed&#39;, etc.). | 
**timestamp** | **object** |  | 
**duration_ms** | **float** | Total execution duration in milliseconds. | 
**credits_used** | **float** | Credits consumed during execution. | 
**total_processed** | **int** | Total documents processed across all stages. | 
**total_returned** | **int** | Number of documents returned in final results. | 
**cache_hit_rate** | **float** | Cache hit rate across stages (0.0-1.0). | [optional] 
**query_summary** | **str** | Brief summary of the query inputs. | [optional] 
**stages_completed** | **int** | Number of stages completed. | 
**total_stages** | **int** | Total number of stages in the pipeline. | 
**collection_ids** | **List[str]** | Collections queried during execution. | [optional] 

## Example

```python
from mixpeek.models.adhoc_execution_summary import AdhocExecutionSummary

# TODO update the JSON string below
json = "{}"
# create an instance of AdhocExecutionSummary from a JSON string
adhoc_execution_summary_instance = AdhocExecutionSummary.from_json(json)
# print the JSON string representation of the object
print(AdhocExecutionSummary.to_json())

# convert the object into a dict
adhoc_execution_summary_dict = adhoc_execution_summary_instance.to_dict()
# create an instance of AdhocExecutionSummary from a dict
adhoc_execution_summary_from_dict = AdhocExecutionSummary.from_dict(adhoc_execution_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


