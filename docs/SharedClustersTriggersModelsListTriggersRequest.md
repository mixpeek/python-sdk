# SharedClustersTriggersModelsListTriggersRequest

Request to list triggers with filters and pagination.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **str** | Filter by cluster ID | [optional] 
**trigger_type** | [**SharedClustersTriggersModelsTriggerType**](SharedClustersTriggersModelsTriggerType.md) | Filter by trigger type | [optional] 
**status** | [**SharedClustersTriggersModelsTriggerStatus**](SharedClustersTriggersModelsTriggerStatus.md) | Filter by status | [optional] 
**offset** | **int** | Pagination offset | [optional] [default to 0]
**limit** | **int** | Results per page | [optional] [default to 50]
**sort_by** | **str** | Field to sort by | [optional] [default to 'created_at']
**direction** | **str** | Sort direction (asc/desc) | [optional] [default to 'desc']

## Example

```python
from mixpeek.models.shared_clusters_triggers_models_list_triggers_request import SharedClustersTriggersModelsListTriggersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SharedClustersTriggersModelsListTriggersRequest from a JSON string
shared_clusters_triggers_models_list_triggers_request_instance = SharedClustersTriggersModelsListTriggersRequest.from_json(json)
# print the JSON string representation of the object
print(SharedClustersTriggersModelsListTriggersRequest.to_json())

# convert the object into a dict
shared_clusters_triggers_models_list_triggers_request_dict = shared_clusters_triggers_models_list_triggers_request_instance.to_dict()
# create an instance of SharedClustersTriggersModelsListTriggersRequest from a dict
shared_clusters_triggers_models_list_triggers_request_from_dict = SharedClustersTriggersModelsListTriggersRequest.from_dict(shared_clusters_triggers_models_list_triggers_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


