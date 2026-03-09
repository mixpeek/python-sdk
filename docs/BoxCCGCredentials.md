# BoxCCGCredentials

Credentials for Box Client Credentials Grant (CCG) authentication.  CCG provides server-to-server authentication without user interaction. Recommended for enterprise and automated sync operations.  Prerequisites:     - Create a Box application with Server Authentication (Client Credentials Grant)     - Authorize the application in the Box Admin Console     - Optionally configure an enterprise or user ID to act as  Security:     - client_secret encrypted at rest via CSFLE     - No user tokens involved; app authenticates as itself or as a user/enterprise

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'ccg']
**client_id** | **str** | REQUIRED. Box application client ID from Developer Console. | 
**client_secret** | **str** | REQUIRED. Box application client secret. SECURITY: Encrypted at rest via CSFLE. | 
**enterprise_id** | **str** | Enterprise ID to authenticate as. Required when using CCG to act as the enterprise (service account). Find in: Box Admin Console &gt; Enterprise Settings. | [optional] 
**user_id** | **str** | User ID to authenticate as. Used when the app needs to act as a specific managed user. Mutually exclusive with enterprise_id for token acquisition. | [optional] 

## Example

```python
from mixpeek.models.box_ccg_credentials import BoxCCGCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of BoxCCGCredentials from a JSON string
box_ccg_credentials_instance = BoxCCGCredentials.from_json(json)
# print the JSON string representation of the object
print(BoxCCGCredentials.to_json())

# convert the object into a dict
box_ccg_credentials_dict = box_ccg_credentials_instance.to_dict()
# create an instance of BoxCCGCredentials from a dict
box_ccg_credentials_from_dict = BoxCCGCredentials.from_dict(box_ccg_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


