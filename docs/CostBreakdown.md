# CostBreakdown

Cost breakdown by category.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**storage_percent** | **float** | Storage cost percentage | 
**upload_percent** | **float** | Upload cost percentage | 
**sync_percent** | **float** | Sync cost percentage | 
**other_percent** | **float** | Other cost percentage | 

## Example

```python
from mixpeek.models.cost_breakdown import CostBreakdown

# TODO update the JSON string below
json = "{}"
# create an instance of CostBreakdown from a JSON string
cost_breakdown_instance = CostBreakdown.from_json(json)
# print the JSON string representation of the object
print(CostBreakdown.to_json())

# convert the object into a dict
cost_breakdown_dict = cost_breakdown_instance.to_dict()
# create an instance of CostBreakdown from a dict
cost_breakdown_from_dict = CostBreakdown.from_dict(cost_breakdown_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


