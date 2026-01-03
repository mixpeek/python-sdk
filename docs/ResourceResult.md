# ResourceResult

Result of applying a single resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_type** | **str** | Type of resource (namespace, bucket, etc.) | 
**name** | **str** | Resource name from manifest | 
**resource_id** | **str** | Created resource ID | [optional] 
**status** | [**ResourceResultStatus**](ResourceResultStatus.md) | Result status | 
**error** | **str** | Error message if failed | [optional] 

## Example

```python
from mixpeek.models.resource_result import ResourceResult

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceResult from a JSON string
resource_result_instance = ResourceResult.from_json(json)
# print the JSON string representation of the object
print(ResourceResult.to_json())

# convert the object into a dict
resource_result_dict = resource_result_instance.to_dict()
# create an instance of ResourceResult from a dict
resource_result_from_dict = ResourceResult.from_dict(resource_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


