# TigrisAccessKeyCredentials

Tigris Data access key credentials.  Tigris uses S3-compatible authentication with access keys. Credentials can be obtained from the Tigris dashboard at https://console.tigris.dev.  Prerequisites:     - Create a Tigris account at https://www.tigrisdata.com     - Create a bucket in the Tigris console     - Generate access keys from the dashboard  Security:     - secret_access_key is encrypted at rest using MongoDB CSFLE     - Rotate keys regularly via the Tigris dashboard     - Use bucket-scoped keys when possible for least privilege  Use Cases:     - Globally distributed object storage     - Low-latency content delivery     - S3-compatible workflows with zero egress fees

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'access_key']
**access_key_id** | **str** | REQUIRED. Tigris access key ID for authentication. Obtain from: Tigris Console &gt; Access Keys | 
**secret_access_key** | **str** | REQUIRED. Tigris secret access key for authentication. SECURITY: This field is encrypted at rest. Never log or expose this value. Obtain from: Tigris Console when creating access key (shown only once) | 

## Example

```python
from mixpeek.models.tigris_access_key_credentials import TigrisAccessKeyCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of TigrisAccessKeyCredentials from a JSON string
tigris_access_key_credentials_instance = TigrisAccessKeyCredentials.from_json(json)
# print the JSON string representation of the object
print(TigrisAccessKeyCredentials.to_json())

# convert the object into a dict
tigris_access_key_credentials_dict = tigris_access_key_credentials_instance.to_dict()
# create an instance of TigrisAccessKeyCredentials from a dict
tigris_access_key_credentials_from_dict = TigrisAccessKeyCredentials.from_dict(tigris_access_key_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


