# GroundTruthQuery

Single query with ground truth relevance labels.  This represents one query in an evaluation dataset, along with the list of documents that are considered relevant for that query.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query_id** | **str** | Unique identifier for this query within the dataset | 
**query_input** | **Dict[str, object]** | Query input in the same format as retriever execution (e.g., {&#39;text&#39;: &#39;...&#39;}) | 
**relevant_documents** | **List[str]** | List of feature_ids that are relevant for this query | 
**relevance_scores** | **Dict[str, int]** | Optional graded relevance scores (doc_id -&gt; score, 0-5 where 5 is most relevant). Used for NDCG calculation. | [optional] 

## Example

```python
from mixpeek.models.ground_truth_query import GroundTruthQuery

# TODO update the JSON string below
json = "{}"
# create an instance of GroundTruthQuery from a JSON string
ground_truth_query_instance = GroundTruthQuery.from_json(json)
# print the JSON string representation of the object
print(GroundTruthQuery.to_json())

# convert the object into a dict
ground_truth_query_dict = ground_truth_query_instance.to_dict()
# create an instance of GroundTruthQuery from a dict
ground_truth_query_from_dict = GroundTruthQuery.from_dict(ground_truth_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


