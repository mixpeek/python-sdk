# ResourceFilter

Filters for selective resource migration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_ids** | **List[str]** | Specific collection IDs to migrate | [optional] 
**taxonomy_ids** | **List[str]** | Specific taxonomy IDs to migrate | [optional] 
**cluster_ids** | **List[str]** | Specific cluster IDs to migrate | [optional] 
**retriever_ids** | **List[str]** | Specific retriever IDs to migrate | [optional] 
**date_range** | **Dict[str, str]** | Date range filter (after, before) | [optional] 
**auto_include_dependencies** | **bool** | Automatically include required dependencies | [optional] [default to True]

## Example

```python
from mixpeek.models.resource_filter import ResourceFilter

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceFilter from a JSON string
resource_filter_instance = ResourceFilter.from_json(json)
# print the JSON string representation of the object
print(ResourceFilter.to_json())

# convert the object into a dict
resource_filter_dict = resource_filter_instance.to_dict()
# create an instance of ResourceFilter from a dict
resource_filter_from_dict = ResourceFilter.from_dict(resource_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


