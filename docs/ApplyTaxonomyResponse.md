# ApplyTaxonomyResponse

Response from applying taxonomy to collection.  Returns statistics about the materialization process.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** | ID of the Ray task executing the materialization | 
**status** | **str** | Status of the materialization task | 
**collection_id** | **str** | Collection ID where taxonomy is being applied | 
**taxonomy_id** | **str** | Taxonomy ID being applied | 
**estimated_documents** | **int** | Estimated number of documents to process (if available) | [optional] 

## Example

```python
from mixpeek.models.apply_taxonomy_response import ApplyTaxonomyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyTaxonomyResponse from a JSON string
apply_taxonomy_response_instance = ApplyTaxonomyResponse.from_json(json)
# print the JSON string representation of the object
print(ApplyTaxonomyResponse.to_json())

# convert the object into a dict
apply_taxonomy_response_dict = apply_taxonomy_response_instance.to_dict()
# create an instance of ApplyTaxonomyResponse from a dict
apply_taxonomy_response_from_dict = ApplyTaxonomyResponse.from_dict(apply_taxonomy_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


