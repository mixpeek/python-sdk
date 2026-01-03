# CreateNamespaceRequest

Request schema for creating a new namespace.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**namespace_name** | **str** | Name of the namespace to create | 
**description** | **str** | Description of the namespace | [optional] 
**feature_extractors** | [**List[BaseFeatureExtractorModelInput]**](BaseFeatureExtractorModelInput.md) | List of feature extractors to use. At least one feature extractor must be provided. Optional &#39;params&#39; can be specified for extractors with configurable settings (e.g., model selection) that affect vector dimensions. These params are locked at namespace creation time. | 
**payload_indexes** | [**List[PayloadIndexConfigInput]**](PayloadIndexConfigInput.md) | Optional list of custom payload index configurations. Indexes required by selected feature extractors will be added automatically. | [optional] 
**auto_create_indexes** | **bool** | Enable automatic creation of Qdrant payload indexes based on filter usage patterns. When enabled, the system tracks which fields are most frequently filtered (&gt;100 queries/24h) and automatically creates indexes to improve query performance. Background task runs every 6 hours. Expected performance improvement: 50-90% latency reduction for filtered queries. | [optional] [default to False]

## Example

```python
from mixpeek.models.create_namespace_request import CreateNamespaceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNamespaceRequest from a JSON string
create_namespace_request_instance = CreateNamespaceRequest.from_json(json)
# print the JSON string representation of the object
print(CreateNamespaceRequest.to_json())

# convert the object into a dict
create_namespace_request_dict = create_namespace_request_instance.to_dict()
# create an instance of CreateNamespaceRequest from a dict
create_namespace_request_from_dict = CreateNamespaceRequest.from_dict(create_namespace_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


