# SetupPaymentMethodResponse

Response after creating a SetupIntent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**setup_intent_id** | **str** | Stripe SetupIntent ID | 
**client_secret** | **str** | Client secret for Stripe Elements | 
**customer_id** | **str** | Stripe Customer ID | 

## Example

```python
from mixpeek.models.setup_payment_method_response import SetupPaymentMethodResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SetupPaymentMethodResponse from a JSON string
setup_payment_method_response_instance = SetupPaymentMethodResponse.from_json(json)
# print the JSON string representation of the object
print(SetupPaymentMethodResponse.to_json())

# convert the object into a dict
setup_payment_method_response_dict = setup_payment_method_response_instance.to_dict()
# create an instance of SetupPaymentMethodResponse from a dict
setup_payment_method_response_from_dict = SetupPaymentMethodResponse.from_dict(setup_payment_method_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


