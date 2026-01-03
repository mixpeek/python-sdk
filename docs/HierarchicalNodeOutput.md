# HierarchicalNodeOutput

A node in a hierarchical taxonomy representing one level in the tree structure.  Each node represents a collection containing documents at a specific hierarchy level. Nodes form parent-child relationships to create multi-level taxonomies with property inheritance. When a document matches a child node, it inherits all properties from parent nodes up to the root.  Use Cases:     - Define organizational hierarchies: employees → managers → executives     - Create product categorizations: products → electronics → phones → smartphones     - Build classification trees: industries → technology → software     - Implement face recognition hierarchies: people → employees → team members     - Enable property inheritance: child nodes get all parent properties  Hierarchy Behavior:     - Root nodes: parent_collection_id = None (top of hierarchy)     - Child nodes: parent_collection_id references parent node's collection_id     - Property inheritance: Children inherit all parent enrichment_fields     - Path construction: Creates path array from root to leaf     - Multi-level matching: Documents matched at deepest applicable level  Configuration:     - Per-node retrievers: Override taxonomy-level retriever for specific nodes     - Per-node enrichment: Override which fields to enrich at each level     - Per-node input mappings: Customize retriever inputs per hierarchy level     - Labels/summaries: Human-readable metadata for UI display  Related Models:     - HierarchicalTaxonomyConfig: Contains list of hierarchical nodes     - TaxonomyAssignment: Result of matching documents to nodes     - EnrichmentField: Specifies which fields to enrich from node  Requirements:     - collection_id: REQUIRED - must reference an existing collection     - parent_collection_id: REQUIRED for non-root nodes (None for root)     - All other fields: OPTIONAL with inheritance from taxonomy-level config

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_id** | **str** | REQUIRED. Collection ID representing this node in the hierarchy. Must reference an existing collection containing documents for this hierarchy level. Format: &#39;col_&#39; prefix followed by alphanumeric/underscore characters. Used to: Match documents against this level, identify node in path, store enrichment data. Example: &#39;col_executives&#39; for executive level, &#39;col_products_phones&#39; for phones category. | 
**parent_collection_id** | **str** | OPTIONAL. Collection ID of the parent node in the hierarchy. When None: This is a root node (top of hierarchy). When set: References parent node&#39;s collection_id, creating parent-child relationship. Format: Same as collection_id (&#39;col_&#39; prefix). Used to: Build hierarchy tree, determine inheritance order, construct path arrays. Example: &#39;col_managers&#39; is parent of &#39;col_executives&#39;, &#39;col_products&#39; is parent of &#39;col_electronics&#39;. Validation: Must reference a valid collection_id from another node in same taxonomy. | [optional] 
**label** | **str** | OPTIONAL. Human-readable display name for this hierarchy node. Used in UI, visualizations, and taxonomy assignment results. NOT REQUIRED - When None: collection name or auto-generated label may be used. Format: Free text, typically title case, 2-50 characters. Examples: &#39;Executive Leadership&#39;, &#39;Mobile Phones&#39;, &#39;Engineering Team&#39;. Can be LLM-generated or manually specified during taxonomy creation. | [optional] 
**summary** | **str** | OPTIONAL. Brief description of this hierarchy level and its contents. Used for: Documentation, UI tooltips, understanding hierarchy structure. NOT REQUIRED - When None: no summary available for this node. Format: Free text, typically 1-3 sentences, up to 500 characters. Can be LLM-generated or manually provided. | [optional] 
**keywords** | **List[str]** | OPTIONAL. Keywords or tags describing this hierarchy level. Used for: Search, filtering, categorization, LLM understanding. NOT REQUIRED - When None: no keywords defined for this node. Format: List of strings, typically 3-10 keywords per node. Can be LLM-generated from collection contents or manually specified. | [optional] 
**retriever_id** | **str** | OPTIONAL. Retriever to use for matching documents at this hierarchy level. When None: Uses taxonomy-level retriever_id (inheritance from parent config). When set: Overrides taxonomy-level retriever for this specific node. Format: &#39;ret_&#39; prefix followed by alphanumeric characters. Use for: Specialized matching at certain levels (e.g., face recognition for employees, semantic search for products). Must reference an existing RetrieverModel. | [optional] 
**enrichment_fields** | [**List[EnrichmentField]**](EnrichmentField.md) | OPTIONAL. Fields to enrich into documents when they match this hierarchy level. Specifies which properties from node collection to copy to matched documents. When None: No field-level enrichment (only taxonomy assignment recorded). Format: List of EnrichmentField objects with field_path and merge_mode. Inheritance: Child nodes inherit all parent enrichment_fields plus their own. Example: executives node adds &#39;executive_level&#39; on top of inherited &#39;employee_id&#39;, &#39;department&#39;. | [optional] 
**input_mappings** | [**List[InputMapping]**](InputMapping.md) | OPTIONAL. Custom input mappings for the retriever at this hierarchy level. Specifies how to construct retriever inputs from document features. When None: Uses taxonomy-level input_mappings (inheritance). When set: Overrides taxonomy-level mappings for this specific node. Format: List of InputMapping objects specifying input_key, source_type, path. Use for: Different matching strategies at different levels (e.g., face at employee level, text at department level). | [optional] 

## Example

```python
from mixpeek.models.hierarchical_node_output import HierarchicalNodeOutput

# TODO update the JSON string below
json = "{}"
# create an instance of HierarchicalNodeOutput from a JSON string
hierarchical_node_output_instance = HierarchicalNodeOutput.from_json(json)
# print the JSON string representation of the object
print(HierarchicalNodeOutput.to_json())

# convert the object into a dict
hierarchical_node_output_dict = hierarchical_node_output_instance.to_dict()
# create an instance of HierarchicalNodeOutput from a dict
hierarchical_node_output_from_dict = HierarchicalNodeOutput.from_dict(hierarchical_node_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


