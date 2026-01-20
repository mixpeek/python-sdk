# ListExecutionsRequest

Request to list retriever executions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | **object** |  | [optional] 
**sorts** | **List[object]** |  | [optional] 
**status** | **str** | Optional status filter (completed, failed, running). | [optional] 

## Example

```python
from mixpeek.models.list_executions_request import ListExecutionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListExecutionsRequest from a JSON string
list_executions_request_instance = ListExecutionsRequest.from_json(json)
# print the JSON string representation of the object
print(ListExecutionsRequest.to_json())

# convert the object into a dict
list_executions_request_dict = list_executions_request_instance.to_dict()
# create an instance of ListExecutionsRequest from a dict
list_executions_request_from_dict = ListExecutionsRequest.from_dict(list_executions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


