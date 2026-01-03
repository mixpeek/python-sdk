# PayloadIndexConfigOutput

Configuration for a payload index.  Defines the structure and behavior of a payload field index in Qdrant collections. Payload indexes enable efficient filtering and searching on document metadata.  Protected Indexes:     System-managed indexes (is_protected=True) cannot be modified or deleted by users.     These are essential for Mixpeek's internal operations:     - internal_id: Tenant isolation     - namespace_id: Namespace scoping     - collection_id, document_id: Document lineage     - bucket_id, object_id, root_object_id, root_bucket_id, source_object_id: Object lineage     - created_at, updated_at: Timestamps  Use Cases:     - Create custom metadata indexes for efficient filtering     - Configure full-text search on text fields     - Set up geospatial queries on location data     - Enable range queries on numeric fields  Requirements:     - field_name: REQUIRED - Must be unique within the namespace     - type: REQUIRED - Must match PayloadSchemaType enum     - field_schema: OPTIONAL - Auto-generated from type if not provided     - is_protected: OPTIONAL - Defaults to False (user-managed index)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_name** | **str** | Name of the payload field to index. Must be unique within the namespace. Use dot notation for nested fields (e.g., &#39;metadata.title&#39;). Cannot use protected system field names when is_protected&#x3D;False. | 
**type** | [**PayloadSchemaType**](PayloadSchemaType.md) | Data type of the indexed field. Determines query capabilities and storage optimization. TEXT: Full-text search. KEYWORD: Exact matching, filtering. INTEGER/FLOAT: Range queries, sorting. DATETIME: Temporal queries. GEO: Geospatial queries. BOOL: Boolean filtering. UUID: Unique identifier matching. | 
**field_schema** | [**FieldSchema**](FieldSchema.md) |  | [optional] 
**is_protected** | **bool** | Whether this index is system-managed and cannot be modified by users. Protected indexes (is_protected&#x3D;True) are created automatically by Mixpeek and are essential for internal operations like tenant isolation, lineage tracking, and document management. Users cannot create, modify, or delete protected indexes. User-created indexes always have is_protected&#x3D;False. | [optional] [default to False]

## Example

```python
from mixpeek.models.payload_index_config_output import PayloadIndexConfigOutput

# TODO update the JSON string below
json = "{}"
# create an instance of PayloadIndexConfigOutput from a JSON string
payload_index_config_output_instance = PayloadIndexConfigOutput.from_json(json)
# print the JSON string representation of the object
print(PayloadIndexConfigOutput.to_json())

# convert the object into a dict
payload_index_config_output_dict = payload_index_config_output_instance.to_dict()
# create an instance of PayloadIndexConfigOutput from a dict
payload_index_config_output_from_dict = PayloadIndexConfigOutput.from_dict(payload_index_config_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


