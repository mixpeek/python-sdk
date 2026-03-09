# InstagramOAuthCredentials

Credentials for Instagram Graph API OAuth2 authentication.  Instagram uses Meta's OAuth2 flow to obtain access tokens. The flow produces a short-lived token which is exchanged for a long-lived token (valid for 60 days). Long-lived tokens can be refreshed before expiry.  Prerequisites:     - Meta Developer account with an Instagram app     - Instagram Business or Creator account linked to a Facebook Page     - App must have instagram_basic permission approved  Security:     - client_secret and access_token encrypted at rest via CSFLE     - Long-lived tokens must be refreshed before 60-day expiry     - Token refresh happens automatically during sync execution

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'oauth']
**client_id** | **str** | Instagram App ID from Meta Developer Console. | 
**client_secret** | **str** | SECURITY: Encrypted at rest via CSFLE. Instagram App Secret from Meta Developer Console. | 
**access_token** | **str** | SECURITY: Encrypted at rest. Long-lived Instagram access token (60-day validity). | 
**token_expires_at** | **datetime** | Token expiration timestamp. Used to trigger proactive refresh. | [optional] 
**instagram_user_id** | **str** | Instagram User ID of the account that authorized access. | 
**instagram_username** | **str** | Instagram username for display purposes. | [optional] 

## Example

```python
from mixpeek.models.instagram_o_auth_credentials import InstagramOAuthCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of InstagramOAuthCredentials from a JSON string
instagram_o_auth_credentials_instance = InstagramOAuthCredentials.from_json(json)
# print the JSON string representation of the object
print(InstagramOAuthCredentials.to_json())

# convert the object into a dict
instagram_o_auth_credentials_dict = instagram_o_auth_credentials_instance.to_dict()
# create an instance of InstagramOAuthCredentials from a dict
instagram_o_auth_credentials_from_dict = InstagramOAuthCredentials.from_dict(instagram_o_auth_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


