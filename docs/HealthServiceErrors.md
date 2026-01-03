# HealthServiceErrors

Optional error messages for dependent services (present when a check fails).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cache** | **str** | Cache layer error message, if any | [optional] 
**metadata** | **str** | Metadata store error message, if any | [optional] 
**vector_store** | **str** | Vector database error message, if any | [optional] 
**object_storage** | **str** | Object storage error message, if any | [optional] 
**task_queue** | **str** | Task queue error message, if any | [optional] 
**inference** | **str** | Inference engine error message, if any | [optional] 
**analytics** | **str** | Analytics backend error message, if any | [optional] 

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


