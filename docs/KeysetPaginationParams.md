# KeysetPaginationParams

Stateless keyset pagination relying on last seen sort key.  Best for: High-performance pagination, large result sets, stable sorting  How it works: - Uses actual field values as pagination markers - Database can use indexes efficiently (WHERE score < 0.73) - No offset calculation or server state - Requires deterministic sort order (e.g., score DESC, id ASC) - Most efficient pagination method  Requirements: - Results must be sorted consistently - Sort fields must be in the \"after\" marker - Example: sorted by (score DESC, id ASC) → after: {score: 0.73, id: \"doc_20\"}  Advantages: - No server-side state (truly stateless) - Consistent even with concurrent writes - Database can use indexes (fast for large datasets) - No offset performance degradation  Use when: - You have stable, deterministic sort fields - Working with large result sets (10k+ docs) - Maximum performance is critical - You need infinite scroll with best efficiency  Example flow: 1. Request: {\"method\": \"keyset\", \"limit\": 20, \"after\": null} 2. Response: {\"documents\": [...], \"next_cursor\": {\"score\": 0.85, \"id\": \"doc_20\"}} 3. Request: {\"method\": \"keyset\", \"limit\": 20, \"after\": {\"score\": 0.85, \"id\": \"doc_20\"}}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | [**PaginationMethod**](PaginationMethod.md) | Constant identifying keyset pagination (REQUIRED). | [optional] 
**limit** | **int** | Maximum number of documents to return per page (REQUIRED). Default: 10. | [optional] [default to 10]
**after** | **Dict[str, object]** | Last seen keyset marker from previous response (OPTIONAL). Must include all sort fields. Example: {&#39;score&#39;: 0.73, &#39;id&#39;: &#39;doc_20&#39;}. null for first page, then use next_cursor from response | [optional] 

## Example

```python
from mixpeek.models.keyset_pagination_params import KeysetPaginationParams

# TODO update the JSON string below
json = "{}"
# create an instance of KeysetPaginationParams from a JSON string
keyset_pagination_params_instance = KeysetPaginationParams.from_json(json)
# print the JSON string representation of the object
print(KeysetPaginationParams.to_json())

# convert the object into a dict
keyset_pagination_params_dict = keyset_pagination_params_instance.to_dict()
# create an instance of KeysetPaginationParams from a dict
keyset_pagination_params_from_dict = KeysetPaginationParams.from_dict(keyset_pagination_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


