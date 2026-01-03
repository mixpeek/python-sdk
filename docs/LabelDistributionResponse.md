# LabelDistributionResponse

Taxonomy label distribution response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**taxonomy_id** | **str** |  | 
**labels** | [**List[LabelMetric]**](LabelMetric.md) |  | 
**total_labels** | **int** |  | 

## Example

```python
from mixpeek.models.label_distribution_response import LabelDistributionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LabelDistributionResponse from a JSON string
label_distribution_response_instance = LabelDistributionResponse.from_json(json)
# print the JSON string representation of the object
print(LabelDistributionResponse.to_json())

# convert the object into a dict
label_distribution_response_dict = label_distribution_response_instance.to_dict()
# create an instance of LabelDistributionResponse from a dict
label_distribution_response_from_dict = LabelDistributionResponse.from_dict(label_distribution_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


