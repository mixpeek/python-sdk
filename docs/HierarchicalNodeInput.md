# HierarchicalNodeInput

A node in a hierarchical taxonomy (explicit representation).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_id** | **str** | The ID of the collection representing this node in the hierarchy. | 
**parent_collection_id** | **str** | The ID of the parent collection in the hierarchy (&#x60;&#x60;None&#x60;&#x60; for root nodes). | [optional] 
**label** | **str** | Optional human-readable label for the node | [optional] 
**summary** | **str** | Optional summary describing the node | [optional] 
**keywords** | **List[str]** | Optional keywords associated with the node | [optional] 
**retriever_id** | **str** | Optional per-node retriever. If omitted, taxonomy-level &#x60;retriever_id&#x60; (if provided) is used. | [optional] 
**enrichment_fields** | [**List[EnrichmentField]**](EnrichmentField.md) | Optional field-level enrichment behaviour for this specific node. | [optional] 
**input_mappings** | [**List[InputMapping]**](InputMapping.md) | Optional override of the taxonomy-level input_mappings when this node is matched. | [optional] 

## Example

```python
from mixpeek.models.hierarchical_node_input import HierarchicalNodeInput

# TODO update the JSON string below
json = "{}"
# create an instance of HierarchicalNodeInput from a JSON string
hierarchical_node_input_instance = HierarchicalNodeInput.from_json(json)
# print the JSON string representation of the object
print(HierarchicalNodeInput.to_json())

# convert the object into a dict
hierarchical_node_input_dict = hierarchical_node_input_instance.to_dict()
# create an instance of HierarchicalNodeInput from a dict
hierarchical_node_input_from_dict = HierarchicalNodeInput.from_dict(hierarchical_node_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


