# S3Config

Amazon S3 and S3-compatible storage provider configuration.  This configuration enables Mixpeek to connect to Amazon S3 or S3-compatible storage services (MinIO, DigitalOcean Spaces, Wasabi, Backblaze B2, etc.) for automated object ingestion and synchronization.  Authentication Methods:     1. IAM Role Assumption (RECOMMENDED for production):         - Most secure option with automatic credential rotation         - No long-lived credentials shared         - Ideal for customer-owned S3 buckets      2. Access Keys:         - Simpler setup for development and testing         - Works with S3-compatible services         - Requires manual credential rotation  Requirements:     - Valid AWS credentials or IAM role configuration     - S3 bucket with appropriate permissions (s3:GetObject, s3:ListBucket)     - Network connectivity to S3 endpoint     - Correct region configuration  Supported Services:     - Amazon S3 (all regions)     - MinIO (self-hosted or cloud)     - DigitalOcean Spaces     - Wasabi Cloud Storage     - Backblaze B2     - Any S3-compatible storage with compatible API  Use Cases:     - Ingest videos from data lakes     - Sync images from marketing asset buckets     - Process documents from archive storage     - Monitor and index uploaded files     - Backup and disaster recovery workflows

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_type** | **str** |  | [optional] [default to 's3']
**credentials** | [**Credentials1**](Credentials1.md) |  | 
**region** | **str** | REQUIRED. AWS region where the S3 bucket is located. Must match the bucket&#39;s actual region to avoid routing errors. For S3-compatible services, use their documented region value or &#39;us-east-1&#39; as a default if regions are not applicable. Format: AWS region code (e.g., us-east-1, eu-west-1) | 
**endpoint_url** | **str** | NOT REQUIRED for AWS S3 (uses default AWS endpoints). REQUIRED for S3-compatible services to specify custom endpoint URL. Must be a valid HTTPS or HTTP URL without trailing slash. Examples: - MinIO: https://minio.example.com - DigitalOcean Spaces: https://nyc3.digitaloceanspaces.com - Wasabi: https://s3.wasabisys.com | [optional] 
**use_ssl** | **bool** | Whether to use TLS/SSL encryption for connections to S3. RECOMMENDED: Always True for production environments. Set to False only for local development with unencrypted endpoints. Default: True | [optional] [default to True]
**verify_ssl** | **bool** | Whether to verify TLS/SSL certificates when connecting. RECOMMENDED: Always True for production to prevent MITM attacks. Set to False only for development with self-signed certificates. Requires use_ssl&#x3D;True to have any effect. Default: True | [optional] [default to True]

## Example

```python
from mixpeek.models.s3_config import S3Config

# TODO update the JSON string below
json = "{}"
# create an instance of S3Config from a JSON string
s3_config_instance = S3Config.from_json(json)
# print the JSON string representation of the object
print(S3Config.to_json())

# convert the object into a dict
s3_config_dict = s3_config_instance.to_dict()
# create an instance of S3Config from a dict
s3_config_from_dict = S3Config.from_dict(s3_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


