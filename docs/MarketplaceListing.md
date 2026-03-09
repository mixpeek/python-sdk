# MarketplaceListing

A marketplace listing for a retriever.  This is the unified model for all public and marketplace retrievers. Replaces the PublishedRetriever system with a simpler, more flexible approach.  Free tier = public retriever (anyone can subscribe for free) Paid tiers = monetized marketplace offering

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**listing_id** | **str** | Unique identifier for the listing | [optional] 
**internal_id** | **str** | Organization that owns this listing (provider) | 
**namespace_id** | **str** | Namespace containing the retriever | 
**retriever_id** | **str** | Retriever being offered in the marketplace | 
**title** | **str** | Public display title | 
**description** | **str** | Public description of what this listing provides | 
**public_name** | **str** | Public URL-safe slug for the listing (e.g., &#39;video-search&#39;). Used in public URL: mxp.co/m/{public_name}. Must be globally unique. | 
**category** | **str** | Category for browsing (e.g., &#39;Content Moderation&#39;, &#39;Search&#39;) | [optional] 
**tags** | **List[str]** | Tags for discovery | [optional] 
**logo_url** | **str** | URL to listing logo/icon | [optional] 
**icon_base64** | **str** | Base64 encoded icon/favicon (data URI format). Max size: ~200KB encoded. Use for small icons. | [optional] 
**available_tiers** | [**List[SubscriptionTierConfig]**](SubscriptionTierConfig.md) | Available subscription tiers (must include at least one tier, typically FREE for public listings) | 
**display_config** | **Dict[str, object]** | JSON-based UI configuration for the public interface. Follows a component-based schema (inspired by json-render): { &#39;components&#39;: [...], &#39;theme&#39;: {...}, &#39;layout&#39;: {...} }. If not provided, a default UI is generated from retriever input_schema. | [optional] 
**password_secret_name** | **str** | Optional organization secret name containing password for access protection. If set, users must provide password to subscribe (even for free tier). | [optional] 
**status** | [**ListingStatus**](ListingStatus.md) | Publication status | [optional] 
**visibility** | [**ListingVisibility**](ListingVisibility.md) | Visibility level. &#39;listed&#39; &#x3D; shown in marketplace catalog &amp; homepage showcase. &#39;unlisted&#39; &#x3D; accessible via direct link only (not in catalog). | [optional] 
**is_active** | **bool** | DEPRECATED: Use &#39;status&#39; field instead. Computed from status (True if PUBLISHED, False otherwise). | [optional] [default to True]
**created_at** | **datetime** | When the listing was created | [optional] 
**updated_at** | **datetime** | When the listing was last updated | [optional] 
**published_at** | **datetime** | When the listing was first published | [optional] 
**total_subscribers** | **int** | Total number of active subscribers | [optional] [default to 0]
**total_queries** | **int** | Total queries executed across all subscribers | [optional] [default to 0]

## Example

```python
from mixpeek.models.marketplace_listing import MarketplaceListing

# TODO update the JSON string below
json = "{}"
# create an instance of MarketplaceListing from a JSON string
marketplace_listing_instance = MarketplaceListing.from_json(json)
# print the JSON string representation of the object
print(MarketplaceListing.to_json())

# convert the object into a dict
marketplace_listing_dict = marketplace_listing_instance.to_dict()
# create an instance of MarketplaceListing from a dict
marketplace_listing_from_dict = MarketplaceListing.from_dict(marketplace_listing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


