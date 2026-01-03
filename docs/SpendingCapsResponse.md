# SpendingCapsResponse

Response with spending cap configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monthly_spending_budget** | **int** | Soft spending limit in USD cents (null &#x3D; unlimited) | [optional] 
**monthly_spending_budget_usd** | **float** | Soft spending limit in USD | [optional] 
**spending_alert_thresholds** | **List[int]** | Percentage thresholds for spending alerts | [optional] 
**spending_alerts_enabled** | **bool** | Whether spending alerts are enabled | [optional] [default to True]
**spending_alerts_sent** | **List[int]** | Alert thresholds triggered in current billing cycle | [optional] 
**hard_spending_cap** | **int** | Hard spending limit in USD cents (null &#x3D; no hard cap) | [optional] 
**hard_spending_cap_usd** | **float** | Hard spending limit in USD | [optional] 
**hard_cap_enabled** | **bool** | Whether hard spending cap is enforced | [optional] [default to False]
**current_spending_cents** | **int** | Current spending in current billing cycle (cents) | 
**current_spending_usd** | **float** | Current spending in current billing cycle (USD) | 
**budget_percentage_used** | **float** | Percentage of budget used (null if no budget set) | [optional] 

## Example

```python
from mixpeek.models.spending_caps_response import SpendingCapsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SpendingCapsResponse from a JSON string
spending_caps_response_instance = SpendingCapsResponse.from_json(json)
# print the JSON string representation of the object
print(SpendingCapsResponse.to_json())

# convert the object into a dict
spending_caps_response_dict = spending_caps_response_instance.to_dict()
# create an instance of SpendingCapsResponse from a dict
spending_caps_response_from_dict = SpendingCapsResponse.from_dict(spending_caps_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


