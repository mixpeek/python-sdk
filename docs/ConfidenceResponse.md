# ConfidenceResponse

Taxonomy confidence distribution response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**taxonomy_id** | **str** |  | 
**distribution** | [**List[ConfidenceDistribution]**](ConfidenceDistribution.md) |  | 
**avg_confidence** | **float** |  | 
**low_confidence_count** | **int** | Count of assignments below 0.5 confidence | 

## Example

```python
from mixpeek.models.confidence_response import ConfidenceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConfidenceResponse from a JSON string
confidence_response_instance = ConfidenceResponse.from_json(json)
# print the JSON string representation of the object
print(ConfidenceResponse.to_json())

# convert the object into a dict
confidence_response_dict = confidence_response_instance.to_dict()
# create an instance of ConfidenceResponse from a dict
confidence_response_from_dict = ConfidenceResponse.from_dict(confidence_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


