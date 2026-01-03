# UpdateSpendingCapsRequest

Request to update spending cap configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monthly_spending_budget** | **int** | Soft spending limit in USD cents. Triggers alerts but doesn&#39;t block API access. Set to null to remove budget limit. | [optional] 
**spending_alert_thresholds** | **List[int]** | Percentage thresholds for spending alerts (0-100). When current spending reaches each threshold, an alert is sent. | [optional] 
**spending_alerts_enabled** | **bool** | Whether to send spending alerts when thresholds are crossed. | [optional] 
**hard_spending_cap** | **int** | Hard spending limit in USD cents. When reached, API access is blocked. Set to null to remove hard cap. | [optional] 
**hard_cap_enabled** | **bool** | Whether to enforce the hard spending cap. | [optional] 

## Example

```python
from mixpeek.models.update_spending_caps_request import UpdateSpendingCapsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSpendingCapsRequest from a JSON string
update_spending_caps_request_instance = UpdateSpendingCapsRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateSpendingCapsRequest.to_json())

# convert the object into a dict
update_spending_caps_request_dict = update_spending_caps_request_instance.to_dict()
# create an instance of UpdateSpendingCapsRequest from a dict
update_spending_caps_request_from_dict = UpdateSpendingCapsRequest.from_dict(update_spending_caps_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


