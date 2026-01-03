# SubmitFeedbackResponse

Response for feedback submission.  Attributes:     session_id: Session identifier     message_id: Message that received feedback     rating: The feedback rating submitted     stored: Whether the exchange was stored to memory     recorded_at: Timestamp when feedback was recorded  Example:     ```python     response = SubmitFeedbackResponse(         session_id=\"ses_abc123\",         message_id=\"msg_xyz789\",         rating=\"positive\",         stored=True,         recorded_at=datetime.utcnow()     )     ```

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **str** | Session identifier | 
**message_id** | **str** | Message identifier | 
**rating** | **str** | Feedback rating submitted | 
**stored** | **bool** | Whether exchange was stored to memory | 
**recorded_at** | **datetime** | Feedback timestamp | 

## Example

```python
from mixpeek.models.submit_feedback_response import SubmitFeedbackResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SubmitFeedbackResponse from a JSON string
submit_feedback_response_instance = SubmitFeedbackResponse.from_json(json)
# print the JSON string representation of the object
print(SubmitFeedbackResponse.to_json())

# convert the object into a dict
submit_feedback_response_dict = submit_feedback_response_instance.to_dict()
# create an instance of SubmitFeedbackResponse from a dict
submit_feedback_response_from_dict = SubmitFeedbackResponse.from_dict(submit_feedback_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


