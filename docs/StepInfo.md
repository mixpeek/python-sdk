# StepInfo

Information about a single step in the taxonomy analytics data.  Attributes:     step_key: The step identifier (e.g., \"inquiry\", \"closed_won\")     event_count: Number of events with this step     sequence_count: Number of unique sequences with this step     first_seen: ISO timestamp of earliest event with this step     last_seen: ISO timestamp of most recent event with this step

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**step_key** | **str** | Step identifier | 
**event_count** | **int** | Total events for this step | 
**sequence_count** | **int** | Unique sequences with this step | 
**first_seen** | **str** | Earliest event timestamp (ISO format) | 
**last_seen** | **str** | Most recent event timestamp (ISO format) | 

## Example

```python
from mixpeek.models.step_info import StepInfo

# TODO update the JSON string below
json = "{}"
# create an instance of StepInfo from a JSON string
step_info_instance = StepInfo.from_json(json)
# print the JSON string representation of the object
print(StepInfo.to_json())

# convert the object into a dict
step_info_dict = step_info_instance.to_dict()
# create an instance of StepInfo from a dict
step_info_from_dict = StepInfo.from_dict(step_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


