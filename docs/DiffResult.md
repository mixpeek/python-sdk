# DiffResult

Result of comparing manifest to current state.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to_create** | [**List[DiffItem]**](DiffItem.md) | Resources in manifest but not in system | [optional] 
**in_system_only** | [**List[DiffItem]**](DiffItem.md) | Resources in system but not in manifest | [optional] 
**differences** | [**List[DiffItem]**](DiffItem.md) | Resources in both with differences | [optional] 

## Example

```python
from mixpeek.models.diff_result import DiffResult

# TODO update the JSON string below
json = "{}"
# create an instance of DiffResult from a JSON string
diff_result_instance = DiffResult.from_json(json)
# print the JSON string representation of the object
print(DiffResult.to_json())

# convert the object into a dict
diff_result_dict = diff_result_instance.to_dict()
# create an instance of DiffResult from a dict
diff_result_from_dict = DiffResult.from_dict(diff_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


