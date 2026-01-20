# ListAlertsResponse

Response model for listing alerts.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[AlertResponse]**](AlertResponse.md) | List of alerts | 
**pagination** | [**PaginationResponse**](PaginationResponse.md) | Pagination information | 
**total_count** | **int** | Total number of alerts matching query | 
**stats** | [**AlertListStats**](AlertListStats.md) | Aggregate statistics across all alerts in the result | [optional] 

## Example

```python
from mixpeek.models.list_alerts_response import ListAlertsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListAlertsResponse from a JSON string
list_alerts_response_instance = ListAlertsResponse.from_json(json)
# print the JSON string representation of the object
print(ListAlertsResponse.to_json())

# convert the object into a dict
list_alerts_response_dict = list_alerts_response_instance.to_dict()
# create an instance of ListAlertsResponse from a dict
list_alerts_response_from_dict = ListAlertsResponse.from_dict(list_alerts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


