# TikTokConfig

TikTok account configuration via TikTok Content API.  Enables Mixpeek to sync videos from TikTok accounts using the official TikTok API. Each video becomes a bucket object with metadata (description, likes, views, shares, comments).  Authentication:     - OAuth 2.0 via TikTok Login Kit     - Access tokens expire in 24h (refresh_token flow)  Requirements:     - TikTok Developer account with approved app     - user.info.basic and video.list scopes  Use Cases:     - Sync creator video content for talent analysis     - Monitor trending content and competitors     - Build video content libraries for multimodal search

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_type** | **str** |  | [optional] [default to 'tiktok']
**credentials** | [**TikTokOAuthCredentials**](TikTokOAuthCredentials.md) | OAuth credentials for TikTok Content API access. | 
**scopes** | **List[str]** | OAuth scopes granted during authorization. | [optional] [default to [user.info.basic, video.list]]

## Example

```python
from mixpeek.models.tik_tok_config import TikTokConfig

# TODO update the JSON string below
json = "{}"
# create an instance of TikTokConfig from a JSON string
tik_tok_config_instance = TikTokConfig.from_json(json)
# print the JSON string representation of the object
print(TikTokConfig.to_json())

# convert the object into a dict
tik_tok_config_dict = tik_tok_config_instance.to_dict()
# create an instance of TikTokConfig from a dict
tik_tok_config_from_dict = TikTokConfig.from_dict(tik_tok_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


