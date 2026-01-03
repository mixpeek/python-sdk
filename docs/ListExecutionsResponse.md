# ListExecutionsResponse

Re-export shared execution listing response for OpenAPI docs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[RetrieverExecutionSummary]**](RetrieverExecutionSummary.md) | Execution summaries | [optional] 
**pagination** | [**PaginationMetadata**](PaginationMetadata.md) | Pagination metadata | 

## Example

```python
from mixpeek.models.list_executions_response import ListExecutionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListExecutionsResponse from a JSON string
list_executions_response_instance = ListExecutionsResponse.from_json(json)
# print the JSON string representation of the object
print(ListExecutionsResponse.to_json())

# convert the object into a dict
list_executions_response_dict = list_executions_response_instance.to_dict()
# create an instance of ListExecutionsResponse from a dict
list_executions_response_from_dict = ListExecutionsResponse.from_dict(list_executions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


