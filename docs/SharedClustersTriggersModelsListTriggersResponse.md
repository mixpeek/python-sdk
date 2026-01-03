# SharedClustersTriggersModelsListTriggersResponse

Response for list triggers request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[SharedClustersTriggersModelsTriggerModel]**](SharedClustersTriggersModelsTriggerModel.md) | List of triggers | 
**total** | **int** | Total number of triggers | 
**offset** | **int** | Current offset | 
**limit** | **int** | Current limit | 

## Example

```python
from mixpeek.models.shared_clusters_triggers_models_list_triggers_response import SharedClustersTriggersModelsListTriggersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SharedClustersTriggersModelsListTriggersResponse from a JSON string
shared_clusters_triggers_models_list_triggers_response_instance = SharedClustersTriggersModelsListTriggersResponse.from_json(json)
# print the JSON string representation of the object
print(SharedClustersTriggersModelsListTriggersResponse.to_json())

# convert the object into a dict
shared_clusters_triggers_models_list_triggers_response_dict = shared_clusters_triggers_models_list_triggers_response_instance.to_dict()
# create an instance of SharedClustersTriggersModelsListTriggersResponse from a dict
shared_clusters_triggers_models_list_triggers_response_from_dict = SharedClustersTriggersModelsListTriggersResponse.from_dict(shared_clusters_triggers_models_list_triggers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


