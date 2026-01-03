# InvoiceInfo

Information about a monthly invoice.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_id** | **str** | Stripe Invoice ID | 
**invoice_url** | **str** | Stripe-hosted invoice URL | 
**invoice_pdf** | **str** | PDF download URL | 
**amount_due** | **int** | Amount due in cents | 
**amount_paid** | **int** | Amount paid in cents | 
**status** | **str** | Invoice status | 
**billing_month** | **str** | Billing month (YYYY-MM) | 
**total_credits** | **int** | Total credits billed | 
**created** | **datetime** | When invoice was created | 
**paid_at** | **datetime** | When invoice was paid | [optional] 

## Example

```python
from mixpeek.models.invoice_info import InvoiceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceInfo from a JSON string
invoice_info_instance = InvoiceInfo.from_json(json)
# print the JSON string representation of the object
print(InvoiceInfo.to_json())

# convert the object into a dict
invoice_info_dict = invoice_info_instance.to_dict()
# create an instance of InvoiceInfo from a dict
invoice_info_from_dict = InvoiceInfo.from_dict(invoice_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


