# StageParamsSample

Configuration for document sampling.  **Stage Category**: REDUCE  **Transformation**: N documents → M documents (where M ≤ N)  **Purpose**: Sample a subset of documents using random or stratified sampling. Operates on in-memory results from previous stages.  **When to Use**:     - A/B testing different pipeline configurations     - Reducing result set for expensive downstream stages     - Exploration and discovery features     - Ensuring proportional representation across categories     - Creating reproducible experiments with seeded sampling  **When NOT to Use**:     - When you need all results (just use previous stage output)     - For ranking/reordering (use SORT stages)     - For filtering by criteria (use FILTER stages)  **Sampling Strategies**:     - `random`: Uniform random sampling     - `stratified`: Proportional sampling across a field's values     - `reservoir`: Reservoir sampling (for streaming scenarios)  **Common Pipeline Position**: feature_search → (expensive stages) → sample  Examples:     Basic random sampling:         ```json         {             \"count\": 10,             \"strategy\": \"random\"         }         ```      Stratified sampling by category:         ```json         {             \"count\": 20,             \"strategy\": \"stratified\",             \"stratify_by\": \"metadata.category\"         }         ```      Reproducible sampling with seed:         ```json         {             \"count\": 50,             \"strategy\": \"random\",             \"seed\": 42         }         ```      Preserve top results, sample rest:         ```json         {             \"count\": 10,             \"strategy\": \"random\",             \"preserve_top_k\": 3         }         ```

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | REQUIRED. Number of documents to sample. If count &gt; available documents, returns all documents. | [optional] [default to 10]
**strategy** | **str** | OPTIONAL. Sampling strategy: - &#39;random&#39;: Uniform random sampling (default) - &#39;stratified&#39;: Proportional sampling across stratify_by field values - &#39;reservoir&#39;: Reservoir sampling (memory-efficient for large sets) | [optional] [default to 'random']
**stratify_by** | **str** | OPTIONAL. Field to stratify on (required when strategy&#x3D;&#39;stratified&#39;). Samples proportionally from each unique value of this field. Supports dot notation for nested fields. | [optional] [default to 'null']
**min_per_stratum** | **int** | OPTIONAL. Minimum documents per stratum (stratified mode). Ensures each category gets at least this many documents. | [optional] [default to 1]
**seed** | **int** | OPTIONAL. Random seed for reproducible sampling. Same seed + same input &#x3D; same output. Leave None for non-deterministic sampling. | [optional] [default to null]
**preserve_top_k** | **int** | OPTIONAL. Always keep the top K documents by score, sample from remainder. Useful when you want to guarantee top results are included. Default: 0 (no preservation, sample from all). | [optional] [default to 0]

## Example

```python
from mixpeek.models.stage_params_sample import StageParamsSample

# TODO update the JSON string below
json = "{}"
# create an instance of StageParamsSample from a JSON string
stage_params_sample_instance = StageParamsSample.from_json(json)
# print the JSON string representation of the object
print(StageParamsSample.to_json())

# convert the object into a dict
stage_params_sample_dict = stage_params_sample_instance.to_dict()
# create an instance of StageParamsSample from a dict
stage_params_sample_from_dict = StageParamsSample.from_dict(stage_params_sample_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


