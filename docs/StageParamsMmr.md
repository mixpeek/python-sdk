# StageParamsMmr

Configuration for MMR (Maximal Marginal Relevance) result diversification.  **Stage Category**: SORT  **Transformation**: N documents → N documents (reordered for diversity)  **Purpose**: Reorders search results to balance relevance with diversity, preventing result sets dominated by near-duplicate or highly similar content. Particularly valuable for multimodal search where visual/semantic similarity can lead to repetitive results.  **When to Use**:     - After feature_search when results may contain near-duplicates     - When users expect variety in search results     - For recommendation systems needing diverse suggestions     - When different facets of a query should be represented  **When NOT to Use**:     - When exact relevance ranking is critical (use sort_relevance)     - For small result sets (<5 documents) where diversity matters less     - When duplicates have already been removed via group_by  **Three Diversity Modes** (mutually exclusive):  | Mode | Config Field | Description | |------|--------------|-------------| | Single Feature | `diversity_feature_uri` | Diversity in one embedding space | | Multi-Feature | `diversity_features` | Weighted fusion across spaces | | Attribute-Based | `diversity_fields` | Diversify by metadata values |  **Mode Selection Logic**:     1. If `diversity_feature_uri` is set → Single Feature mode     2. If `diversity_features` is set → Multi-Feature mode     3. If `diversity_fields` is set → Attribute-Based mode     4. If none set → Auto-detect from previous feature_search stage  **Common Pipeline Position**: feature_search → mmr → (optional rerank)  Examples:     Single feature diversity (simplest):         ```json         {             \"lambda_\": 0.7,             \"top_k\": 25,             \"diversity_feature_uri\": \"mixpeek://clip@v1/image_embedding\"         }         ```      Multi-feature diversity (multimodal):         ```json         {             \"lambda_\": 0.6,             \"top_k\": 20,             \"diversity_features\": [                 {\"feature_uri\": \"mixpeek://text@v1/embedding\", \"weight\": 0.5},                 {\"feature_uri\": \"mixpeek://clip@v1/embedding\", \"weight\": 0.5}             ]         }         ```      Attribute-based diversity (no embeddings):         ```json         {             \"lambda_\": 0.5,             \"top_k\": 30,             \"diversity_fields\": [\"metadata.category\", \"metadata.source\"]         }         ```

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_lambda** | **float** | OPTIONAL. Balance between relevance and diversity (default: 0.7). Higher values favor relevance, lower values favor diversity.   Guidelines: - 1.0: Pure relevance (no diversity, equivalent to no MMR) - 0.7-0.8: Slight diversity while maintaining relevance (recommended) - 0.5: Balanced relevance and diversity - 0.3-0.4: High diversity, may sacrifice some relevance - 0.0: Maximum diversity (ignores relevance scores) | [optional] [default to 0.7]
**top_k** | **int** | OPTIONAL. Number of documents to return after MMR reordering (default: 25). MMR processes all input documents but returns only top_k. Set to match your UI&#39;s result count for optimal diversity. | [optional] [default to 25]
**diversity_feature_uri** | **str** | OPTIONAL. Single embedding feature URI for diversity computation. Use this for simple cases where one embedding space captures similarity.   If not specified and no other mode is set, auto-detects from the previous feature_search stage&#39;s feature_uri.   Format: &#39;mixpeek://extractor@version/output&#39; | [optional] [default to 'null']
**diversity_features** | [**List[DiversityFeatureConfig]**](DiversityFeatureConfig.md) | OPTIONAL. Multiple embedding features for weighted diversity fusion. Use this for multimodal content where similarity should consider multiple embedding spaces (e.g., text + image + audio).   Diversity scores from each feature are combined using weights. Weights are normalized to sum to 1.0. | [optional] [default to null]
**diversity_fields** | **List[str]** | OPTIONAL. Metadata fields to use for attribute-based diversity. No embeddings required - uses field value matching.   Documents with the same field values are considered similar. Useful for categorical diversity (one per category, source, type).   Dot notation supported for nested fields. | [optional] [default to null]
**diversity_field_weights** | **Dict[str, float]** | OPTIONAL. Weights for each diversity field (for attribute-based mode). If not specified, all fields are weighted equally. Keys must match field paths in diversity_fields. | [optional] 
**score_field** | **str** | OPTIONAL. Document field containing relevance score from previous stage. Used as the &#39;relevance&#39; component in MMR formula. | [optional] [default to 'score']
**mmr_score_field** | **str** | OPTIONAL. Field path to store the computed MMR score. Useful for debugging and understanding ranking decisions. | [optional] [default to 'scores.mmr']
**similarity_metric** | **str** | OPTIONAL. Similarity metric for embedding comparison. Cosine is recommended for normalized embeddings (most common). | [optional] [default to 'cosine']

## Example

```python
from mixpeek.models.stage_params_mmr import StageParamsMmr

# TODO update the JSON string below
json = "{}"
# create an instance of StageParamsMmr from a JSON string
stage_params_mmr_instance = StageParamsMmr.from_json(json)
# print the JSON string representation of the object
print(StageParamsMmr.to_json())

# convert the object into a dict
stage_params_mmr_dict = stage_params_mmr_instance.to_dict()
# create an instance of StageParamsMmr from a dict
stage_params_mmr_from_dict = StageParamsMmr.from_dict(stage_params_mmr_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


