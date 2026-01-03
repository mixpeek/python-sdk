# S3AccessKeyCredentials

AWS S3 access key and secret credentials.  Access keys provide programmatic access to S3 buckets using long-lived credentials. This authentication method is straightforward but less secure than IAM role assumption.  Prerequisites:     - IAM user or role with S3 access permissions     - Access key and secret key generated in AWS Console     - Appropriate bucket policies or IAM policies configured  Security Considerations:     - Access keys are long-lived and don't automatically expire     - secret_access_key is encrypted at rest but should be rotated regularly     - Consider using IAM role assumption (S3RoleCredentials) for production     - Never commit access keys to version control  Use Cases:     - Quick prototyping and development     - Testing S3 integrations     - Temporary credentials with session_token for enhanced security     - Accessing S3-compatible services (MinIO, DigitalOcean Spaces)  Recommended Alternative:     For production deployments, use S3RoleCredentials with IAM role assumption     instead of access keys for better security and credential management.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'access_key']
**access_key_id** | **str** | REQUIRED. AWS access key ID for authentication. Format: 20-character alphanumeric string starting with &#39;AKIA&#39; (long-term) or &#39;ASIA&#39; (temporary). Obtain from: AWS Console &gt; IAM &gt; Users &gt; Security Credentials | 
**secret_access_key** | **str** | REQUIRED. AWS secret access key for authentication. SECURITY: This field is encrypted at rest. Never log or expose this value. Format: 40-character base64-encoded string. Obtain from: AWS Console when creating/viewing access key (shown only once) | 
**session_token** | **str** | NOT REQUIRED. Temporary session token for AWS STS credentials. REQUIRED when using temporary security credentials from AWS STS. NOT REQUIRED for long-term IAM user access keys. SECURITY: Encrypted at rest. Automatically expires after session duration. Format: Base64-encoded string, typically several hundred characters. Use case: Enhanced security with automatic credential rotation | [optional] 

## Example

```python
from mixpeek.models.s3_access_key_credentials import S3AccessKeyCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of S3AccessKeyCredentials from a JSON string
s3_access_key_credentials_instance = S3AccessKeyCredentials.from_json(json)
# print the JSON string representation of the object
print(S3AccessKeyCredentials.to_json())

# convert the object into a dict
s3_access_key_credentials_dict = s3_access_key_credentials_instance.to_dict()
# create an instance of S3AccessKeyCredentials from a dict
s3_access_key_credentials_from_dict = S3AccessKeyCredentials.from_dict(s3_access_key_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


