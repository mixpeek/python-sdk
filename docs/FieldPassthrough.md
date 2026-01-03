# FieldPassthrough

Configuration for passing fields from source to output documents.  Simple field passthrough: specify which fields to copy from source (bucket object or upstream collection document) to the output documents alongside extractor outputs.  Use Cases:     - Preserve identifiers: campaign_id, product_sku, user_id     - Keep metadata: category, tags, author, timestamp     - Maintain business context: priority, status, region     - Extract nested values: metadata.author, config.model_version     - Rename fields for cleaner schemas: doc_title → title  Field Selection:     - WITHOUT field_passthrough: Only extractor outputs appear in documents     - WITH field_passthrough: Specified fields + extractor outputs     - WITH include_all_source_fields=True: All source fields + extractor outputs  Field Naming:     - WITHOUT target_path: Output uses source name (or last component for nested)       - \"title\" → \"title\"       - \"metadata.author\" → \"author\"     - WITH target_path: Output uses specified name       - source_path=\"doc_title\", target_path=\"title\" → \"title\"       - source_path=\"metadata.author\", target_path=\"contributor\" → \"contributor\"  Requirements:     - source_path is REQUIRED - specifies which field to copy (supports dot notation)     - target_path is OPTIONAL - rename field in output (default: auto-derived name)     - default is OPTIONAL - provides fallback if field missing (default: omit field)     - required is OPTIONAL - errors if field missing (default: false, omit field)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_path** | **str** | REQUIRED. Path to the source field to copy. Simple fields: Use field name directly (e.g., &#39;title&#39;, &#39;campaign_id&#39;). Nested fields: Use dot notation (e.g., &#39;metadata.author&#39;, &#39;config.model.version&#39;). The field must exist in the source bucket schema or upstream collection schema. Without target_path, nested fields are flattened: &#39;metadata.author&#39; becomes &#39;author&#39; in output. | 
**target_path** | **str** | OPTIONAL. Target field name in output document. If NOT PROVIDED: Uses source_path name (or last component for nested paths).   - &#39;title&#39; → &#39;title&#39;   - &#39;metadata.author&#39; → &#39;author&#39; If PROVIDED: Uses this exact name in output.   - source_path&#x3D;&#39;doc_title&#39;, target_path&#x3D;&#39;title&#39; → &#39;title&#39;   - source_path&#x3D;&#39;metadata.author&#39;, target_path&#x3D;&#39;contributor&#39; → &#39;contributor&#39; Use cases:   - Rename fields for cleaner API schemas   - Avoid name conflicts with extractor outputs   - Standardize field names across different sources Constraints:   - Must not conflict with system fields (document_id, collection_id, etc.)   - Must not conflict with extractor output fields   - Must be a valid field name (alphanumeric, underscores, hyphens) | [optional] 
**default** | **object** |  | [optional] 
**required** | **bool** | OPTIONAL. Whether this field MUST exist in source. If True and field missing: Raises validation error, processing fails. If False and field missing: Field omitted (or default used if provided). Use True for: Critical identifiers, required business fields. Use False for: Optional metadata, nice-to-have fields. Default: False (field is optional). | [optional] [default to False]

## Example

```python
from mixpeek.models.field_passthrough import FieldPassthrough

# TODO update the JSON string below
json = "{}"
# create an instance of FieldPassthrough from a JSON string
field_passthrough_instance = FieldPassthrough.from_json(json)
# print the JSON string representation of the object
print(FieldPassthrough.to_json())

# convert the object into a dict
field_passthrough_dict = field_passthrough_instance.to_dict()
# create an instance of FieldPassthrough from a dict
field_passthrough_from_dict = FieldPassthrough.from_dict(field_passthrough_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


