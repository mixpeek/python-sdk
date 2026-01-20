# StageParamsRerank

Configuration for reranking documents using cross-encoder models.  Reranking refines search results by computing query-document relevance scores using cross-encoder models (e.g., BGE reranker). More accurate than vector similarity but slower, so typically used on top-K results.  Common Pipeline:     feature_filter (retrieve 100) → rerank (refine to 10) → sort_relevance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inference_name** | **str** | Reranking inference service name. Must be a reranking service. Use GET /engine/inference to list available rerankers. | [optional] [default to 'baai_bge_reranker_v2_m3']
**query** | **str** | Query text to compare against documents. Supports template variables: {{INPUT.query}}, etc. | [optional] [default to '{{INPUT.query}}']
**document_field** | **str** | Document field path containing text to rerank against | [optional] [default to 'content']
**top_k** | **int** | Number of top documents to keep after reranking. If None, returns all documents in reranked order. | [optional] [default to null]
**score_field** | **str** | Document field path to store reranking scores | [optional] [default to 'scores.rerank']
**batch_size** | **int** | Batch size for reranking inference calls | [optional] [default to 32]

## Example

```python
from mixpeek.models.stage_params_rerank import StageParamsRerank

# TODO update the JSON string below
json = "{}"
# create an instance of StageParamsRerank from a JSON string
stage_params_rerank_instance = StageParamsRerank.from_json(json)
# print the JSON string representation of the object
print(StageParamsRerank.to_json())

# convert the object into a dict
stage_params_rerank_dict = stage_params_rerank_instance.to_dict()
# create an instance of StageParamsRerank from a dict
stage_params_rerank_from_dict = StageParamsRerank.from_dict(stage_params_rerank_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


