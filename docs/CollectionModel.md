# CollectionModel

Collection model with single feature extractor and deterministic schema.  Collections are processing pipelines that transform source data (from buckets or other collections) into searchable documents with features. Each collection represents ONE transformation step with ONE feature extractor.  Key Concepts:     - Input Schema: What goes IN (from bucket or upstream collection)     - Feature Extractor: The transformation logic (text embedding, video processing, etc.)     - Field Passthrough: User-selected source fields to include in output     - Output Schema: What comes OUT (field_passthrough + extractor outputs)  Architecture (Task 9):     - ONE feature extractor per collection (not a list)     - output_schema computed at creation time (deterministic, no waiting)     - Multiple extractors = multiple collections     - Enables clean decomposition trees and clear lineage  Use Cases:     - Create embeddings from text/images/video     - Build multi-tier pipelines (bucket → frames → scenes)     - Apply feature extraction with metadata passthrough     - Organize data processing into clear stages  Requirements:     - collection_name: REQUIRED, unique within namespace     - source: REQUIRED, bucket or collection source     - feature_extractor: REQUIRED, single extractor configuration     - input_schema: Auto-computed from source (bucket_schema or upstream output_schema)     - output_schema: Auto-computed at creation (field_passthrough + extractor output)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_id** | **str** | NOT REQUIRED (auto-generated). Unique identifier for this collection. Used for: API paths, document queries, pipeline references. Format: &#39;col_&#39; prefix + 10 random alphanumeric characters. Stable after creation - use for all collection references. | [optional] 
**collection_name** | **str** | REQUIRED. Human-readable name for the collection. Must be unique within the namespace. Used for: Display, lookups (can query by name or ID), organization. Format: Alphanumeric with underscores/hyphens, 3-100 characters. Examples: &#39;product_embeddings&#39;, &#39;video_frames&#39;, &#39;customer_documents&#39;. | 
**description** | **str** | NOT REQUIRED. Human-readable description of the collection&#39;s purpose. Use for: Documentation, team communication, UI display. Common pattern: Describe what the collection contains and what processing is applied. | [optional] 
**input_schema** | [**BucketSchemaOutput**](BucketSchemaOutput.md) | REQUIRED (auto-computed from source). Input schema defining fields available to the feature extractor. Source: bucket.bucket_schema (if source.type&#x3D;&#39;bucket&#39;) OR upstream_collection.output_schema (if source.type&#x3D;&#39;collection&#39;). Determines: Which fields can be used in input_mappings and field_passthrough. This is the &#39;left side&#39; of the transformation - what data goes IN. Format: BucketSchema with properties dict. Use for: Validating input_mappings, configuring field_passthrough. | 
**output_schema** | [**BucketSchemaOutput**](BucketSchemaOutput.md) | REQUIRED (auto-computed at creation). Output schema defining fields in final documents. Computed as: field_passthrough fields + extractor output fields (deterministic). Known IMMEDIATELY when collection is created - no waiting for documents! This is the &#39;right side&#39; of the transformation - what data comes OUT. Use for: Understanding document structure, building queries, schema validation. Example: {title (passthrough), embedding (extractor output)} &#x3D; output_schema. | 
**feature_extractor** | [**SharedCollectionFeaturesExtractorsModelsFeatureExtractorConfigOutput**](SharedCollectionFeaturesExtractorsModelsFeatureExtractorConfigOutput.md) | REQUIRED. Single feature extractor configuration for this collection. Defines: extractor name/version, input_mappings, field_passthrough, parameters. Task 9 change: ONE extractor per collection (previously supported multiple). For multiple extractors: Create multiple collections and use collection-to-collection pipelines. Use field_passthrough to include additional source fields beyond extractor outputs. | 
**source** | [**SourceConfigOutput**](SourceConfigOutput.md) | REQUIRED. Source configuration defining where data comes from. Type &#39;bucket&#39;: Process objects from one or more buckets (tier 1). Type &#39;collection&#39;: Process documents from upstream collection(s) (tier 2+). For multi-bucket sources, all buckets must have compatible schemas. For multi-collection sources, all collections must have compatible schemas. Determines input_schema and enables decomposition trees. | 
**source_bucket_schemas** | [**Dict[str, BucketSchemaOutput]**](BucketSchemaOutput.md) | NOT REQUIRED (auto-computed). Snapshot of bucket schemas at collection creation. Only populated for multi-bucket collections (source.type&#x3D;&#39;bucket&#39; with multiple bucket_ids). Key: bucket_id, Value: BucketSchema at time of collection creation. Used for: Schema compatibility validation, document lineage, debugging. Schema snapshot is immutable - bucket schema changes after collection creation do not affect this. Single-bucket collections may omit this field (schema in input_schema is sufficient). | [optional] 
**source_lineage** | [**List[SingleLineageEntry]**](SingleLineageEntry.md) | NOT REQUIRED (auto-computed). Lineage chain showing complete processing history. Each entry contains: source_config, feature_extractor, output_schema for one tier. Length indicates processing depth (1 &#x3D; tier 1, 2 &#x3D; tier 2, etc.). Use for: Understanding multi-tier pipelines, visualizing decomposition trees. | [optional] 
**vector_indexes** | **List[object]** | NOT REQUIRED (auto-computed from extractor). Vector indexes for semantic search. Populated from feature_extractor.required_vector_indexes. Defines: Which embeddings are indexed, dimensions, distance metrics. Use for: Understanding search capabilities, debugging vector queries. | [optional] 
**payload_indexes** | **List[object]** | NOT REQUIRED (auto-computed from extractor + namespace). Payload indexes for filtering. Enables efficient filtering on metadata fields, timestamps, IDs. Populated from: extractor requirements + namespace defaults. Use for: Understanding which fields support fast filtering. | [optional] 
**enabled** | **bool** | NOT REQUIRED (defaults to True). Whether the collection accepts new documents. False: Collection exists but won&#39;t process new objects. True: Active and processing. Use for: Temporarily disabling collections without deletion. | [optional] [default to True]
**metadata** | **Dict[str, object]** | NOT REQUIRED. Additional user-defined metadata for the collection. Arbitrary key-value pairs for custom organization, tracking, configuration. Not used by the platform - purely for user purposes. Common uses: team ownership, project tags, deployment environment. | [optional] 
**created_at** | **datetime** | Timestamp when the collection was created. Automatically set by the system when the collection is first saved to the database. | [optional] 
**updated_at** | **datetime** | Timestamp when the collection was last updated. Automatically updated by the system whenever the collection is modified. | [optional] 
**document_count** | **int** | Number of documents currently in the collection. Automatically maintained by the system as documents are added or removed. Used for: Sorting, filtering, and pagination in list endpoints. Updated during batch processing and document operations. | [optional] [default to 0]
**schema_version** | **int** | Version number for the output_schema. Increments automatically when schema is updated via document sampling. Used to track schema evolution and trigger downstream collection schema updates. | [optional] [default to 1]
**last_schema_sync** | **datetime** | Timestamp of last automatic schema sync from document sampling. Used to debounce schema updates (prevents thrashing). | [optional] 
**schema_sync_enabled** | **bool** | Whether automatic schema discovery and sync is enabled for this collection. When True, schema is periodically updated by sampling documents. When False, schema remains fixed at creation time. | [optional] [default to True]
**taxonomy_applications** | [**List[TaxonomyApplicationConfigOutput]**](TaxonomyApplicationConfigOutput.md) | NOT REQUIRED. List of taxonomies to apply to documents in this collection. Each entry specifies: taxonomy_id, optional target_collection_id, optional filters. Enrichments are materialized (persisted to documents) during ingestion. Empty/null if no taxonomies attached. Use for: Categorization, hierarchical classification. | [optional] 
**cluster_applications** | [**List[ClusterApplicationConfig]**](ClusterApplicationConfig.md) | NOT REQUIRED. List of clusters to automatically execute when batch processing completes. Each entry specifies: cluster_id, auto_execute_on_batch, min_document_threshold, cooldown_seconds. Clusters enrich source documents with cluster assignments (cluster_id, cluster_label, etc.). Empty/null if no clusters attached. Use for: Segmentation, grouping, pattern discovery. | [optional] 

## Example

```python
from mixpeek.models.collection_model import CollectionModel

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionModel from a JSON string
collection_model_instance = CollectionModel.from_json(json)
# print the JSON string representation of the object
print(CollectionModel.to_json())

# convert the object into a dict
collection_model_dict = collection_model_instance.to_dict()
# create an instance of CollectionModel from a dict
collection_model_from_dict = CollectionModel.from_dict(collection_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


