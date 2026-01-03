# GetPaymentMethodResponse

Response with current payment method.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_payment_method** | **bool** | Whether organization has a payment method saved | 
**payment_method** | [**PaymentMethodInfo**](PaymentMethodInfo.md) | Payment method details (null if none saved) | [optional] 
**auto_billing_enabled** | **bool** | Whether automatic billing is enabled | 

## Example

```python
from mixpeek.models.get_payment_method_response import GetPaymentMethodResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetPaymentMethodResponse from a JSON string
get_payment_method_response_instance = GetPaymentMethodResponse.from_json(json)
# print the JSON string representation of the object
print(GetPaymentMethodResponse.to_json())

# convert the object into a dict
get_payment_method_response_dict = get_payment_method_response_instance.to_dict()
# create an instance of GetPaymentMethodResponse from a dict
get_payment_method_response_from_dict = GetPaymentMethodResponse.from_dict(get_payment_method_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


