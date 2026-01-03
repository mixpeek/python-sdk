# SourceConfigInput

Configuration for collection source (bucket(s) or collection).  Collections can process data from two types of sources:  1. **Bucket Source**: Process raw objects from one or more buckets (first-stage processing)    - Use this to create your initial collections from uploaded data    - Can specify multiple buckets to consolidate data from different sources    - All buckets must have compatible schemas (validated at creation)    - Example: Videos from multiple regions → Frame extraction collection  2. **Collection Source**: Process documents from another collection (decomposition trees)    - Use this to create multi-stage processing pipelines    - Example: Frames collection → Scene detection collection  Multi-Bucket Requirements: - All buckets must have compatible schemas (same fields, types, and required status) - Schema compatibility is validated when the collection is created - Documents track which specific bucket they came from via root_bucket_id - Useful for consolidating data from multiple regions, teams, or environments  The source determines: - What data the feature extractor receives as input - The input_schema available for input_mappings and field_passthrough - The lineage tracking in output documents  Examples:     Single bucket: {\"type\": \"bucket\", \"bucket_ids\": [\"bkt_products\"]}     Multi-bucket: {\"type\": \"bucket\", \"bucket_ids\": [\"bkt_us\", \"bkt_eu\", \"bkt_asia\"]}     Collection: {\"type\": \"collection\", \"collection_id\": \"col_frames\"}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**SourceType**](SourceType.md) | REQUIRED. Type of source for this collection. &#39;bucket&#39;: Process objects from one or more buckets (first-stage processing). &#39;collection&#39;: Process documents from another collection (downstream processing). Use &#39;bucket&#39; for initial data ingestion, &#39;collection&#39; for decomposition trees. | 
**bucket_ids** | **List[str]** | List of bucket IDs when type&#x3D;&#39;bucket&#39;. REQUIRED when type&#x3D;&#39;bucket&#39;. NOT ALLOWED when type&#x3D;&#39;collection&#39;. Can specify one or more buckets to process. Single bucket: Use array with one element [&#39;bkt_id&#39;]. Multiple buckets: All buckets MUST have compatible schemas. Schema compatibility validated at collection creation. Compatible schemas have: 1) Same field names, 2) Same field types, 3) Same required status. Documents will include root_bucket_id to track which bucket they came from. Use cases: multi-region data, multi-team consolidation, environment aggregation. | [optional] 
**collection_id** | **str** | Collection ID when type&#x3D;&#39;collection&#39; (single collection). Use this OR collection_ids (not both). REQUIRED when type&#x3D;&#39;collection&#39; and processing single collection. NOT ALLOWED when type&#x3D;&#39;bucket&#39;. The collection will process documents from this upstream collection. The upstream collection&#39;s output_schema becomes this collection&#39;s input_schema. This enables decomposition trees (multi-stage pipelines). Example: Process frames collection → create scenes collection. | [optional] 
**collection_ids** | **List[str]** | List of collection IDs when type&#x3D;&#39;collection&#39; (multiple collections). Use this OR collection_id (not both). REQUIRED when type&#x3D;&#39;collection&#39; and processing multiple collections. NOT ALLOWED when type&#x3D;&#39;bucket&#39;. Used for operations that consolidate multiple upstream collections. Example: Clustering across multiple collections → cluster output collection. All collections must have compatible schemas for consolidation operations. | [optional] 
**inherited_bucket_ids** | **List[str]** | List of original bucket IDs that source collections originated from. OPTIONAL. Only used when type&#x3D;&#39;collection&#39;. Tracks the complete lineage chain: buckets → collections → derived collections. Extracted from upstream collection metadata at collection creation time. Enables tracing derived collections (like cluster outputs) back to original data sources. Example: Cluster output collection inherits bucket IDs from its source collections. Format: List of bucket IDs with &#39;bkt_&#39; prefix. | [optional] 
**source_filters** | [**SourceFiltersInput**](SourceFiltersInput.md) | Optional filters to apply to source data. When specified, only objects/documents matching these filters will be processed by this collection. Filters are evaluated at batch creation time. Uses same LogicalOperator model as list APIs for consistency. | [optional] 

## Example

```python
from mixpeek.models.source_config_input import SourceConfigInput

# TODO update the JSON string below
json = "{}"
# create an instance of SourceConfigInput from a JSON string
source_config_input_instance = SourceConfigInput.from_json(json)
# print the JSON string representation of the object
print(SourceConfigInput.to_json())

# convert the object into a dict
source_config_input_dict = source_config_input_instance.to_dict()
# create an instance of SourceConfigInput from a dict
source_config_input_from_dict = SourceConfigInput.from_dict(source_config_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


