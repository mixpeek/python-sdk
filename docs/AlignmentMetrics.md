# AlignmentMetrics

Metrics measuring how well a ranking aligns with observed user behavior.  These metrics compare a candidate pipeline's ranking against ground truth derived from actual user interactions (clicks, purchases, etc.).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ndcg_at_k** | **Dict[str, float]** | Normalized Discounted Cumulative Gain at various K values. | 
**mean_rank_clicked** | **float** | Average position of clicked items in the new ranking. | 
**mean_rank_purchased** | **float** | Average position of purchased items (if any purchases observed). | [optional] 
**recall_at_k** | **Dict[str, float]** | Fraction of interacted items found in top K results. | 
**avg_position_delta** | **float** | Average change in position for interacted items (negative &#x3D; promoted). | 
**items_promoted** | **int** | Number of interacted items moved to higher positions. | 
**items_demoted** | **int** | Number of interacted items moved to lower positions. | 
**sessions_improved** | **int** | Sessions where candidate outperformed baseline. | 
**sessions_degraded** | **int** | Sessions where candidate underperformed baseline. | 
**sessions_neutral** | **int** | Sessions with no significant difference. | 

## Example

```python
from mixpeek.models.alignment_metrics import AlignmentMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of AlignmentMetrics from a JSON string
alignment_metrics_instance = AlignmentMetrics.from_json(json)
# print the JSON string representation of the object
print(AlignmentMetrics.to_json())

# convert the object into a dict
alignment_metrics_dict = alignment_metrics_instance.to_dict()
# create an instance of AlignmentMetrics from a dict
alignment_metrics_from_dict = AlignmentMetrics.from_dict(alignment_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


