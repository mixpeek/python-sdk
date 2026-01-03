# CurrentUsageResponse

Response with current month usage.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_month_usage** | **int** | Credits consumed in current billing cycle | 
**billing_month** | **str** | Current billing month (YYYY-MM) | 
**billing_period_start** | **datetime** | Start of current billing period | 
**billing_period_end** | **datetime** | End of current billing period | 
**estimated_cost_usd** | **float** | Estimated cost for current usage | 
**credit_rate** | **float** | Cost per credit in USD | [optional] [default to 0.001]
**auto_billing_enabled** | **bool** | Whether auto-billing is enabled | 
**next_invoice_date** | **datetime** | When next invoice will be generated | 

## Example

```python
from mixpeek.models.current_usage_response import CurrentUsageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CurrentUsageResponse from a JSON string
current_usage_response_instance = CurrentUsageResponse.from_json(json)
# print the JSON string representation of the object
print(CurrentUsageResponse.to_json())

# convert the object into a dict
current_usage_response_dict = current_usage_response_instance.to_dict()
# create an instance of CurrentUsageResponse from a dict
current_usage_response_from_dict = CurrentUsageResponse.from_dict(current_usage_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


