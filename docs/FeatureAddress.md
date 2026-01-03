# FeatureAddress

Canonical feature address: mixpeek://{extractor}@{version}/{output}.  The output segment is the inference_name (embedding model identifier), which enables cross-extractor compatibility checking. Two feature URIs with the same inference_name in the output segment produce compatible embeddings that can be compared/fused.  Format examples:     - mixpeek://text_extractor@v1/multilingual_e5_large_instruct_v1     - mixpeek://multimodal_extractor@v1/multilingual_e5_large_instruct_v1  (compatible with above!)     - mixpeek://image_extractor@v1/google_siglip_base_v1  (different model = incompatible)  Short form without the output segment is allowed only if the extractor has a single vector output.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scheme** | **str** |  | [optional] [default to 'mixpeek']
**extractor** | **str** |  | 
**version** | **str** |  | 
**output** | **str** |  | [optional] 

## Example

```python
from mixpeek.models.feature_address import FeatureAddress

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureAddress from a JSON string
feature_address_instance = FeatureAddress.from_json(json)
# print the JSON string representation of the object
print(FeatureAddress.to_json())

# convert the object into a dict
feature_address_dict = feature_address_instance.to_dict()
# create an instance of FeatureAddress from a dict
feature_address_from_dict = FeatureAddress.from_dict(feature_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


