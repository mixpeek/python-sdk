# DiversityFeatureConfig

Configuration for a single feature used in multi-feature diversity computation.  When using multi-feature diversity mode, you can specify multiple embedding spaces and weight their contribution to the overall diversity score.  Example:     Combine text and image embeddings with different weights:     ```python     features = [         DiversityFeatureConfig(             feature_uri=\"mixpeek://text_extractor@v1/multilingual_e5_large_instruct_v1\",             weight=0.6         ),         DiversityFeatureConfig(             feature_uri=\"mixpeek://clip@v1/image_embedding\",             weight=0.4         )     ]     ```

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_uri** | **str** | REQUIRED. Feature URI specifying which embedding to use for diversity. Format: &#39;mixpeek://extractor@version/output&#39;. The embedding must exist on documents from the previous stage. Use state.context to find available embeddings from feature_search. | 
**weight** | **float** | OPTIONAL. Weight for this feature&#39;s contribution to diversity score. Weights across all features are normalized to sum to 1.0. Higher weight &#x3D; more influence on diversity computation. | [optional] [default to 1.0]

## Example

```python
from mixpeek.models.diversity_feature_config import DiversityFeatureConfig

# TODO update the JSON string below
json = "{}"
# create an instance of DiversityFeatureConfig from a JSON string
diversity_feature_config_instance = DiversityFeatureConfig.from_json(json)
# print the JSON string representation of the object
print(DiversityFeatureConfig.to_json())

# convert the object into a dict
diversity_feature_config_dict = diversity_feature_config_instance.to_dict()
# create an instance of DiversityFeatureConfig from a dict
diversity_feature_config_from_dict = DiversityFeatureConfig.from_dict(diversity_feature_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


