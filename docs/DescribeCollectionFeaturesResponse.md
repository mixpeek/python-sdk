# DescribeCollectionFeaturesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**features** | [**List[CollectionFeatureDescriptor]**](CollectionFeatureDescriptor.md) | Feature extractors and fields enabled on this collection | 

## Example

```python
from mixpeek.models.describe_collection_features_response import DescribeCollectionFeaturesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DescribeCollectionFeaturesResponse from a JSON string
describe_collection_features_response_instance = DescribeCollectionFeaturesResponse.from_json(json)
# print the JSON string representation of the object
print(DescribeCollectionFeaturesResponse.to_json())

# convert the object into a dict
describe_collection_features_response_dict = describe_collection_features_response_instance.to_dict()
# create an instance of DescribeCollectionFeaturesResponse from a dict
describe_collection_features_response_from_dict = DescribeCollectionFeaturesResponse.from_dict(describe_collection_features_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


