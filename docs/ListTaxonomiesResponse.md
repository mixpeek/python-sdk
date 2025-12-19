# ListTaxonomiesResponse

Response model for listing taxonomies.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[TaxonomyResponse]**](TaxonomyResponse.md) |  | 
**pagination** | **Dict[str, object]** |  | 
**total_count** | **int** |  | 

## Example

```python
from mixpeek.models.list_taxonomies_response import ListTaxonomiesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListTaxonomiesResponse from a JSON string
list_taxonomies_response_instance = ListTaxonomiesResponse.from_json(json)
# print the JSON string representation of the object
print(ListTaxonomiesResponse.to_json())

# convert the object into a dict
list_taxonomies_response_dict = list_taxonomies_response_instance.to_dict()
# create an instance of ListTaxonomiesResponse from a dict
list_taxonomies_response_from_dict = ListTaxonomiesResponse.from_dict(list_taxonomies_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


