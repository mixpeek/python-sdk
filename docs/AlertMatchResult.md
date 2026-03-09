# AlertMatchResult

A single match from alert execution.  Represents a document that matched the retriever's query criteria.  Attributes:     document_id: ID of the matched document     asset_id: Asset ID of the matched document     score: Similarity/relevance score     matched_features: Optional features that caused the match     metadata: Optional metadata from the matched document

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** | ID of the matched document | 
**asset_id** | **str** | Asset ID of the matched document | [optional] 
**score** | **float** | Similarity/relevance score | 
**matched_features** | **Dict[str, object]** | Features that caused the match | [optional] 
**metadata** | **Dict[str, object]** | Metadata from the matched document | [optional] 

## Example

```python
from mixpeek.models.alert_match_result import AlertMatchResult

# TODO update the JSON string below
json = "{}"
# create an instance of AlertMatchResult from a JSON string
alert_match_result_instance = AlertMatchResult.from_json(json)
# print the JSON string representation of the object
print(AlertMatchResult.to_json())

# convert the object into a dict
alert_match_result_dict = alert_match_result_instance.to_dict()
# create an instance of AlertMatchResult from a dict
alert_match_result_from_dict = AlertMatchResult.from_dict(alert_match_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


