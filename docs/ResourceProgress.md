# ResourceProgress

Progress tracking for individual resources.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** | Resource ID | 
**resource_type** | [**SharedNamespacesMigrationsModelsResourceType**](SharedNamespacesMigrationsModelsResourceType.md) | Resource type | 
**status** | [**MigrationStatus**](MigrationStatus.md) | Resource status | 
**progress_percent** | **float** | Progress % | [optional] [default to 0.0]
**error_message** | **str** | Error if failed | [optional] 

## Example

```python
from mixpeek.models.resource_progress import ResourceProgress

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceProgress from a JSON string
resource_progress_instance = ResourceProgress.from_json(json)
# print the JSON string representation of the object
print(ResourceProgress.to_json())

# convert the object into a dict
resource_progress_dict = resource_progress_instance.to_dict()
# create an instance of ResourceProgress from a dict
resource_progress_from_dict = ResourceProgress.from_dict(resource_progress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


