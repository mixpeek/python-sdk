# ConfirmPaymentMethodRequest

Request to confirm a payment method after collection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_method_id** | **str** | Stripe PaymentMethod ID from frontend | 

## Example

```python
from mixpeek.models.confirm_payment_method_request import ConfirmPaymentMethodRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConfirmPaymentMethodRequest from a JSON string
confirm_payment_method_request_instance = ConfirmPaymentMethodRequest.from_json(json)
# print the JSON string representation of the object
print(ConfirmPaymentMethodRequest.to_json())

# convert the object into a dict
confirm_payment_method_request_dict = confirm_payment_method_request_instance.to_dict()
# create an instance of ConfirmPaymentMethodRequest from a dict
confirm_payment_method_request_from_dict = ConfirmPaymentMethodRequest.from_dict(confirm_payment_method_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


