# ScrollPaginationParams

Scroll-style pagination maintaining server-side context for TTL.  Best for: Bulk exports, batch processing, iterating through all results  How it works: - Server maintains a snapshot of results - First request: scroll_id=null, returns scroll_id - Subsequent requests: use scroll_id from response - Context expires after scroll_ttl seconds - Consistent view of data (point-in-time snapshot)  Tradeoffs: - Requires server-side state (memory/cache) - TTL means sessions can expire - Not suitable for long-lived sessions - Good for background jobs, not user-facing UIs  Use when: - Exporting large datasets - Batch processing all results - Background jobs iterating through results - You need consistent point-in-time view  Example flow: 1. Request: {\"method\": \"scroll\", \"limit\": 100, \"scroll_id\": null} 2. Response: {\"documents\": [...], \"scroll_id\": \"xyz789\", \"has_next\": true} 3. Request: {\"method\": \"scroll\", \"limit\": 100, \"scroll_id\": \"xyz789\"}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | [**PaginationMethod**](PaginationMethod.md) | Constant identifying scroll pagination (REQUIRED). | [optional] 
**limit** | **int** | Number of documents to fetch per scroll page (REQUIRED). Default: 100. | [optional] [default to 100]
**scroll_id** | **str** | Server-issued scroll session identifier (OPTIONAL). null for first request, then use scroll_id from response | [optional] 
**scroll_ttl** | **int** | Seconds to keep scroll context alive (REQUIRED). Default: 300 (5 minutes). | [optional] [default to 300]

## Example

```python
from mixpeek.models.scroll_pagination_params import ScrollPaginationParams

# TODO update the JSON string below
json = "{}"
# create an instance of ScrollPaginationParams from a JSON string
scroll_pagination_params_instance = ScrollPaginationParams.from_json(json)
# print the JSON string representation of the object
print(ScrollPaginationParams.to_json())

# convert the object into a dict
scroll_pagination_params_dict = scroll_pagination_params_instance.to_dict()
# create an instance of ScrollPaginationParams from a dict
scroll_pagination_params_from_dict = ScrollPaginationParams.from_dict(scroll_pagination_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


