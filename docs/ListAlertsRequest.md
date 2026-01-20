# ListAlertsRequest

Request model to list alerts.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search** | **str** | Search term for wildcard search across alert_id, name, description | [optional] 
**filters** | [**LogicalOperatorInput**](LogicalOperatorInput.md) | Filters to apply to the alert list | [optional] 
**sort** | [**SortOption**](SortOption.md) | Sort configuration for the alert list | [optional] 
**case_sensitive** | **bool** | If True, filters and search will be case-sensitive | [optional] [default to False]

## Example

```python
from mixpeek.models.list_alerts_request import ListAlertsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListAlertsRequest from a JSON string
list_alerts_request_instance = ListAlertsRequest.from_json(json)
# print the JSON string representation of the object
print(ListAlertsRequest.to_json())

# convert the object into a dict
list_alerts_request_dict = list_alerts_request_instance.to_dict()
# create an instance of ListAlertsRequest from a dict
list_alerts_request_from_dict = ListAlertsRequest.from_dict(list_alerts_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


