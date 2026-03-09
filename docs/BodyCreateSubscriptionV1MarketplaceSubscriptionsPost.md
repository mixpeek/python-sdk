# BodyCreateSubscriptionV1MarketplaceSubscriptionsPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**listing_id** | **str** | Marketplace listing ID | 
**tier** | [**SubscriptionTier**](SubscriptionTier.md) | Subscription tier (free, basic, pro, enterprise) | 

## Example

```python
from mixpeek.models.body_create_subscription_v1_marketplace_subscriptions_post import BodyCreateSubscriptionV1MarketplaceSubscriptionsPost

# TODO update the JSON string below
json = "{}"
# create an instance of BodyCreateSubscriptionV1MarketplaceSubscriptionsPost from a JSON string
body_create_subscription_v1_marketplace_subscriptions_post_instance = BodyCreateSubscriptionV1MarketplaceSubscriptionsPost.from_json(json)
# print the JSON string representation of the object
print(BodyCreateSubscriptionV1MarketplaceSubscriptionsPost.to_json())

# convert the object into a dict
body_create_subscription_v1_marketplace_subscriptions_post_dict = body_create_subscription_v1_marketplace_subscriptions_post_instance.to_dict()
# create an instance of BodyCreateSubscriptionV1MarketplaceSubscriptionsPost from a dict
body_create_subscription_v1_marketplace_subscriptions_post_from_dict = BodyCreateSubscriptionV1MarketplaceSubscriptionsPost.from_dict(body_create_subscription_v1_marketplace_subscriptions_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


