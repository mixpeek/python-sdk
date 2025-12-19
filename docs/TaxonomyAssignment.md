# TaxonomyAssignment

Represents a taxonomy node assignment for a document.  This is a lightweight reference to a taxonomy/node with optional path/label/score metadata; full node details live in the taxonomy module.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**taxonomy_id** | **str** | ID of the taxonomy | 
**node_id** | **str** | Matched taxonomy node ID | 
**path** | **List[str]** | Optional hierarchical path labels | [optional] 
**label** | **str** | Optional human-readable label | [optional] 
**score** | **float** | Optional similarity score | [optional] 

## Example

```python
from mixpeek.models.taxonomy_assignment import TaxonomyAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of TaxonomyAssignment from a JSON string
taxonomy_assignment_instance = TaxonomyAssignment.from_json(json)
# print the JSON string representation of the object
print(TaxonomyAssignment.to_json())

# convert the object into a dict
taxonomy_assignment_dict = taxonomy_assignment_instance.to_dict()
# create an instance of TaxonomyAssignment from a dict
taxonomy_assignment_from_dict = TaxonomyAssignment.from_dict(taxonomy_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


