# ConfirmPaymentMethodResponse

Response after confirming payment method.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Whether payment method was successfully confirmed | [optional] [default to True]
**payment_method** | [**PaymentMethodInfo**](PaymentMethodInfo.md) | Confirmed payment method details | 
**auto_billing_enabled** | **bool** | Whether auto-billing is now enabled | 
**billing_period_start** | **datetime** | When the current billing period started | 

## Example

```python
from mixpeek.models.confirm_payment_method_response import ConfirmPaymentMethodResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConfirmPaymentMethodResponse from a JSON string
confirm_payment_method_response_instance = ConfirmPaymentMethodResponse.from_json(json)
# print the JSON string representation of the object
print(ConfirmPaymentMethodResponse.to_json())

# convert the object into a dict
confirm_payment_method_response_dict = confirm_payment_method_response_instance.to_dict()
# create an instance of ConfirmPaymentMethodResponse from a dict
confirm_payment_method_response_from_dict = ConfirmPaymentMethodResponse.from_dict(confirm_payment_method_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


