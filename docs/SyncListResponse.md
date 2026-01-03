# SyncListResponse

Response containing a list of sync configurations with pagination.  Wraps the list of sync configurations with pagination metadata to support efficient browsing of large result sets.  Response Structure:     - results: The actual sync configuration objects     - pagination: Links and metadata for navigation     - total: Total count for client-side progress indicators

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[SyncConfigurationModel]**](SyncConfigurationModel.md) | List of sync configurations matching the query filters. ALWAYS PRESENT. May be empty if no configurations match. Each item is a complete SyncConfigurationModel. Ordered by creation date (newest first). | 
**pagination** | [**PaginationResponse**](PaginationResponse.md) | Pagination metadata for navigating result sets. ALWAYS PRESENT. Contains next/previous links, current page info. Use the provided links for cursor-based pagination. | 
**total** | **int** | Total number of sync configurations matching the filters. ALWAYS PRESENT. Useful for progress indicators and UI display. Note: This is the total across all pages, not just current page. | 

## Example

```python
from mixpeek.models.sync_list_response import SyncListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SyncListResponse from a JSON string
sync_list_response_instance = SyncListResponse.from_json(json)
# print the JSON string representation of the object
print(SyncListResponse.to_json())

# convert the object into a dict
sync_list_response_dict = sync_list_response_instance.to_dict()
# create an instance of SyncListResponse from a dict
sync_list_response_from_dict = SyncListResponse.from_dict(sync_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


