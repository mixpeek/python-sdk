# TransitionLifecycleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lifecycle_state** | [**LifecycleState**](LifecycleState.md) | Target lifecycle state for the collection | 
**async_transition** | **bool** | If False, block until the transition completes | [optional] [default to True]

## Example

```python
from mixpeek.models.transition_lifecycle_request import TransitionLifecycleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransitionLifecycleRequest from a JSON string
transition_lifecycle_request_instance = TransitionLifecycleRequest.from_json(json)
# print the JSON string representation of the object
print(TransitionLifecycleRequest.to_json())

# convert the object into a dict
transition_lifecycle_request_dict = transition_lifecycle_request_instance.to_dict()
# create an instance of TransitionLifecycleRequest from a dict
transition_lifecycle_request_from_dict = TransitionLifecycleRequest.from_dict(transition_lifecycle_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


