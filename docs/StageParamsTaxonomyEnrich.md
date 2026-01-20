# StageParamsTaxonomyEnrich

Configuration for enriching documents with taxonomy assignments.  **Stage Category**: APPLY (1-1 or 1-N depending on configuration)  **Transformation**:     - 1-1 mode (top_k=1): N documents → N documents (same count, expanded schema)     - 1-N mode (top_k>1): N documents → N*M documents (outer join/tagging)  **Purpose**: Applies each document to a taxonomy search, matching against predefined taxonomy nodes using vector similarity. Can operate as 1-1 enrichment (single best match) or 1-N expansion (multiple matching tags).  **When to Use**:     - After FILTER/SORT to classify and tag retrieved documents     - For automatic content categorization (topics, genres, entities)     - When you have labeled reference data (people, products, categories)     - For face recognition (matching faces against enrolled identities)     - To apply hierarchical categorization (parent/child relationships)     - For entity linking (matching content to knowledge base entities)     - **1-1 mode** (top_k=1): Single best match enrichment     - **1-N mode** (top_k>1): Multi-tag expansion (document multiplication)  **When NOT to Use**:     - For initial document retrieval from collections (use FILTER: hybrid_search)     - For removing documents (use FILTER stages)     - For reordering results (use SORT stages)     - For general field-based JOINs (use document_enrich instead)     - When you don't have a predefined taxonomy collection  **Operational Behavior**:     - Applies each input document to taxonomy vector search     - Performs vector similarity search against taxonomy collection (Qdrant)     - Document count: N in → N out (top_k=1) or N*M out (top_k>1)     - Expands or maintains schema depending on mode     - Moderate performance (vector similarity searches per document)     - Supports conditional enrichment (via `when` parameter for cost savings)  **Common Pipeline Position**: FILTER → SORT → APPLY (this stage)  **Conditional Enrichment**: Supports `when` parameter to only enrich documents matching specific criteria. Critical for:     - Cost savings (vector searches are compute-intensive)     - Selective enrichment based on document properties     - Applying different taxonomies to different document types  Requirements:     - taxonomy_id: REQUIRED - ID of the taxonomy to use for enrichment     - fields: OPTIONAL, which taxonomy fields to merge into documents     - top_k: OPTIONAL, max taxonomy matches per document (default 3)     - min_score: OPTIONAL, minimum similarity threshold (default 0.0)     - when: OPTIONAL, condition for selective enrichment  Use Cases:     - Face recognition: Match detected faces to employee directory     - Content classification: Tag articles with topic categories     - Product categorization: Assign products to taxonomy of categories     - Entity linking: Link mentions to knowledge base entities     - Brand detection: Identify brand logos in images  Examples:     Basic taxonomy enrichment:         ```json         {             \"taxonomy_id\": \"tax_abc123\",             \"top_k\": 3         }         ```      Conditional enrichment (only enrich if category=product):         ```json         {             \"taxonomy_id\": \"tax_product_classifier\",             \"top_k\": 3,             \"when\": {                 \"AND\": [                     {\"field\": \"metadata.category\", \"operator\": \"eq\", \"value\": \"product\"},                     {\"field\": \"metadata.has_image\", \"operator\": \"eq\", \"value\": true}                 ]             }         }         ```

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**taxonomy_id** | **str** | ID of the taxonomy to use for enrichment. The taxonomy&#39;s configured input_mappings determine which vector field from source documents to use for similarity matching. NOTE: You must replace the default placeholder with your actual taxonomy ID. | [optional] [default to '{{TAXONOMY_ID}}']
**fields** | [**List[EnrichmentField]**](EnrichmentField.md) | Fields from the taxonomy node to merge into the document. | [optional] 
**top_k** | **int** | Maximum taxonomy assignments to attach per document. | [optional] [default to 3]
**min_score** | **float** | Minimum similarity score required to keep an assignment. | [optional] [default to 0.0]
**when** | [**LogicalOperator**](LogicalOperator.md) | OPTIONAL. Conditional filter that documents must satisfy to be enriched. Uses LogicalOperator (AND/OR/NOT) for complex boolean logic, or simple field/operator/value for single conditions. Documents NOT matching this condition will SKIP enrichment (pass-through unchanged). Useful for cost savings (only enrich relevant documents) and conditional processing. When NOT specified, ALL documents are enriched unconditionally.   Simple condition example: {\&quot;field\&quot;: \&quot;metadata.category\&quot;, \&quot;operator\&quot;: \&quot;eq\&quot;, \&quot;value\&quot;: \&quot;product\&quot;} Boolean AND example: {\&quot;AND\&quot;: [{\&quot;field\&quot;: \&quot;x\&quot;, \&quot;operator\&quot;: \&quot;eq\&quot;, \&quot;value\&quot;: \&quot;y\&quot;}, ...]} Boolean OR example: {\&quot;OR\&quot;: [{\&quot;field\&quot;: \&quot;x\&quot;, \&quot;operator\&quot;: \&quot;eq\&quot;, \&quot;value\&quot;: \&quot;y\&quot;}, ...]}  | [optional] 

## Example

```python
from mixpeek.models.stage_params_taxonomy_enrich import StageParamsTaxonomyEnrich

# TODO update the JSON string below
json = "{}"
# create an instance of StageParamsTaxonomyEnrich from a JSON string
stage_params_taxonomy_enrich_instance = StageParamsTaxonomyEnrich.from_json(json)
# print the JSON string representation of the object
print(StageParamsTaxonomyEnrich.to_json())

# convert the object into a dict
stage_params_taxonomy_enrich_dict = stage_params_taxonomy_enrich_instance.to_dict()
# create an instance of StageParamsTaxonomyEnrich from a dict
stage_params_taxonomy_enrich_from_dict = StageParamsTaxonomyEnrich.from_dict(stage_params_taxonomy_enrich_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


