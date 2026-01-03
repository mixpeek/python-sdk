# ApplyResult

Result of applying a manifest.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Whether all resources were created successfully | 
**resources** | [**List[ResourceResult]**](ResourceResult.md) | Results for each resource | [optional] 
**created_count** | **int** | Number of resources created | [optional] [default to 0]
**failed_count** | **int** | Number of resources that failed | [optional] [default to 0]
**skipped_count** | **int** | Number of resources skipped | [optional] [default to 0]
**errors** | **List[str]** | Error messages | [optional] 
**rollback_performed** | **bool** | Whether rollback was performed due to failure | [optional] [default to False]
**dry_run** | **bool** | Whether this was a dry run (no changes made) | [optional] [default to False]

## Example

```python
from mixpeek.models.apply_result import ApplyResult

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyResult from a JSON string
apply_result_instance = ApplyResult.from_json(json)
# print the JSON string representation of the object
print(ApplyResult.to_json())

# convert the object into a dict
apply_result_dict = apply_result_instance.to_dict()
# create an instance of ApplyResult from a dict
apply_result_from_dict = ApplyResult.from_dict(apply_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


