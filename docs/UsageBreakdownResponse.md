# UsageBreakdownResponse

Response with detailed usage breakdown.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_month** | **str** | Billing month (YYYY-MM) | 
**total_credits** | **int** | Total credits consumed | 
**total_cost_usd** | **float** | Total cost in USD | 
**by_operation** | **Dict[str, int]** | Credits consumed by operation type | 
**by_extractor** | **Dict[str, int]** | Credits consumed by extractor | 
**period_start** | **datetime** | Start of billing period | 
**period_end** | **datetime** | End of billing period | 

## Example

```python
from mixpeek.models.usage_breakdown_response import UsageBreakdownResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UsageBreakdownResponse from a JSON string
usage_breakdown_response_instance = UsageBreakdownResponse.from_json(json)
# print the JSON string representation of the object
print(UsageBreakdownResponse.to_json())

# convert the object into a dict
usage_breakdown_response_dict = usage_breakdown_response_instance.to_dict()
# create an instance of UsageBreakdownResponse from a dict
usage_breakdown_response_from_dict = UsageBreakdownResponse.from_dict(usage_breakdown_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


