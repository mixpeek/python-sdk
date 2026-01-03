# ClonedResourceSummary

Summary of cloned resources.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collections** | **int** | Collections cloned | [optional] [default to 0]
**retrievers** | **int** | Retrievers cloned | [optional] [default to 0]
**taxonomies** | **int** | Taxonomies cloned | [optional] [default to 0]
**buckets** | **int** | Buckets cloned | [optional] [default to 0]
**objects** | **int** | Objects cloned | [optional] [default to 0]
**points** | **int** | Vector points cloned | [optional] [default to 0]

## Example

```python
from mixpeek.models.cloned_resource_summary import ClonedResourceSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ClonedResourceSummary from a JSON string
cloned_resource_summary_instance = ClonedResourceSummary.from_json(json)
# print the JSON string representation of the object
print(ClonedResourceSummary.to_json())

# convert the object into a dict
cloned_resource_summary_dict = cloned_resource_summary_instance.to_dict()
# create an instance of ClonedResourceSummary from a dict
cloned_resource_summary_from_dict = ClonedResourceSummary.from_dict(cloned_resource_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


