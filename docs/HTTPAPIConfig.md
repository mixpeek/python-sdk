# HTTPAPIConfig

REST/HTTP JSON API configuration. source_path = API URL.  Enables Mixpeek to sync items from any JSON REST API endpoint. Each item in the API response becomes a bucket object with its JSON body stored as the blob.  Authentication:     - Optional HTTP headers (API keys, Bearer tokens, etc.)  Requirements:     - API must return JSON (or JSONL) response     - Response must contain an array of items (at root or nested path)     - Each item must have a unique ID field for deduplication  Use Cases:     - Sync data from public APIs (Hacker News, GitHub, etc.)     - Ingest records from internal REST services     - Poll third-party APIs (Stripe, Shopify, etc.)     - Monitor any JSON endpoint for new items

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_type** | **str** |  | [optional] [default to 'http_api']
**credentials** | [**HTTPAPIHeaderCredentials**](HTTPAPIHeaderCredentials.md) | Optional HTTP headers for authenticated API endpoints. | [optional] 
**http_method** | **str** | HTTP method to use when calling the API. | [optional] [default to 'GET']
**request_body** | **Dict[str, object]** | Optional JSON body for POST requests. | [optional] 
**items_path** | **str** | Dot-notation path to the array of items in the JSON response. Examples: &#39;hits&#39; for {hits: [...]}, &#39;data.items&#39; for {data: {items: [...]}}. Leave empty if the response is a top-level array. | [optional] [default to '']
**item_id_field** | **str** | REQUIRED. Field name in each item used as a unique ID for deduplication. Examples: &#39;id&#39;, &#39;objectID&#39;, &#39;uuid&#39;. | 
**item_modified_field** | **str** | Optional field name for a timestamp used for incremental sync. Supports ISO 8601 strings and Unix timestamps. Examples: &#39;updated_at&#39;, &#39;created_at&#39;, &#39;modified&#39;. | [optional] 
**response_content_type** | **str** | Response format: &#39;json&#39; (default) or &#39;jsonl&#39; (newline-delimited JSON). | [optional] [default to 'json']
**user_agent** | **str** | User-Agent header for API requests. | [optional] [default to 'Mixpeek HTTP API Sync/1.0']
**request_timeout** | **int** | HTTP request timeout in seconds. | [optional] [default to 30]

## Example

```python
from mixpeek.models.httpapi_config import HTTPAPIConfig

# TODO update the JSON string below
json = "{}"
# create an instance of HTTPAPIConfig from a JSON string
httpapi_config_instance = HTTPAPIConfig.from_json(json)
# print the JSON string representation of the object
print(HTTPAPIConfig.to_json())

# convert the object into a dict
httpapi_config_dict = httpapi_config_instance.to_dict()
# create an instance of HTTPAPIConfig from a dict
httpapi_config_from_dict = HTTPAPIConfig.from_dict(httpapi_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


