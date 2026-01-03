# CloneTaxonomyResponse

Response after cloning a taxonomy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**taxonomy** | [**TaxonomyModelOutput**](TaxonomyModelOutput.md) | Cloned taxonomy configuration with new taxonomy_id. | 
**source_taxonomy_id** | **str** | ID of the source taxonomy that was cloned. | 

## Example

```python
from mixpeek.models.clone_taxonomy_response import CloneTaxonomyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CloneTaxonomyResponse from a JSON string
clone_taxonomy_response_instance = CloneTaxonomyResponse.from_json(json)
# print the JSON string representation of the object
print(CloneTaxonomyResponse.to_json())

# convert the object into a dict
clone_taxonomy_response_dict = clone_taxonomy_response_instance.to_dict()
# create an instance of CloneTaxonomyResponse from a dict
clone_taxonomy_response_from_dict = CloneTaxonomyResponse.from_dict(clone_taxonomy_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


