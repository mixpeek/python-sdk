# TigrisConfig

Tigris Data globally distributed object storage configuration.  Tigris is an S3-compatible object storage service with automatic global distribution, zero egress fees, and built-in CDN capabilities. It uses the AWS S3 API, making integration straightforward.  Key Features:     - S3-compatible API (drop-in replacement)     - Automatic global data distribution     - Zero egress fees     - Built-in CDN and caching     - Strong consistency guarantees  Authentication:     - Access keys only (similar to S3 access keys)     - No IAM role assumption (Tigris is not AWS)  Requirements:     - Tigris account with access keys     - Bucket created in Tigris console     - Network connectivity to fly.storage.tigris.dev  Use Cases:     - Globally distributed media assets     - Low-latency content delivery worldwide     - Cost-effective storage with no egress fees     - S3-compatible workflows outside AWS

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_type** | **str** |  | [optional] [default to 'tigris']
**credentials** | [**TigrisAccessKeyCredentials**](TigrisAccessKeyCredentials.md) | REQUIRED. Tigris access key credentials. Obtain from Tigris Console at https://console.tigris.dev | 
**region** | **str** | Region for Tigris. Typically &#39;auto&#39; for automatic global distribution. Tigris automatically distributes data globally, so region is usually &#39;auto&#39;. Default: auto | [optional] [default to 'auto']
**endpoint_url** | **str** | Tigris S3-compatible endpoint URL. Default: https://fly.storage.tigris.dev This is the standard Tigris endpoint and usually doesn&#39;t need to be changed. | [optional] [default to 'https://fly.storage.tigris.dev']

## Example

```python
from mixpeek.models.tigris_config import TigrisConfig

# TODO update the JSON string below
json = "{}"
# create an instance of TigrisConfig from a JSON string
tigris_config_instance = TigrisConfig.from_json(json)
# print the JSON string representation of the object
print(TigrisConfig.to_json())

# convert the object into a dict
tigris_config_dict = tigris_config_instance.to_dict()
# create an instance of TigrisConfig from a dict
tigris_config_from_dict = TigrisConfig.from_dict(tigris_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


