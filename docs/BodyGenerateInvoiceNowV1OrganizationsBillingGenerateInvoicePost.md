# BodyGenerateInvoiceNowV1OrganizationsBillingGenerateInvoicePost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_month** | **str** | Billing month (YYYY-MM). Defaults to previous month. | [optional] 
**dry_run** | **bool** | If true, show what would be invoiced without creating Stripe invoice. | [optional] [default to False]

## Example

```python
from mixpeek.models.body_generate_invoice_now_v1_organizations_billing_generate_invoice_post import BodyGenerateInvoiceNowV1OrganizationsBillingGenerateInvoicePost

# TODO update the JSON string below
json = "{}"
# create an instance of BodyGenerateInvoiceNowV1OrganizationsBillingGenerateInvoicePost from a JSON string
body_generate_invoice_now_v1_organizations_billing_generate_invoice_post_instance = BodyGenerateInvoiceNowV1OrganizationsBillingGenerateInvoicePost.from_json(json)
# print the JSON string representation of the object
print(BodyGenerateInvoiceNowV1OrganizationsBillingGenerateInvoicePost.to_json())

# convert the object into a dict
body_generate_invoice_now_v1_organizations_billing_generate_invoice_post_dict = body_generate_invoice_now_v1_organizations_billing_generate_invoice_post_instance.to_dict()
# create an instance of BodyGenerateInvoiceNowV1OrganizationsBillingGenerateInvoicePost from a dict
body_generate_invoice_now_v1_organizations_billing_generate_invoice_post_from_dict = BodyGenerateInvoiceNowV1OrganizationsBillingGenerateInvoicePost.from_dict(body_generate_invoice_now_v1_organizations_billing_generate_invoice_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


