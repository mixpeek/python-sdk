# Credentials1

REQUIRED. AWS authentication credentials configuration. Choose 'iam_role' for production deployments (recommended) or 'access_key' for development, testing, or S3-compatible services. The 'type' field determines which credential mechanism is used.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'access_key']
**access_key_id** | **str** | REQUIRED. AWS access key ID for authentication. Format: 20-character alphanumeric string starting with &#39;AKIA&#39; (long-term) or &#39;ASIA&#39; (temporary). Obtain from: AWS Console &gt; IAM &gt; Users &gt; Security Credentials | 
**secret_access_key** | **str** | REQUIRED. AWS secret access key for authentication. SECURITY: This field is encrypted at rest. Never log or expose this value. Format: 40-character base64-encoded string. Obtain from: AWS Console when creating/viewing access key (shown only once) | 
**session_token** | **str** | NOT REQUIRED. Temporary session token for AWS STS credentials. REQUIRED when using temporary security credentials from AWS STS. NOT REQUIRED for long-term IAM user access keys. SECURITY: Encrypted at rest. Automatically expires after session duration. Format: Base64-encoded string, typically several hundred characters. Use case: Enhanced security with automatic credential rotation | [optional] 
**role_arn** | **str** | REQUIRED. Amazon Resource Name (ARN) of the IAM role to assume. This role must exist in the customer&#39;s AWS account and have a trust relationship configured to allow Mixpeek to assume it. Format: arn:aws:iam::{account-id}:role/{role-name} Example trust policy should allow principal: arn:aws:iam::{mixpeek-account}:root Recommended role name: mixpeek-storage-sync-role | 
**external_id** | **str** | REQUIRED. External ID for secure role assumption (prevents confused deputy attacks). This value should be unique to your organization and kept confidential. Mixpeek provides this value during connection setup. Must match the ExternalId condition in the role&#39;s trust policy. Format: Recommended pattern is mixpeek-{organization_id} Security: Include this in the trust policy Condition statement | 

## Example

```python
from mixpeek.models.credentials1 import Credentials1

# TODO update the JSON string below
json = "{}"
# create an instance of Credentials1 from a JSON string
credentials1_instance = Credentials1.from_json(json)
# print the JSON string representation of the object
print(Credentials1.to_json())

# convert the object into a dict
credentials1_dict = credentials1_instance.to_dict()
# create an instance of Credentials1 from a dict
credentials1_from_dict = Credentials1.from_dict(credentials1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


