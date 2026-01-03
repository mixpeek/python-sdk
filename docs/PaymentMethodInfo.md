# PaymentMethodInfo

Payment method details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_method_id** | **str** | Stripe PaymentMethod ID | 
**type** | **str** | Payment method type | 
**card_last4** | **str** | Last 4 digits of card | 
**card_brand** | **str** | Card brand | 

## Example

```python
from mixpeek.models.payment_method_info import PaymentMethodInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodInfo from a JSON string
payment_method_info_instance = PaymentMethodInfo.from_json(json)
# print the JSON string representation of the object
print(PaymentMethodInfo.to_json())

# convert the object into a dict
payment_method_info_dict = payment_method_info_instance.to_dict()
# create an instance of PaymentMethodInfo from a dict
payment_method_info_from_dict = PaymentMethodInfo.from_dict(payment_method_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


