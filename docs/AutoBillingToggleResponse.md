# AutoBillingToggleResponse

Response after toggling auto-billing.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Whether the operation was successful | [optional] [default to True]
**auto_billing_enabled** | **bool** | New auto-billing status | 
**message** | **str** | Human-readable message | 
**billing_period_start** | **datetime** | Billing period start (if enabled) | [optional] 

## Example

```python
from mixpeek.models.auto_billing_toggle_response import AutoBillingToggleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AutoBillingToggleResponse from a JSON string
auto_billing_toggle_response_instance = AutoBillingToggleResponse.from_json(json)
# print the JSON string representation of the object
print(AutoBillingToggleResponse.to_json())

# convert the object into a dict
auto_billing_toggle_response_dict = auto_billing_toggle_response_instance.to_dict()
# create an instance of AutoBillingToggleResponse from a dict
auto_billing_toggle_response_from_dict = AutoBillingToggleResponse.from_dict(auto_billing_toggle_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


