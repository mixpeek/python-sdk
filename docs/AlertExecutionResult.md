# AlertExecutionResult

Result of an alert execution.  Captures the outcome of running an alert against one or more documents, including whether the alert was triggered and what matched.  Attributes:     alert_id: ID of the alert that was executed     collection_id: Collection the alert was executed against     execution_id: Unique identifier for this execution     triggered: Whether the alert was triggered (i.e., retriever returned results)     match_count: Number of matches found     matches: List of match results (if include_matches was True)     source_documents: Document IDs that triggered the alert check     executed_at: When the alert was executed     duration_ms: How long the execution took

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_id** | **str** | ID of the alert that was executed | 
**collection_id** | **str** | Collection the alert was executed against | 
**execution_id** | **str** | Unique identifier for this execution | [optional] 
**triggered** | **bool** | Whether the alert was triggered | 
**match_count** | **int** | Number of matches found | 
**matches** | [**List[AlertMatchResult]**](AlertMatchResult.md) | List of match results | [optional] 
**source_documents** | **List[str]** | Document IDs that triggered the alert check | [optional] 
**executed_at** | **str** | ISO 8601 timestamp when the alert was executed | 
**duration_ms** | **int** | How long the execution took in milliseconds | 

## Example

```python
from mixpeek.models.alert_execution_result import AlertExecutionResult

# TODO update the JSON string below
json = "{}"
# create an instance of AlertExecutionResult from a JSON string
alert_execution_result_instance = AlertExecutionResult.from_json(json)
# print the JSON string representation of the object
print(AlertExecutionResult.to_json())

# convert the object into a dict
alert_execution_result_dict = alert_execution_result_instance.to_dict()
# create an instance of AlertExecutionResult from a dict
alert_execution_result_from_dict = AlertExecutionResult.from_dict(alert_execution_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


