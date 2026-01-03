# BudgetLimits

User-defined limits for time and credits during execution.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_credits** | **float** | Maximum credits allowed for a single execution (OPTIONAL). | [optional] 
**max_time_ms** | **int** | Maximum wall-clock time in milliseconds before forcing halt (OPTIONAL). | [optional] 

## Example

```python
from mixpeek.models.budget_limits import BudgetLimits

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetLimits from a JSON string
budget_limits_instance = BudgetLimits.from_json(json)
# print the JSON string representation of the object
print(BudgetLimits.to_json())

# convert the object into a dict
budget_limits_dict = budget_limits_instance.to_dict()
# create an instance of BudgetLimits from a dict
budget_limits_from_dict = BudgetLimits.from_dict(budget_limits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


