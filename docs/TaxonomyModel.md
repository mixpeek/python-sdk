# TaxonomyModel

Primary Pydantic model representing a taxonomy definition.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**taxonomy_id** | **str** | Unique identifier for the taxonomy | [optional] 
**version** | **int** | Monotonic version number of the taxonomy configuration | [optional] [default to 1]
**taxonomy_name** | **str** | A unique name for the taxonomy within the namespace. | 
**description** | **str** | Optional human-readable description. | [optional] 
**retriever_id** | **str** | Optional taxonomy-level retriever (prefer per-layer). | [optional] 
**input_mappings** | [**List[InputMapping]**](InputMapping.md) | Optional taxonomy-level inputs (prefer per-layer). | [optional] 
**config** | [**Config1**](Config1.md) |  | 
**ready** | **bool** | Whether the taxonomy is ready for use. False for async inference (cluster/LLM) that needs processing. True for flat/explicit hierarchies. | [optional] [default to True]
**created_at** | **datetime** | Creation timestamp for this taxonomy record | [optional] 

## Example

```python
from mixpeek.models.taxonomy_model import TaxonomyModel

# TODO update the JSON string below
json = "{}"
# create an instance of TaxonomyModel from a JSON string
taxonomy_model_instance = TaxonomyModel.from_json(json)
# print the JSON string representation of the object
print(TaxonomyModel.to_json())

# convert the object into a dict
taxonomy_model_dict = taxonomy_model_instance.to_dict()
# create an instance of TaxonomyModel from a dict
taxonomy_model_from_dict = TaxonomyModel.from_dict(taxonomy_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


