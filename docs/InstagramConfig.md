# InstagramConfig

Instagram Business/Creator account configuration via Meta Graph API.  Enables Mixpeek to sync media (posts, reels, carousels) from Instagram accounts using the official Instagram Graph API. Each media item becomes a bucket object with metadata (caption, likes, comments, permalink).  Authentication:     - OAuth 2.0 via Meta Developer Console     - Long-lived tokens (60 days) with automatic refresh  Requirements:     - Instagram Business or Creator account     - Facebook Page linked to the Instagram account     - Meta app with instagram_basic permission  Use Cases:     - Sync creator content for talent analysis     - Monitor competitor ad creatives     - Build social media content libraries for multimodal search

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_type** | **str** |  | [optional] [default to 'instagram']
**credentials** | [**InstagramOAuthCredentials**](InstagramOAuthCredentials.md) | OAuth credentials for Instagram Graph API access. | 
**scopes** | **List[str]** | OAuth scopes granted during authorization. | [optional] [default to [instagram_basic, instagram_manage_insights, pages_show_list]]
**business_account_id** | **str** | Instagram Business Account ID if different from the user ID. Auto-populated from OAuth flow. | [optional] 

## Example

```python
from mixpeek.models.instagram_config import InstagramConfig

# TODO update the JSON string below
json = "{}"
# create an instance of InstagramConfig from a JSON string
instagram_config_instance = InstagramConfig.from_json(json)
# print the JSON string representation of the object
print(InstagramConfig.to_json())

# convert the object into a dict
instagram_config_dict = instagram_config_instance.to_dict()
# create an instance of InstagramConfig from a dict
instagram_config_from_dict = InstagramConfig.from_dict(instagram_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


