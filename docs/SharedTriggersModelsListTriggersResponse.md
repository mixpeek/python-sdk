# SharedTriggersModelsListTriggersResponse

Response for list triggers request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[SharedTriggersModelsTriggerModel]**](SharedTriggersModelsTriggerModel.md) | List of triggers | 
**total** | **int** | Total number of triggers | 
**offset** | **int** | Current offset | 
**limit** | **int** | Current limit | 

## Example

```python
from mixpeek.models.shared_triggers_models_list_triggers_response import SharedTriggersModelsListTriggersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SharedTriggersModelsListTriggersResponse from a JSON string
shared_triggers_models_list_triggers_response_instance = SharedTriggersModelsListTriggersResponse.from_json(json)
# print the JSON string representation of the object
print(SharedTriggersModelsListTriggersResponse.to_json())

# convert the object into a dict
shared_triggers_models_list_triggers_response_dict = shared_triggers_models_list_triggers_response_instance.to_dict()
# create an instance of SharedTriggersModelsListTriggersResponse from a dict
shared_triggers_models_list_triggers_response_from_dict = SharedTriggersModelsListTriggersResponse.from_dict(shared_triggers_models_list_triggers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


