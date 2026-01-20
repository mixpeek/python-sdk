# InteractionResponse

Response model for a stored interaction.  Extends SearchInteraction with system-assigned fields.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_id** | **str** | ID of the document/feature that was interacted with. REQUIRED. This should be the document_id returned in retriever results. Used to track which specific items users engage with. | 
**interaction_type** | [**List[InteractionType]**](InteractionType.md) | List of interaction types that occurred. REQUIRED. Multiple types can be recorded simultaneously (e.g., VIEW + CLICK + LONG_VIEW for a result the user engaged with). Use the InteractionType enum values. | 
**position** | **int** | Position in search results where interaction occurred (0-indexed). REQUIRED. Critical for Learning to Rank - helps identify position bias. E.g., position&#x3D;0 means first result, position&#x3D;9 means 10th result. Higher engagement at lower positions suggests higher quality. | 
**metadata** | **object** | Additional context about the interaction. NOT REQUIRED. Can include device, duration, viewport info, etc. Use this to enrich interaction data with application-specific context. | [optional] 
**user_id** | **str** | Customer&#39;s authenticated user identifier. NOT REQUIRED. Persists across sessions for long-term tracking. Enables personalization and user-specific metrics. Use your application&#39;s user ID format. | [optional] 
**session_id** | **str** | Temporary identifier for a single search session. NOT REQUIRED. Typically 30min-1hr duration. Tracks anonymous and authenticated users within a session. Use to group related queries and understand search journeys. | [optional] 
**execution_id** | **str** | ID of the retriever execution that generated these results. NOT REQUIRED but HIGHLY RECOMMENDED for training and optimization. Links the interaction back to the exact search query, pipeline configuration, and stage execution that produced the results the user saw. Essential for: fine-tuning embeddings, training rerankers, query understanding, and tracing which pipeline configs produce better user engagement. Retrieve from the retriever execution response and pass to interactions. | [optional] 
**retriever_id** | **str** | ID of the retriever that was executed. NOT REQUIRED but RECOMMENDED for multi-retriever analytics. Enables comparing performance across different retriever configurations. If execution_id is provided, retriever_id can be inferred from the execution record. | [optional] 
**query_snapshot** | **object** | Snapshot of the query input that generated these results. HIGHLY RECOMMENDED for training optimization. Storing the query directly enables 10-100x faster training data extraction by avoiding expensive joins to execution records. Use the same format as retriever query input (e.g., {&#39;text&#39;: &#39;...&#39;, &#39;filters&#39;: {...}}). Essential for: embedding fine-tuning (query-document pairs), query expansion learning, and analyzing which query patterns lead to better engagement. NOT REQUIRED but strongly recommended for production use cases involving model training. | [optional] 
**document_score** | **float** | Initial retrieval score of this document when shown to the user. HIGHLY RECOMMENDED for Learning to Rank (LTR). This is a critical feature for reranker training - helps the model learn how to adjust initial scores based on user engagement. Should match the score from the retriever execution results. NOT REQUIRED but strongly recommended for LTR and reranker training. | [optional] 
**result_set_size** | **int** | Total number of results shown to the user in this search. NOT REQUIRED but useful for context. Helps understand interaction patterns - clicking position 5 of 10 results is different from position 5 of 100 results. Useful for position bias correction and CTR analysis. | [optional] 
**interaction_id** | **str** | Unique identifier for this interaction record. System-assigned UUID. Use this to reference the interaction in subsequent requests. | 
**timestamp** | **str** | ISO 8601 timestamp when the interaction was recorded. System-assigned. Used for time-based analysis, training data recency weighting, and temporal trends in user behavior. | [optional] 

## Example

```python
from mixpeek.models.interaction_response import InteractionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InteractionResponse from a JSON string
interaction_response_instance = InteractionResponse.from_json(json)
# print the JSON string representation of the object
print(InteractionResponse.to_json())

# convert the object into a dict
interaction_response_dict = interaction_response_instance.to_dict()
# create an instance of InteractionResponse from a dict
interaction_response_from_dict = InteractionResponse.from_dict(interaction_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


