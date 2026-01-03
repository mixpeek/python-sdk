# CompoundIndexPattern

Pattern of fields commonly queried together.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_combination** | **List[str]** | Fields used together | 
**combination_count** | **int** | Number of times this combination was used | 
**avg_latency_ms** | **float** | Average latency for this combination | 
**p95_latency_ms** | **float** | 95th percentile latency | 

## Example

```python
from mixpeek.models.compound_index_pattern import CompoundIndexPattern

# TODO update the JSON string below
json = "{}"
# create an instance of CompoundIndexPattern from a JSON string
compound_index_pattern_instance = CompoundIndexPattern.from_json(json)
# print the JSON string representation of the object
print(CompoundIndexPattern.to_json())

# convert the object into a dict
compound_index_pattern_dict = compound_index_pattern_instance.to_dict()
# create an instance of CompoundIndexPattern from a dict
compound_index_pattern_from_dict = CompoundIndexPattern.from_dict(compound_index_pattern_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


