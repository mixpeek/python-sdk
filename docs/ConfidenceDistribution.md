# ConfidenceDistribution

Confidence score distribution bucket.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confidence_range** | **str** | Confidence range (e.g., &#39;0.8-0.9&#39;) | 
**count** | **int** |  | 
**percentage** | **float** |  | 

## Example

```python
from mixpeek.models.confidence_distribution import ConfidenceDistribution

# TODO update the JSON string below
json = "{}"
# create an instance of ConfidenceDistribution from a JSON string
confidence_distribution_instance = ConfidenceDistribution.from_json(json)
# print the JSON string representation of the object
print(ConfidenceDistribution.to_json())

# convert the object into a dict
confidence_distribution_dict = confidence_distribution_instance.to_dict()
# create an instance of ConfidenceDistribution from a dict
confidence_distribution_from_dict = ConfidenceDistribution.from_dict(confidence_distribution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


