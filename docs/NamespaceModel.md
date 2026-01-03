# NamespaceModel

Namespace model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**namespace_id** | **str** | Unique identifier for the namespace | [optional] 
**namespace_name** | **str** | Name of the namespace | 
**infrastructure** | [**NamespaceInfrastructure**](NamespaceInfrastructure.md) | Infrastructure configuration for the namespace (Ray, Qdrant). | [optional] 
**cluster_id** | **str** | Infrastructure cluster ID for this namespace (Enterprise only). When set, this namespace uses dedicated Anyscale/Ray + Qdrant cluster. If None, uses shared infrastructure or organization-level infrastructure. Format: iclstr_xxx | [optional] 
**description** | **str** | Description of the namespace | [optional] 
**feature_extractors** | [**List[BaseFeatureExtractorModelOutput]**](BaseFeatureExtractorModelOutput.md) | List of feature extractors configured for this namespace | [optional] 
**payload_indexes** | [**List[PayloadIndexConfigOutput]**](PayloadIndexConfigOutput.md) | Custom payload indexes configured for this namespace | [optional] 
**document_count** | **int** | Total number of documents in this namespace (from Qdrant collection) | [optional] 
**bucket_count** | **int** | Total number of buckets in this namespace | [optional] 
**collection_count** | **int** | Total number of collections in this namespace | [optional] 
**object_count** | **int** | Total number of objects across all buckets in this namespace | [optional] 
**auto_create_indexes** | **bool** | Enable automatic creation of Qdrant payload indexes based on filter usage patterns. When enabled, the system tracks which fields are most frequently filtered (&gt;100 queries/24h) and automatically creates indexes to improve query performance. Background task runs every 6 hours. Expected performance improvement: 50-90% latency reduction for filtered queries. | [optional] [default to False]
**vector_inference_map** | **Dict[str, str]** | Mapping of vector index names to inference service names. Built at namespace creation based on extractor configurations. Used by feature search to determine correct inference service for queries. Example: {&#39;image_extractor_v1_embedding&#39;: &#39;google_siglip_base_v1&#39;} | [optional] 
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


