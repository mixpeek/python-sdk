# ConfigureCORSRequest

Request model for configuring CORS on object storage.  This allows administrators to configure CORS policies on the object storage bucket to enable browser-based uploads using presigned URLs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_origins** | **List[str]** | List of allowed origins for CORS. These are the frontend URLs that will be allowed to upload directly to object storage. REQUIRED. Must be valid HTTP/HTTPS URLs. Examples: [&#39;http://localhost:8080&#39;, &#39;https://app.example.com&#39;] | 
**allowed_methods** | **List[str]** | HTTP methods to allow for CORS requests. OPTIONAL - defaults to [&#39;GET&#39;, &#39;PUT&#39;, &#39;POST&#39;, &#39;HEAD&#39;, &#39;DELETE&#39;] if not provided. Common methods: GET (download), PUT (upload), POST (multipart upload), HEAD (metadata check) | [optional] 
**allowed_headers** | **List[str]** | Headers that are allowed in CORS requests. OPTIONAL - defaults to [&#39;*&#39;] (allow all headers) if not provided. Use [&#39;*&#39;] for maximum compatibility or specify specific headers. | [optional] 
**expose_headers** | **List[str]** | Headers that browsers are allowed to access in responses. OPTIONAL - defaults to [&#39;ETag&#39;, &#39;x-amz-request-id&#39;] if not provided. &#39;ETag&#39; is particularly important for upload confirmation. | [optional] 
**max_age_seconds** | **int** | How long (in seconds) browsers should cache preflight request results. OPTIONAL - defaults to 3000 seconds (50 minutes) if not provided. Higher values reduce preflight requests but may delay policy updates. | [optional] 

## Example

```python
from mixpeek.models.configure_cors_request import ConfigureCORSRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigureCORSRequest from a JSON string
configure_cors_request_instance = ConfigureCORSRequest.from_json(json)
# print the JSON string representation of the object
print(ConfigureCORSRequest.to_json())

# convert the object into a dict
configure_cors_request_dict = configure_cors_request_instance.to_dict()
# create an instance of ConfigureCORSRequest from a dict
configure_cors_request_from_dict = ConfigureCORSRequest.from_dict(configure_cors_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


