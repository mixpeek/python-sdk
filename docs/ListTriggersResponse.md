# ListTriggersResponse

Response for list triggers request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**triggers** | [**List[TriggerModel]**](TriggerModel.md) | List of triggers | 
**total** | **int** | Total number of triggers | 
**offset** | **int** | Current offset | 
**limit** | **int** | Current limit | 

## Example

```python
from mixpeek.models.list_triggers_response import ListTriggersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListTriggersResponse from a JSON string
list_triggers_response_instance = ListTriggersResponse.from_json(json)
# print the JSON string representation of the object
print(ListTriggersResponse.to_json())

# convert the object into a dict
list_triggers_response_dict = list_triggers_response_instance.to_dict()
# create an instance of ListTriggersResponse from a dict
list_triggers_response_from_dict = ListTriggersResponse.from_dict(list_triggers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


