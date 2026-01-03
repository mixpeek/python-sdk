# S3RoleCredentials

AWS S3 IAM role assumption credentials (RECOMMENDED for production).  IAM role assumption provides secure, temporary credentials for accessing customer S3 buckets without sharing long-lived access keys. This is the recommended authentication method for production deployments.  How It Works:     1. Customer creates an IAM role in their AWS account     2. Role trust policy allows Mixpeek AWS account to assume the role     3. External ID provides additional security against confused deputy attacks     4. Mixpeek assumes the role and receives temporary credentials (auto-renewed)     5. Temporary credentials are used to access the customer's S3 bucket  Prerequisites:     1. Create IAM role in customer AWS account     2. Attach policy granting s3:GetObject, s3:ListBucket permissions     3. Configure trust relationship to allow Mixpeek account     4. Use organization-specific external_id for security     5. Share role ARN with Mixpeek  Security Advantages:     - No long-lived credentials shared with third parties     - Temporary credentials automatically rotate (1-hour sessions by default)     - Customer retains full control and can revoke access anytime     - External ID prevents confused deputy attacks     - Audit trail in CloudTrail for all access  Use Cases:     - Production deployments accessing customer S3 buckets     - Enterprise integrations requiring strong security     - Multi-tenant environments with customer-owned storage     - Compliance-sensitive workloads (HIPAA, SOC 2, etc.)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'iam_role']
**role_arn** | **str** | REQUIRED. Amazon Resource Name (ARN) of the IAM role to assume. This role must exist in the customer&#39;s AWS account and have a trust relationship configured to allow Mixpeek to assume it. Format: arn:aws:iam::{account-id}:role/{role-name} Example trust policy should allow principal: arn:aws:iam::{mixpeek-account}:root Recommended role name: mixpeek-storage-sync-role | 
**external_id** | **str** | REQUIRED. External ID for secure role assumption (prevents confused deputy attacks). This value should be unique to your organization and kept confidential. Mixpeek provides this value during connection setup. Must match the ExternalId condition in the role&#39;s trust policy. Format: Recommended pattern is mixpeek-{organization_id} Security: Include this in the trust policy Condition statement | 

## Example

```python
from mixpeek.models.s3_role_credentials import S3RoleCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of S3RoleCredentials from a JSON string
s3_role_credentials_instance = S3RoleCredentials.from_json(json)
# print the JSON string representation of the object
print(S3RoleCredentials.to_json())

# convert the object into a dict
s3_role_credentials_dict = s3_role_credentials_instance.to_dict()
# create an instance of S3RoleCredentials from a dict
s3_role_credentials_from_dict = S3RoleCredentials.from_dict(s3_role_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


