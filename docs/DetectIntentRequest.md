# DetectIntentRequest

Request to detect intent from user input.  Attributes:     user_request: The user's natural language request to analyze     include_collection_analysis: Whether to analyze existing collections

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_request** | **str** | User&#39;s natural language request | 
**include_collection_analysis** | **bool** | Whether to check existing collections | [optional] [default to True]

## Example

```python
from mixpeek.models.detect_intent_request import DetectIntentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DetectIntentRequest from a JSON string
detect_intent_request_instance = DetectIntentRequest.from_json(json)
# print the JSON string representation of the object
print(DetectIntentRequest.to_json())

# convert the object into a dict
detect_intent_request_dict = detect_intent_request_instance.to_dict()
# create an instance of DetectIntentRequest from a dict
detect_intent_request_from_dict = DetectIntentRequest.from_dict(detect_intent_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


