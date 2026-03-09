# HTTPAPIHeaderCredentials

Optional HTTP credentials for HTTP API endpoints.  Supports arbitrary headers for authentication (API keys, Bearer tokens, etc.). Same pattern as RSS credentials but for REST API endpoints.  Security:     - Header values containing secrets are encrypted at rest via CSFLE     - Common patterns: Authorization: Bearer <token>, X-API-Key: <key>

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'http_headers']
**headers** | **Dict[str, str]** | HTTP headers for API requests (e.g., Authorization, X-API-Key). | [optional] 

## Example

```python
from mixpeek.models.httpapi_header_credentials import HTTPAPIHeaderCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of HTTPAPIHeaderCredentials from a JSON string
httpapi_header_credentials_instance = HTTPAPIHeaderCredentials.from_json(json)
# print the JSON string representation of the object
print(HTTPAPIHeaderCredentials.to_json())

# convert the object into a dict
httpapi_header_credentials_dict = httpapi_header_credentials_instance.to_dict()
# create an instance of HTTPAPIHeaderCredentials from a dict
httpapi_header_credentials_from_dict = HTTPAPIHeaderCredentials.from_dict(httpapi_header_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


