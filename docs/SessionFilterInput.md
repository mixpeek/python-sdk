# SessionFilterInput

Criteria for selecting historical sessions to replay.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retriever_ids** | **List[str]** | Filter to sessions from these retrievers. | [optional] 
**taxonomy_node_ids** | **List[str]** | Filter to sessions with these taxonomy classifications. | [optional] 
**time_range** | [**TimeRangeInput**](TimeRangeInput.md) | Filter to sessions within this time window. | [optional] 
**min_interactions** | **int** | Minimum number of user interactions required. | [optional] [default to 1]
**interaction_types** | **List[str]** | Filter to sessions with these interaction types (e.g., [&#39;click&#39;, &#39;purchase&#39;]). | [optional] 
**sample_strategy** | **str** | How to sample sessions: &#39;random&#39;, &#39;recent&#39;, or &#39;stratified&#39;. | [optional] [default to 'random']
**interaction_weights** | [**InteractionWeights**](InteractionWeights.md) | Custom weights for interaction types when computing relevance scores. | [optional] 

## Example

```python
from mixpeek.models.session_filter_input import SessionFilterInput

# TODO update the JSON string below
json = "{}"
# create an instance of SessionFilterInput from a JSON string
session_filter_input_instance = SessionFilterInput.from_json(json)
# print the JSON string representation of the object
print(SessionFilterInput.to_json())

# convert the object into a dict
session_filter_input_dict = session_filter_input_instance.to_dict()
# create an instance of SessionFilterInput from a dict
session_filter_input_from_dict = SessionFilterInput.from_dict(session_filter_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


