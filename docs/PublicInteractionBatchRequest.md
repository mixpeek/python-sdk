# PublicInteractionBatchRequest

Request to track multiple interactions in batch.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interactions** | [**List[PublicInteractionRequest]**](PublicInteractionRequest.md) | List of interactions to track (max 100 per batch) | 

## Example

```python
from mixpeek.models.public_interaction_batch_request import PublicInteractionBatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PublicInteractionBatchRequest from a JSON string
public_interaction_batch_request_instance = PublicInteractionBatchRequest.from_json(json)
# print the JSON string representation of the object
print(PublicInteractionBatchRequest.to_json())

# convert the object into a dict
public_interaction_batch_request_dict = public_interaction_batch_request_instance.to_dict()
# create an instance of PublicInteractionBatchRequest from a dict
public_interaction_batch_request_from_dict = PublicInteractionBatchRequest.from_dict(public_interaction_batch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


