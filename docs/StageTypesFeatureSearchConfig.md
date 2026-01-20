# StageTypesFeatureSearchConfig

Configuration for a single feature search within the feature_filter stage.  Each feature search specifies: - Which feature URI to search (embedding index) - What input to search with (text, URL, or base64) - Search parameters (top_k, score threshold) - Optional weight for fusion  Multiple feature searches are combined using the stage's fusion strategy.  Examples:     Text semantic search:         ```json         {             \"feature_uri\": \"mixpeek://text_extractor@v1/multilingual_e5_large_instruct_v1\",             \"query\": {\"input_mode\": \"text\", \"value\": \"Hello world!\"},             \"top_k\": 100         }         ```      Image visual search with URL (auto-detected):         ```json         {             \"feature_uri\": \"mixpeek://clip_extractor@v1/image_embedding\",             \"query\": {\"input_mode\": \"content\", \"value\": \"{{INPUT.image_url}}\"},             \"top_k\": 50         }         ```      Multimodal search with template and weight:         ```json         {             \"feature_uri\": \"mixpeek://multimodal_extractor@v1/embedding\",             \"query\": {\"input_mode\": \"text\", \"value\": \"{{INPUT.query}}\"},             \"top_k\": 100,             \"weight\": 0.7         }         ```

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_uri** | **str** | REQUIRED. Feature URI specifying which embedding index to search. Format: &#39;mixpeek://extractor@version/output&#39; or &#39;namespace://collection/feature&#39;. Must reference a valid dense vector index in the collection. The feature must exist and be indexed for all documents in the collection. | 
**query** | [**Query**](Query.md) |  | 
**top_k** | **int** | OPTIONAL. Number of results to fetch for this specific feature search. Defaults to 100. This is the per-feature top_k, independent of the final_top_k parameter. Higher values: More comprehensive but slower. Lower values: Faster but may miss relevant results. Qdrant will fetch this many results before fusion. | [optional] [default to 100]
**min_score** | **float** | OPTIONAL. Minimum similarity score threshold for this feature search. NOT REQUIRED - if not specified, no score filtering is applied. Filters out results below this threshold BEFORE fusion. Typical values: 0.5-0.8 depending on model and use case. Lower threshold: More recall, less precision. Higher threshold: More precision, less recall. | [optional] 
**weight** | **float** | OPTIONAL. Weight for this feature search when using &#39;weighted&#39; fusion. Defaults to 1.0 (equal weight). Ignored for &#39;rrf&#39; and &#39;max&#39; fusion strategies. Sum of all feature weights should typically equal 1.0 for normalized scores. Higher weight: More influence on final ranking. Example: Text&#x3D;0.7, Image&#x3D;0.3 for text-heavy search. | [optional] [default to 1.0]
**on_empty** | [**OnEmptyBehavior**](OnEmptyBehavior.md) | OPTIONAL. Behavior when input is empty after template resolution. Defaults to &#39;error&#39; (fail if input missing).   ┌─────────┬────────────────────────────────────────────────────────────┐ │ Value   │ Behavior                                                   │ ├─────────┼────────────────────────────────────────────────────────────┤ │ error   │ Fail with error (input is required) - DEFAULT              │ │ skip    │ Exclude from fusion (let other searches drive results)     │ │ random  │ Use random vector (always return results)                  │ └─────────┴────────────────────────────────────────────────────────────┘   &#39;error&#39; (default): Strict mode - fail fast if input is missing. Use when input is required and missing input indicates a bug.   &#39;skip&#39;: Graceful degradation - exclude this search from fusion. Use for multi-modal search where user may provide text OR image OR both. If all searches skip (all inputs empty), returns error.   &#39;random&#39;: Always return results - use random vector as fallback. Use for single-feature optional search where you always want results. | [optional] 
**collection_identifiers** | **List[str]** | OPTIONAL. Collection identifiers to search for this specific feature search. Can be collection IDs or names. Enables per-search collection targeting for hybrid/multi-feature searches.   Fallback Priority (most specific wins): 1. This field (per-search targeting) - most specific 2. Stage-level collection_identifiers 3. Retriever-level collection_identifiers   Use Cases: - Hybrid search where different features exist in different collections - Text embeddings in col_products, image embeddings in col_media - Fine-grained collection targeting per feature URI   Note: All collections (across all searches) must be declared in the retriever&#39;s collection_identifiers at creation time for validation. | [optional] 

## Example

```python
from mixpeek.models.stage_types_feature_search_config import StageTypesFeatureSearchConfig

# TODO update the JSON string below
json = "{}"
# create an instance of StageTypesFeatureSearchConfig from a JSON string
stage_types_feature_search_config_instance = StageTypesFeatureSearchConfig.from_json(json)
# print the JSON string representation of the object
print(StageTypesFeatureSearchConfig.to_json())

# convert the object into a dict
stage_types_feature_search_config_dict = stage_types_feature_search_config_instance.to_dict()
# create an instance of StageTypesFeatureSearchConfig from a dict
stage_types_feature_search_config_from_dict = StageTypesFeatureSearchConfig.from_dict(stage_types_feature_search_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


