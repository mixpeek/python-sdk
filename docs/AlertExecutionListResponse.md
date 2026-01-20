# AlertExecutionListResponse

Response model for listing alert executions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[AlertExecutionResult]**](AlertExecutionResult.md) | List of execution results | 
**pagination** | [**PaginationResponse**](PaginationResponse.md) | Pagination information | 
**total_count** | **int** | Total number of executions | 

## Example

```python
from mixpeek.models.alert_execution_list_response import AlertExecutionListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AlertExecutionListResponse from a JSON string
alert_execution_list_response_instance = AlertExecutionListResponse.from_json(json)
# print the JSON string representation of the object
print(AlertExecutionListResponse.to_json())

# convert the object into a dict
alert_execution_list_response_dict = alert_execution_list_response_instance.to_dict()
# create an instance of AlertExecutionListResponse from a dict
alert_execution_list_response_from_dict = AlertExecutionListResponse.from_dict(alert_execution_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


