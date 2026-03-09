# TierLimits

Rate limits and quotas for a subscription tier.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests_per_minute** | **int** | Maximum requests per minute (None &#x3D; unlimited) | [optional] 
**requests_per_hour** | **int** | Maximum requests per hour (None &#x3D; unlimited) | [optional] 
**requests_per_day** | **int** | Maximum requests per day (None &#x3D; unlimited) | [optional] 
**requests_per_month** | **int** | Maximum requests per month (None &#x3D; unlimited) | [optional] 

## Example

```python
from mixpeek.models.tier_limits import TierLimits

# TODO update the JSON string below
json = "{}"
# create an instance of TierLimits from a JSON string
tier_limits_instance = TierLimits.from_json(json)
# print the JSON string representation of the object
print(TierLimits.to_json())

# convert the object into a dict
tier_limits_dict = tier_limits_instance.to_dict()
# create an instance of TierLimits from a dict
tier_limits_from_dict = TierLimits.from_dict(tier_limits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


