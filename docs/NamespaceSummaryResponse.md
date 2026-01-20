# NamespaceSummaryResponse

Comprehensive namespace analytics summary.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**namespace_id** | **str** | Namespace ID analyzed | 
**time_range_days** | **int** | Number of days analyzed | 
**summary** | **object** | Summary statistics (total_fields_analyzed, high_priority_indexes, etc.) | 
**recommendations** | [**List[IndexRecommendation]**](IndexRecommendation.md) | Top index recommendations | 
**most_queried_fields** | [**List[FieldQueryMetrics]**](FieldQueryMetrics.md) | Most frequently queried fields | 
**slowest_fields** | [**List[FieldPerformanceMetrics]**](FieldPerformanceMetrics.md) | Fields with highest latency | 
**compound_indexes** | [**List[CompoundIndexPattern]**](CompoundIndexPattern.md) | Compound index opportunities | 

## Example

```python
from mixpeek.models.namespace_summary_response import NamespaceSummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NamespaceSummaryResponse from a JSON string
namespace_summary_response_instance = NamespaceSummaryResponse.from_json(json)
# print the JSON string representation of the object
print(NamespaceSummaryResponse.to_json())

# convert the object into a dict
namespace_summary_response_dict = namespace_summary_response_instance.to_dict()
# create an instance of NamespaceSummaryResponse from a dict
namespace_summary_response_from_dict = NamespaceSummaryResponse.from_dict(namespace_summary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


