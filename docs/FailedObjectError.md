# FailedObjectError

Error details for a failed object in a batch.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_index** | **int** | 0-based index of the failed object in the batch request | 
**error** | **str** | Error message describing why the object failed | 
**error_type** | **str** | Type of error (e.g., &#39;ValidationError&#39;, &#39;URLValidationError&#39;) | 

## Example

```python
from mixpeek.models.failed_object_error import FailedObjectError

# TODO update the JSON string below
json = "{}"
# create an instance of FailedObjectError from a JSON string
failed_object_error_instance = FailedObjectError.from_json(json)
# print the JSON string representation of the object
print(FailedObjectError.to_json())

# convert the object into a dict
failed_object_error_dict = failed_object_error_instance.to_dict()
# create an instance of FailedObjectError from a dict
failed_object_error_from_dict = FailedObjectError.from_dict(failed_object_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


