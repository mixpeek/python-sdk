# HealthServiceStatus

Status flags for dependent services.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cache** | **bool** | Cache layer connectivity successful | 
**metadata** | **bool** | Metadata store connectivity successful | 
**vector_store** | **bool** | Vector database connectivity successful | 
**object_storage** | **bool** | Object storage connectivity successful | 
**task_queue** | **bool** | Task queue execution successful | 
**inference** | **bool** | Inference engine health check successful | 
**analytics** | **bool** | Analytics backend healthy (optional, None if disabled) | [optional] 

## Example

```python
from mixpeek.models.health_service_status import HealthServiceStatus

# TODO update the JSON string below
json = "{}"
# create an instance of HealthServiceStatus from a JSON string
health_service_status_instance = HealthServiceStatus.from_json(json)
# print the JSON string representation of the object
print(HealthServiceStatus.to_json())

# convert the object into a dict
health_service_status_dict = health_service_status_instance.to_dict()
# create an instance of HealthServiceStatus from a dict
health_service_status_from_dict = HealthServiceStatus.from_dict(health_service_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


