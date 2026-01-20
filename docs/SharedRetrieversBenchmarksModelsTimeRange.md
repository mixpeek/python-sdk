# SharedRetrieversBenchmarksModelsTimeRange

Time range filter for session queries.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **datetime** | Start of time range (inclusive). | [optional] 
**end** | **datetime** | End of time range (inclusive). | [optional] 

## Example

```python
from mixpeek.models.shared_retrievers_benchmarks_models_time_range import SharedRetrieversBenchmarksModelsTimeRange

# TODO update the JSON string below
json = "{}"
# create an instance of SharedRetrieversBenchmarksModelsTimeRange from a JSON string
shared_retrievers_benchmarks_models_time_range_instance = SharedRetrieversBenchmarksModelsTimeRange.from_json(json)
# print the JSON string representation of the object
print(SharedRetrieversBenchmarksModelsTimeRange.to_json())

# convert the object into a dict
shared_retrievers_benchmarks_models_time_range_dict = shared_retrievers_benchmarks_models_time_range_instance.to_dict()
# create an instance of SharedRetrieversBenchmarksModelsTimeRange from a dict
shared_retrievers_benchmarks_models_time_range_from_dict = SharedRetrieversBenchmarksModelsTimeRange.from_dict(shared_retrievers_benchmarks_models_time_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


