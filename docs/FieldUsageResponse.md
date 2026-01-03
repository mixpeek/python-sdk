# FieldUsageResponse

Response containing field usage statistics.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**namespace_id** | **str** | Namespace being analyzed | 
**period** | **str** | Analysis period (24h, 7d, 30d) | 
**fields** | [**List[FieldUsageStat]**](FieldUsageStat.md) | Field usage statistics | 
**total_fields** | **int** | Total number of fields found | 
**indexed_fields** | **int** | Number of indexed fields | 
**unindexed_fields** | **int** | Number of unindexed fields | 

## Example

```python
from mixpeek.models.field_usage_response import FieldUsageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FieldUsageResponse from a JSON string
field_usage_response_instance = FieldUsageResponse.from_json(json)
# print the JSON string representation of the object
print(FieldUsageResponse.to_json())

# convert the object into a dict
field_usage_response_dict = field_usage_response_instance.to_dict()
# create an instance of FieldUsageResponse from a dict
field_usage_response_from_dict = FieldUsageResponse.from_dict(field_usage_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


