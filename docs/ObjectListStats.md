# ObjectListStats

Aggregate statistics for a list of objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_objects** | **int** | Total number of objects in the result | [optional] [default to 0]
**total_blobs** | **int** | Total number of blobs across all objects | [optional] [default to 0]
**avg_blobs_per_object** | **float** | Average number of blobs per object | [optional] [default to 0.0]
**objects_by_status** | **Dict[str, object]** | Count of objects grouped by status | [optional] 

## Example

```python
from mixpeek.models.object_list_stats import ObjectListStats

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectListStats from a JSON string
object_list_stats_instance = ObjectListStats.from_json(json)
# print the JSON string representation of the object
print(ObjectListStats.to_json())

# convert the object into a dict
object_list_stats_dict = object_list_stats_instance.to_dict()
# create an instance of ObjectListStats from a dict
object_list_stats_from_dict = ObjectListStats.from_dict(object_list_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


