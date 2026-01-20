# CostsInfo

Credit cost information for a feature extractor.  Describes the pricing tier and standardized cost rates for using this extractor. Rates are defined using CostUnit types that align with extractor input types.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tier** | **int** | Cost tier (1-4): 1&#x3D;SIMPLE, 2&#x3D;MODERATE, 3&#x3D;COMPLEX, 4&#x3D;PREMIUM | 
**tier_label** | **str** | Human-readable tier label (SIMPLE, MODERATE, COMPLEX, PREMIUM) | 
**rates** | [**List[CostRate]**](CostRate.md) | List of cost rates for different input types this extractor processes | 

## Example

```python
from mixpeek.models.costs_info import CostsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CostsInfo from a JSON string
costs_info_instance = CostsInfo.from_json(json)
# print the JSON string representation of the object
print(CostsInfo.to_json())

# convert the object into a dict
costs_info_dict = costs_info_instance.to_dict()
# create an instance of CostsInfo from a dict
costs_info_from_dict = CostsInfo.from_dict(costs_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


