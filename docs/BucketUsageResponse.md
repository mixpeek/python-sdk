# BucketUsageResponse

Bucket usage and cost analytics response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_id** | **str** | Bucket identifier | 
**time_range** | [**ApiAnalyticsBucketsModelsTimeRange**](ApiAnalyticsBucketsModelsTimeRange.md) | Query time range | 
**metrics** | [**List[UsageMetric]**](UsageMetric.md) | Usage metrics | 
**cost_breakdown** | [**CostBreakdown**](CostBreakdown.md) | Cost breakdown | 
**total_credits** | **int** | Total credits consumed | 
**total_cost_usd** | **float** | Total cost in USD | 

## Example

```python
from mixpeek.models.bucket_usage_response import BucketUsageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BucketUsageResponse from a JSON string
bucket_usage_response_instance = BucketUsageResponse.from_json(json)
# print the JSON string representation of the object
print(BucketUsageResponse.to_json())

# convert the object into a dict
bucket_usage_response_dict = bucket_usage_response_instance.to_dict()
# create an instance of BucketUsageResponse from a dict
bucket_usage_response_from_dict = BucketUsageResponse.from_dict(bucket_usage_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


