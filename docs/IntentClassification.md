# IntentClassification

Result of intent detection analysis.  This model represents the agent's understanding of whether the user wants to: - Execute queries on existing data (execution mode) - Create new resources/infrastructure (setup mode) - Or if the request is ambiguous and needs clarification  Attributes:     intent: The detected intent (\"execution\", \"setup\", or \"ambiguous\")     confidence: Confidence score 0.0-1.0     reasoning: Explanation of why this intent was detected     suitable_collections: Existing collections that might fulfill the request     recommended_action: What the agent should do next     clarification_needed: Whether to ask user for clarification     clarification_options: Options to present if clarification needed     keywords_found: Keywords that influenced the classification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**intent** | **str** | Detected intent: &#39;execution&#39;, &#39;setup&#39;, or &#39;ambiguous&#39; | 
**confidence** | **float** | Confidence in classification | 
**reasoning** | **str** | Why this intent was detected | 
**suitable_collections** | [**List[SuitableCollection]**](SuitableCollection.md) | Existing collections that might help | [optional] 
**recommended_action** | **str** | Next action to take (e.g., &#39;setup_pipeline&#39;, &#39;execute_retriever&#39;) | 
**clarification_needed** | **bool** | Whether to ask user for clarification | 
**clarification_options** | [**List[ClarificationOption]**](ClarificationOption.md) | Options for user if clarification needed | [optional] 
**keywords_found** | **Dict[str, List[str]]** | Keywords found (setup_keywords, execution_keywords, neutral_keywords) | [optional] 

## Example

```python
from mixpeek.models.intent_classification import IntentClassification

# TODO update the JSON string below
json = "{}"
# create an instance of IntentClassification from a JSON string
intent_classification_instance = IntentClassification.from_json(json)
# print the JSON string representation of the object
print(IntentClassification.to_json())

# convert the object into a dict
intent_classification_dict = intent_classification_instance.to_dict()
# create an instance of IntentClassification from a dict
intent_classification_from_dict = IntentClassification.from_dict(intent_classification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


