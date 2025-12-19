# HealthServiceErrors

Optional error messages for dependent services (present when a check fails).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redis** | **str** | Redis error message, if any | [optional] 
**mongodb** | **str** | MongoDB error message, if any | [optional] 
**qdrant** | **str** | Qdrant error message, if any | [optional] 
**s3** | **str** | S3 error message, if any | [optional] 
**celery** | **str** | Celery error message, if any | [optional] 
**engine** | **str** | Engine error message, if any | [optional] 

## Example

```python
from mixpeek.models.health_service_errors import HealthServiceErrors

# TODO update the JSON string below
json = "{}"
# create an instance of HealthServiceErrors from a JSON string
health_service_errors_instance = HealthServiceErrors.from_json(json)
# print the JSON string representation of the object
print(HealthServiceErrors.to_json())

# convert the object into a dict
health_service_errors_dict = health_service_errors_instance.to_dict()
# create an instance of HealthServiceErrors from a dict
health_service_errors_from_dict = HealthServiceErrors.from_dict(health_service_errors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


