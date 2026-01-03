# CompoundIndexResponse

Response for compound index patterns endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**namespace_id** | **str** | Namespace ID analyzed | 
**time_range_days** | **int** | Number of days analyzed | 
**patterns** | [**List[CompoundIndexPattern]**](CompoundIndexPattern.md) | Compound field patterns | 
**total_patterns** | **int** | Total patterns found | 

## Example

```python
from mixpeek.models.compound_index_response import CompoundIndexResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CompoundIndexResponse from a JSON string
compound_index_response_instance = CompoundIndexResponse.from_json(json)
# print the JSON string representation of the object
print(CompoundIndexResponse.to_json())

# convert the object into a dict
compound_index_response_dict = compound_index_response_instance.to_dict()
# create an instance of CompoundIndexResponse from a dict
compound_index_response_from_dict = CompoundIndexResponse.from_dict(compound_index_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


