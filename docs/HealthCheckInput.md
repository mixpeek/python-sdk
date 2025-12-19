# HealthCheckInput

Health check information for a retriever.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**HealthStatusInput**](HealthStatusInput.md) | Current health status | [optional] 
**last_check** | **datetime** | When the health was last checked | [optional] 
**issues** | **List[str]** | List of current issues if any | [optional] 

## Example

```python
from mixpeek.models.health_check_input import HealthCheckInput

# TODO update the JSON string below
json = "{}"
# create an instance of HealthCheckInput from a JSON string
health_check_input_instance = HealthCheckInput.from_json(json)
# print the JSON string representation of the object
print(HealthCheckInput.to_json())

# convert the object into a dict
health_check_input_dict = health_check_input_instance.to_dict()
# create an instance of HealthCheckInput from a dict
health_check_input_from_dict = HealthCheckInput.from_dict(health_check_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


