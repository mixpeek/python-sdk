# NamespaceModel

Namespace model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**namespace_id** | **str** | Unique identifier for the namespace | [optional] 
**namespace_name** | **str** | Name of the namespace | 
**description** | **str** | Description of the namespace | [optional] 
**feature_extractors** | [**List[BaseFeatureExtractorModelOutput]**](BaseFeatureExtractorModelOutput.md) | List of feature extractors configured for this namespace | [optional] 
**payload_indexes** | [**List[PayloadIndexConfigOutput]**](PayloadIndexConfigOutput.md) | Custom payload indexes configured for this namespace | [optional] 
**created_at** | **datetime** | When the namespace was created | [optional] 
**updated_at** | **datetime** | When the namespace was last updated | [optional] 

## Example

```python
from mixpeek.models.namespace_model import NamespaceModel

# TODO update the JSON string below
json = "{}"
# create an instance of NamespaceModel from a JSON string
namespace_model_instance = NamespaceModel.from_json(json)
# print the JSON string representation of the object
print(NamespaceModel.to_json())

# convert the object into a dict
namespace_model_dict = namespace_model_instance.to_dict()
# create an instance of NamespaceModel from a dict
namespace_model_from_dict = NamespaceModel.from_dict(namespace_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


