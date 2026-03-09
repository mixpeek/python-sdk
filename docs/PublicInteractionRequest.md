# PublicInteractionRequest

Request to track a single interaction from public retriever.  Simplified wrapper around SearchInteraction for public API use.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** | ID of the document that was interacted with (from search results) | 
**interaction_type** | [**List[InteractionType]**](InteractionType.md) | Type(s) of interaction that occurred | 
**position** | **int** | Position in search results (0-indexed) | 
**execution_id** | **str** | ID of the retriever execution that generated these results. HIGHLY RECOMMENDED for analytics. | [optional] 
**query_snapshot** | **Dict[str, object]** | Snapshot of the query that generated these results. HIGHLY RECOMMENDED for training optimization. | [optional] 
**document_score** | **float** | Initial retrieval score of this document | [optional] 
**result_set_size** | **int** | Total number of results shown | [optional] 
**session_id** | **str** | Session identifier for tracking user journey | [optional] 
**metadata** | **Dict[str, object]** | Additional context about the interaction | [optional] 

## Example

```python
from mixpeek.models.public_interaction_request import PublicInteractionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PublicInteractionRequest from a JSON string
public_interaction_request_instance = PublicInteractionRequest.from_json(json)
# print the JSON string representation of the object
print(PublicInteractionRequest.to_json())

# convert the object into a dict
public_interaction_request_dict = public_interaction_request_instance.to_dict()
# create an instance of PublicInteractionRequest from a dict
public_interaction_request_from_dict = PublicInteractionRequest.from_dict(public_interaction_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


