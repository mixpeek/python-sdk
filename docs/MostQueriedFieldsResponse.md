# MostQueriedFieldsResponse

Response for most queried fields endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**namespace_id** | **str** | Namespace ID analyzed | 
**time_range_days** | **int** | Number of days analyzed | 
**fields** | [**List[FieldQueryMetrics]**](FieldQueryMetrics.md) | Most queried fields | 
**total_fields** | **int** | Total unique fields found | 

## Example

```python
from mixpeek.models.most_queried_fields_response import MostQueriedFieldsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MostQueriedFieldsResponse from a JSON string
most_queried_fields_response_instance = MostQueriedFieldsResponse.from_json(json)
# print the JSON string representation of the object
print(MostQueriedFieldsResponse.to_json())

# convert the object into a dict
most_queried_fields_response_dict = most_queried_fields_response_instance.to_dict()
# create an instance of MostQueriedFieldsResponse from a dict
most_queried_fields_response_from_dict = MostQueriedFieldsResponse.from_dict(most_queried_fields_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


