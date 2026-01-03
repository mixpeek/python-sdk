# ListSyncConfigurationsRequest

Request to filter sync configurations for listing.  All filters are optional - when omitted, returns all sync configurations for the bucket. Multiple filters can be combined for precise queries.  Use Cases:     - Find all syncs for a specific connection     - List only active or paused syncs     - Filter by status to find failed syncs  Requirements:     - All fields are OPTIONAL     - Multiple filters are combined with AND logic     - Empty request returns all configurations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_id** | **str** | Filter sync configurations by connection ID. NOT REQUIRED. When provided, only returns syncs using this connection. Useful for managing syncs across multiple storage providers. Example: &#39;conn_abc123&#39; | [optional] 
**status** | [**TaskStatusEnum**](TaskStatusEnum.md) | Filter sync configurations by status. NOT REQUIRED. Valid values: &#39;pending&#39;, &#39;processing&#39;, &#39;completed&#39;, &#39;failed&#39;, &#39;paused&#39;. Useful for finding syncs that need attention or monitoring. Example: &#39;failed&#39; to find syncs with errors. | [optional] 
**is_active** | **bool** | Filter sync configurations by active status. NOT REQUIRED. True: Only active syncs that are currently monitoring/processing. False: Only paused/disabled syncs. Omit to include both active and inactive. | [optional] 

## Example

```python
from mixpeek.models.list_sync_configurations_request import ListSyncConfigurationsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListSyncConfigurationsRequest from a JSON string
list_sync_configurations_request_instance = ListSyncConfigurationsRequest.from_json(json)
# print the JSON string representation of the object
print(ListSyncConfigurationsRequest.to_json())

# convert the object into a dict
list_sync_configurations_request_dict = list_sync_configurations_request_instance.to_dict()
# create an instance of ListSyncConfigurationsRequest from a dict
list_sync_configurations_request_from_dict = ListSyncConfigurationsRequest.from_dict(list_sync_configurations_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


