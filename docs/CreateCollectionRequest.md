# CreateCollectionRequest

Request model for creating a new collection.  Collections process data from buckets or other collections using a single feature extractor.  KEY ARCHITECTURAL CHANGE: Each collection has EXACTLY ONE feature extractor. - Use field_passthrough to include additional source fields in output documents - Multiple extractors = multiple collections - This simplifies processing and makes output schema deterministic  CRITICAL: To use input_mappings: 1. Your source bucket MUST have a bucket_schema defined 2. The input_mappings reference fields from that bucket_schema 3. The system validates that mapped fields exist in the source schema  Example workflow: 1. Create bucket with schema: { \"properties\": { \"image\": {\"type\": \"image\"}, \"title\": {\"type\": \"string\"} } } 2. Upload objects conforming to that schema 3. Create collection with:    - input_mappings: { \"image\": \"image\" }    - field_passthrough: [{\"source_path\": \"title\"}] 4. Output documents will have both extractor outputs AND passthrough fields  Schema Computation: - output_schema is computed IMMEDIATELY when collection is created - output_schema = field_passthrough fields + extractor output fields - No waiting for documents to be processed!

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_name** | **str** | Name of the collection to create | 
**description** | **str** | Description of the collection | [optional] 
**source** | [**SourceConfigInput**](SourceConfigInput.md) | Source configuration (bucket or collection) for this collection | 
**input_schema** | [**BucketSchemaInput**](BucketSchemaInput.md) | Input schema for the collection. If not provided, inferred from source bucket&#39;s bucket_schema or source collection&#39;s output_schema. REQUIRED for input_mappings to work - defines what fields can be mapped to feature extractors. | [optional] 
**feature_extractor** | [**SharedCollectionFeaturesExtractorsModelsFeatureExtractorConfigInput**](SharedCollectionFeaturesExtractorsModelsFeatureExtractorConfigInput.md) | Single feature extractor for this collection. Use field_passthrough within the extractor config to include additional source fields. For multiple extractors, create multiple collections and use collection-to-collection pipelines. | 
**enabled** | **bool** | Whether the collection is enabled | [optional] [default to True]
**metadata** | **Dict[str, object]** | Additional metadata for the collection | [optional] 
**taxonomy_applications** | [**List[TaxonomyApplicationConfigInput]**](TaxonomyApplicationConfigInput.md) | Optional taxonomy applications to automatically enrich documents in this collection. Each taxonomy will classify/enrich documents based on configured retriever matches. | [optional] 
**cluster_applications** | [**List[ClusterApplicationConfig]**](ClusterApplicationConfig.md) | Optional cluster applications to automatically execute when batch processing completes. Each cluster enriches documents with cluster assignments (cluster_id, cluster_label, etc.). | [optional] 
**alert_applications** | [**List[AlertApplicationConfigInput]**](AlertApplicationConfigInput.md) | Optional alert applications to automatically execute when documents are ingested. Each alert runs a retriever against new documents and sends notifications if matches are found. Supports both ON_INGEST (triggered per batch) and SCHEDULED (periodic) execution modes. | [optional] 

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


