# ListAdhocExecutionsRequest

Request to list ad-hoc retriever executions with filtering.  Allows filtering by status, time range, and searching by query summary. Results are ordered by timestamp descending (most recent first).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Filter by execution status. Common values: &#39;completed&#39;, &#39;failed&#39;. OPTIONAL - omit to see all statuses. | [optional] 
**start_time** | **object** |  | [optional] 
**end_time** | **object** |  | [optional] 

## Example

```python
from mixpeek.models.list_adhoc_executions_request import ListAdhocExecutionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListAdhocExecutionsRequest from a JSON string
list_adhoc_executions_request_instance = ListAdhocExecutionsRequest.from_json(json)
# print the JSON string representation of the object
print(ListAdhocExecutionsRequest.to_json())

# convert the object into a dict
list_adhoc_executions_request_dict = list_adhoc_executions_request_instance.to_dict()
# create an instance of ListAdhocExecutionsRequest from a dict
list_adhoc_executions_request_from_dict = ListAdhocExecutionsRequest.from_dict(list_adhoc_executions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


