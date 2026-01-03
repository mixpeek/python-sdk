# TaxonomyModelOutput

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
**config** | [**Config2**](Config2.md) |  | 
**ready** | **bool** | Whether the taxonomy is ready for use. False for async inference (cluster/LLM) that needs processing. True for flat/explicit hierarchies. | [optional] [default to True]
**created_at** | **datetime** | Creation timestamp for this taxonomy record | [optional] 
**metadata** | **Dict[str, object]** | Additional user-defined metadata for the taxonomy | [optional] 

## Example

```python
from mixpeek.models.taxonomy_model_output import TaxonomyModelOutput

# TODO update the JSON string below
json = "{}"
# create an instance of TaxonomyModelOutput from a JSON string
taxonomy_model_output_instance = TaxonomyModelOutput.from_json(json)
# print the JSON string representation of the object
print(TaxonomyModelOutput.to_json())

# convert the object into a dict
taxonomy_model_output_dict = taxonomy_model_output_instance.to_dict()
# create an instance of TaxonomyModelOutput from a dict
taxonomy_model_output_from_dict = TaxonomyModelOutput.from_dict(taxonomy_model_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


