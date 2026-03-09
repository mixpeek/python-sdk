# StageDefsQueryPreprocessing

Configuration for query preprocessing — large file decomposition at query time.  When a query input is a large file (video, PDF, long text), preprocessing decomposes it using the same extractor pipeline that indexed the data, generates N embeddings (one per chunk), runs N parallel searches, and fuses the results into a single ranked list.  This is \"ingestion applied to the query\" — same decomposition and embedding, but vectors are used for search instead of storage.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_uri** | **str** | Feature URI for the extractor pipeline to use for decomposition. If None, inherits from the parent search&#39;s feature_uri. | [optional] 
**params** | **Dict[str, object]** | Extractor-specific parameter overrides. Same params as ingestion: split_method, time_split_interval, chunk_size, chunk_overlap, etc. | [optional] 
**max_chunks** | **int** | Maximum number of chunks to search with. Caps parallel queries and embedding calls to control cost. Chunks are evenly sampled across the file if the extractor produces more than max_chunks. | [optional] [default to 20]
**aggregation** | **str** | Fusion strategy for combining results from N chunk queries. &#39;rrf&#39;: Reciprocal Rank Fusion (balanced, recommended). &#39;max&#39;: Keep highest score per document (best for &#39;find this exact moment&#39;). &#39;avg&#39;: Average scores (best for &#39;find similar overall content&#39;). | [optional] [default to 'rrf']
**dedup_field** | **str** | Optional payload field to deduplicate results by. E.g., &#39;_internal.document_id&#39; to collapse chunks from the same parent document. | [optional] 

## Example

```python
from mixpeek.models.stage_defs_query_preprocessing import StageDefsQueryPreprocessing

# TODO update the JSON string below
json = "{}"
# create an instance of StageDefsQueryPreprocessing from a JSON string
stage_defs_query_preprocessing_instance = StageDefsQueryPreprocessing.from_json(json)
# print the JSON string representation of the object
print(StageDefsQueryPreprocessing.to_json())

# convert the object into a dict
stage_defs_query_preprocessing_dict = stage_defs_query_preprocessing_instance.to_dict()
# create an instance of StageDefsQueryPreprocessing from a dict
stage_defs_query_preprocessing_from_dict = StageDefsQueryPreprocessing.from_dict(stage_defs_query_preprocessing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


