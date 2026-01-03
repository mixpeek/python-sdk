# SubmitFeedbackRequest

Request payload for submitting feedback on a message.  Attributes:     message_id: The assistant message ID to provide feedback for     rating: Feedback rating (positive or negative)     feedback_text: Optional additional feedback text  Example:     ```python     request = SubmitFeedbackRequest(         message_id=\"msg_abc123\",         rating=\"positive\",         feedback_text=\"This was very helpful!\"     )     ```

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **str** | Assistant message ID (REQUIRED) | 
**rating** | **str** | Feedback rating: &#39;positive&#39; or &#39;negative&#39; (REQUIRED) | 
**feedback_text** | **str** | Additional feedback text (OPTIONAL) | [optional] 

## Example

```python
from mixpeek.models.submit_feedback_request import SubmitFeedbackRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SubmitFeedbackRequest from a JSON string
submit_feedback_request_instance = SubmitFeedbackRequest.from_json(json)
# print the JSON string representation of the object
print(SubmitFeedbackRequest.to_json())

# convert the object into a dict
submit_feedback_request_dict = submit_feedback_request_instance.to_dict()
# create an instance of SubmitFeedbackRequest from a dict
submit_feedback_request_from_dict = SubmitFeedbackRequest.from_dict(submit_feedback_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


