# HealthCheckOutput

Health check information for a retriever.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**SharedRetrieversModelsHealthStatus**](SharedRetrieversModelsHealthStatus.md) | Current health status | [optional] 
**last_check** | **datetime** | When the health was last checked | [optional] 
**issues** | **List[str]** | List of current issues if any | [optional] 

## Example

```python
from mixpeek.models.health_check_output import HealthCheckOutput

# TODO update the JSON string below
json = "{}"
# create an instance of HealthCheckOutput from a JSON string
health_check_output_instance = HealthCheckOutput.from_json(json)
# print the JSON string representation of the object
print(HealthCheckOutput.to_json())

# convert the object into a dict
health_check_output_dict = health_check_output_instance.to_dict()
# create an instance of HealthCheckOutput from a dict
health_check_output_from_dict = HealthCheckOutput.from_dict(health_check_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


