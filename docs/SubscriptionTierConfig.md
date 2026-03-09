# SubscriptionTierConfig

Configuration for a subscription tier.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tier** | [**SubscriptionTier**](SubscriptionTier.md) | Tier level | 
**price_per_month** | **float** | Monthly price in USD (0.0 for free tier) | [optional] [default to 0]
**limits** | [**TierLimits**](TierLimits.md) | Rate limits and quotas for this tier | [optional] 
**features** | **List[str]** | List of features included in this tier | [optional] 
**stripe_price_id** | **str** | Stripe price ID for paid tiers | [optional] 

## Example

```python
from mixpeek.models.subscription_tier_config import SubscriptionTierConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionTierConfig from a JSON string
subscription_tier_config_instance = SubscriptionTierConfig.from_json(json)
# print the JSON string representation of the object
print(SubscriptionTierConfig.to_json())

# convert the object into a dict
subscription_tier_config_dict = subscription_tier_config_instance.to_dict()
# create an instance of SubscriptionTierConfig from a dict
subscription_tier_config_from_dict = SubscriptionTierConfig.from_dict(subscription_tier_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


