# BoxConfig

Box cloud content management and file sharing configuration.  Enables Mixpeek to connect to Box for automated file ingestion and synchronization. Supports enterprise-grade content management features including folder sync, metadata, versioning, and retention policies.  Authentication Methods:     1. OAuth 2.0 (for user-level access):         - Standard OAuth flow with access/refresh tokens         - Access scoped to the authorizing user's content      2. Client Credentials Grant (CCG) (RECOMMENDED for production):         - Server-to-server without user interaction         - Acts as service account or specific user         - Requires admin authorization in Box Admin Console      3. JWT (for high-security enterprise):         - RSA key pair for signing JWT assertions         - No user interaction required         - Highest security option  Requirements:     - Box Developer account with an application     - Application authorized in Box Admin Console (for CCG/JWT)     - Network connectivity to api.box.com  Use Cases:     - Sync enterprise document libraries     - Ingest compliance and legal documents     - Monitor collaboration folders for new content     - Archive and search enterprise content

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_type** | **str** |  | [optional] [default to 'box']
**credentials** | [**Credentials**](Credentials.md) |  | 
**folder_id** | **str** | Box folder ID to sync from. Default &#39;0&#39; is the root folder. Find folder ID: Open folder in Box web UI, copy the numeric ID from the URL. Example URL: https://app.box.com/folder/123456789 → folder_id&#x3D;&#39;123456789&#39; | [optional] [default to '0']

## Example

```python
from mixpeek.models.box_config import BoxConfig

# TODO update the JSON string below
json = "{}"
# create an instance of BoxConfig from a JSON string
box_config_instance = BoxConfig.from_json(json)
# print the JSON string representation of the object
print(BoxConfig.to_json())

# convert the object into a dict
box_config_dict = box_config_instance.to_dict()
# create an instance of BoxConfig from a dict
box_config_from_dict = BoxConfig.from_dict(box_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


