# Config1

Configuration specific to the taxonomy type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**taxonomy_type** | **str** | Discriminator identifying this as a hierarchical taxonomy. | [optional] [default to 'hierarchical']
**retriever_id** | **str** | Default retriever to use for all nodes unless overridden per-node. | 
**input_mappings** | [**List[InputMapping]**](InputMapping.md) | Default input mappings for all nodes unless overridden per-node. | 
**source_collection** | [**SourceCollectionInput**](SourceCollectionInput.md) | The single source collection for this flat taxonomy. | 
**inference_strategy** | [**HierarchyInferenceStrategy**](HierarchyInferenceStrategy.md) | Strategy for inferring hierarchy structure from collections. Can be &#39;schema&#39; (overlap-based), &#39;cluster&#39; (clustering-based), or &#39;llm&#39; (AI-based). When set, will infer relationships from inference_collections. | [optional] 
**inference_collections** | **List[str]** | Collection IDs to use for hierarchy inference. The inference_strategy will analyze these collections to discover relationships. Can be combined with hierarchical_nodes for hybrid configuration. | [optional] 
**llm_provider** | **str** | LLM provider to use for hierarchy inference (default openai_chat_v1) | [optional] 
**llm_model** | **str** | LLM model name (e.g., gpt-4o-mini) | [optional] 
**llm_prompt_template** | **str** | Optional prompt template. Variables available: {collection_id}, {collection_name}. | [optional] 
**llm_sample_size** | **int** | Optional number of sample docs to include in prompts (0 &#x3D; disabled). | [optional] [default to 0]
**cluster_ids** | **List[str]** | Cluster IDs to use for CLUSTER inference strategy | [optional] 
**cluster_overlap_threshold** | **float** | Minimum overlap ratio to establish parent-child relationship between clusters | [optional] [default to 0.7]
**hierarchical_nodes** | [**List[HierarchicalNodeInput]**](HierarchicalNodeInput.md) | Explicit node definitions that either: 1) Define the entire hierarchy (when inference_strategy is None), 2) Add additional nodes to an inferred hierarchy, or 3) Override specific relationships in an inferred hierarchy. Supports true hybrid: infer from some collections, manually add others. | [optional] 

## Example

```python
from mixpeek.models.config1 import Config1

# TODO update the JSON string below
json = "{}"
# create an instance of Config1 from a JSON string
config1_instance = Config1.from_json(json)
# print the JSON string representation of the object
print(Config1.to_json())

# convert the object into a dict
config1_dict = config1_instance.to_dict()
# create an instance of Config1 from a dict
config1_from_dict = Config1.from_dict(config1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


