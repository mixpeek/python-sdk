# CreateCollectionRequest

Request model for creating a new collection.  Collections process data from buckets or other collections using feature extractors.  CRITICAL: To use input_mappings in feature_extractors: 1. Your source bucket MUST have a bucket_schema defined 2. The input_mappings reference fields from that bucket_schema 3. The system validates that mapped fields exist in the source schema  Example workflow: 1. Create bucket with schema: { \"properties\": { \"image\": {\"type\": \"image\"}, \"metadata\": {...} } } 2. Upload objects conforming to that schema 3. Create collection with input_mappings: { \"image\": \"image\", \"text\": \"metadata.title\" } 4. The system validates \"image\" and \"metadata.title\" exist in the bucket schema  Without a bucket_schema, input_mappings will fail with: \"The source field 'X' does not exist in the source schema.\"

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_name** | **str** | Name of the collection to create | 
**description** | **str** | Description of the collection | [optional] 
**source** | [**SourceConfig**](SourceConfig.md) | Source configuration (bucket or collection) for this collection | 
**input_schema** | [**BucketSchemaInput**](BucketSchemaInput.md) | Input schema for the collection. If not provided, inferred from source bucket&#39;s bucket_schema or source collection&#39;s output_schema. REQUIRED for input_mappings to work - defines what fields can be mapped to feature extractors. | [optional] 
**feature_extractors** | [**List[FeatureExtractorConfigInput]**](FeatureExtractorConfigInput.md) | Feature extractors to apply. Use input_mappings in each extractor to map source schema fields to extractor inputs. Example: {&#39;image&#39;: &#39;product_image&#39;, &#39;text&#39;: &#39;metadata.title&#39;} | [optional] 
**enabled** | **bool** | Whether the collection is enabled | [optional] [default to True]
**metadata** | **Dict[str, object]** | Additional metadata for the collection | [optional] 

## Example

```python
from mixpeek.models.create_collection_request import CreateCollectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCollectionRequest from a JSON string
create_collection_request_instance = CreateCollectionRequest.from_json(json)
# print the JSON string representation of the object
print(CreateCollectionRequest.to_json())

# convert the object into a dict
create_collection_request_dict = create_collection_request_instance.to_dict()
# create an instance of CreateCollectionRequest from a dict
create_collection_request_from_dict = CreateCollectionRequest.from_dict(create_collection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


