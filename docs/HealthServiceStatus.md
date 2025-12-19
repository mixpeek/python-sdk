# HealthServiceStatus

Status flags for dependent services.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redis** | **bool** | Connectivity to Redis successful | 
**mongodb** | **bool** | Connectivity to MongoDB successful | 
**qdrant** | **bool** | Connectivity to Qdrant successful | 
**s3** | **bool** | Connectivity to S3 successful | 
**celery** | **bool** | Celery task execution successful | 
**engine** | **bool** | Engine HTTP health endpoint responded healthy | 

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


