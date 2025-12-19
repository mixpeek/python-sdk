# ListTaxonomiesRequest

Request model to list taxonomies.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search** | **str** | Search term to filter taxonomies by name | [optional] 
**filters** | [**LogicalOperatorInput**](LogicalOperatorInput.md) | Filters to apply to the taxonomy list | [optional] 
**sort** | [**SortOption**](SortOption.md) | Sort configuration for the taxonomy list | [optional] 
**case_sensitive** | **bool** | If True, filters and search will be case-sensitive | [optional] [default to False]

## Example

```python
from mixpeek.models.list_taxonomies_request import ListTaxonomiesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListTaxonomiesRequest from a JSON string
list_taxonomies_request_instance = ListTaxonomiesRequest.from_json(json)
# print the JSON string representation of the object
print(ListTaxonomiesRequest.to_json())

# convert the object into a dict
list_taxonomies_request_dict = list_taxonomies_request_instance.to_dict()
# create an instance of ListTaxonomiesRequest from a dict
list_taxonomies_request_from_dict = ListTaxonomiesRequest.from_dict(list_taxonomies_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


