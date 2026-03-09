# TikTokOAuthCredentials

Credentials for TikTok Content API OAuth2 authentication.  TikTok uses OAuth2 via TikTok Login Kit. Access tokens are short-lived (24 hours) and must be refreshed using the refresh token.  Prerequisites:     - TikTok Developer account with an approved app     - App must have user.info.basic and video.list scopes  Security:     - client_secret, access_token, and refresh_token encrypted at rest via CSFLE     - Access tokens expire in 24h; refresh tokens used for renewal     - Token refresh happens automatically during sync execution

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'oauth']
**client_key** | **str** | TikTok App Client Key from Developer Portal. | 
**client_secret** | **str** | SECURITY: Encrypted at rest via CSFLE. TikTok App Client Secret from Developer Portal. | 
**access_token** | **str** | SECURITY: Encrypted at rest. TikTok access token (24h validity). | 
**refresh_token** | **str** | SECURITY: Encrypted at rest. Used to obtain new access tokens. | 
**token_expires_at** | **datetime** | Access token expiration timestamp. | [optional] 
**open_id** | **str** | TikTok user&#39;s open_id from the authorization response. | 

## Example

```python
from mixpeek.models.tik_tok_o_auth_credentials import TikTokOAuthCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of TikTokOAuthCredentials from a JSON string
tik_tok_o_auth_credentials_instance = TikTokOAuthCredentials.from_json(json)
# print the JSON string representation of the object
print(TikTokOAuthCredentials.to_json())

# convert the object into a dict
tik_tok_o_auth_credentials_dict = tik_tok_o_auth_credentials_instance.to_dict()
# create an instance of TikTokOAuthCredentials from a dict
tik_tok_o_auth_credentials_from_dict = TikTokOAuthCredentials.from_dict(tik_tok_o_auth_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


