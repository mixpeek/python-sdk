# PipelineComparison

Statistical comparison between a candidate and baseline pipeline.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**candidate_retriever_id** | **str** | ID of the candidate pipeline. | 
**ndcg_delta** | **Dict[str, float]** | Change in NDCG at each K (positive &#x3D; candidate better). | 
**recall_delta** | **Dict[str, float]** | Change in recall at each K (positive &#x3D; candidate better). | 
**latency_delta_ms** | **float** | Change in mean latency (positive &#x3D; candidate slower). | 
**p_value** | **float** | Statistical significance of the difference (paired t-test). | [optional] 
**confidence_interval** | **List[object]** | 95% confidence interval for NDCG@10 delta. | [optional] 
**taxonomy_wins** | **List[str]** | Taxonomy nodes where candidate significantly outperforms. | [optional] 
**taxonomy_losses** | **List[str]** | Taxonomy nodes where candidate significantly underperforms. | [optional] 

## Example

```python
from mixpeek.models.pipeline_comparison import PipelineComparison

# TODO update the JSON string below
json = "{}"
# create an instance of PipelineComparison from a JSON string
pipeline_comparison_instance = PipelineComparison.from_json(json)
# print the JSON string representation of the object
print(PipelineComparison.to_json())

# convert the object into a dict
pipeline_comparison_dict = pipeline_comparison_instance.to_dict()
# create an instance of PipelineComparison from a dict
pipeline_comparison_from_dict = PipelineComparison.from_dict(pipeline_comparison_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


