# CostRate

Cost rate for a specific billing unit.  Defines how many credits are charged per unit of a specific type.  Example:     CostRate(         unit=CostUnit.MINUTE,         credits_per_unit=200,         description=\"Video processing\"     )     # Means: 200 credits per minute of video

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit** | [**CostUnit**](CostUnit.md) | The billing unit type | 
**credits_per_unit** | **int** | Number of credits charged per unit | 
**description** | **str** | Human-readable description of what this rate covers | [optional] 

## Example

```python
from mixpeek.models.cost_rate import CostRate

# TODO update the JSON string below
json = "{}"
# create an instance of CostRate from a JSON string
cost_rate_instance = CostRate.from_json(json)
# print the JSON string representation of the object
print(CostRate.to_json())

# convert the object into a dict
cost_rate_dict = cost_rate_instance.to_dict()
# create an instance of CostRate from a dict
cost_rate_from_dict = CostRate.from_dict(cost_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


