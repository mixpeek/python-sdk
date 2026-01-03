# InvoiceListResponse

Response with list of invoices.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoices** | [**List[InvoiceInfo]**](InvoiceInfo.md) | List of invoices | [optional] 
**total** | **int** | Total number of invoices | 
**has_more** | **bool** | Whether there are more invoices | 

## Example

```python
from mixpeek.models.invoice_list_response import InvoiceListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceListResponse from a JSON string
invoice_list_response_instance = InvoiceListResponse.from_json(json)
# print the JSON string representation of the object
print(InvoiceListResponse.to_json())

# convert the object into a dict
invoice_list_response_dict = invoice_list_response_instance.to_dict()
# create an instance of InvoiceListResponse from a dict
invoice_list_response_from_dict = InvoiceListResponse.from_dict(invoice_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


