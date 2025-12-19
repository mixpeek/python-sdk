# HealthCheckResponse

Health check response model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ApiHealthHealthStatus**](ApiHealthHealthStatus.md) | Overall API health status | 
**data** | [**HealthServiceStatus**](HealthServiceStatus.md) | Per-service health status flags | 
**errors** | [**HealthServiceErrors**](HealthServiceErrors.md) | Optional per-service error messages when a service check fails | [optional] 
**meta** | **Dict[str, object]** | Optional metadata such as configured S3 bucket/region/endpoint | [optional] 

## Example

```python
from mixpeek.models.health_check_response import HealthCheckResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HealthCheckResponse from a JSON string
health_check_response_instance = HealthCheckResponse.from_json(json)
# print the JSON string representation of the object
print(HealthCheckResponse.to_json())

# convert the object into a dict
health_check_response_dict = health_check_response_instance.to_dict()
# create an instance of HealthCheckResponse from a dict
health_check_response_from_dict = HealthCheckResponse.from_dict(health_check_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


