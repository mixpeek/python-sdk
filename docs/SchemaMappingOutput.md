# SchemaMappingOutput

Complete schema mapping configuration for a sync.  Defines how source data (files, tags, metadata, columns) maps to the target bucket schema. Each key is a target field/blob name in the bucket.  **Key Concepts:** - Keys are target bucket schema field names - Values define the source and extraction method - At least one blob mapping is typically required for file syncs - Field mappings extract metadata alongside the file content  **Provider Examples:**  **S3/Tigris Video Sync:** ```json {     \"content\": {         \"target_type\": \"blob\",         \"source\": {\"type\": \"file\"},         \"blob_type\": \"video\"     },     \"category\": {         \"target_type\": \"field\",         \"source\": {\"type\": \"tag\", \"key\": \"category\"}     },     \"source_bucket\": {         \"target_type\": \"field\",         \"source\": {\"type\": \"constant\", \"value\": \"production-videos\"}     } } ```  **Snowflake Customer Table Sync:** ```json {     \"customer_name\": {         \"target_type\": \"field\",         \"source\": {\"type\": \"column\", \"name\": \"NAME\"}     },     \"profile_image\": {         \"target_type\": \"blob\",         \"source\": {\"type\": \"column\", \"name\": \"AVATAR_URL\"},         \"blob_type\": \"image\"     },     \"segment\": {         \"target_type\": \"field\",         \"source\": {\"type\": \"column\", \"name\": \"CUSTOMER_SEGMENT\"},         \"transform\": \"lowercase\"     } } ```  **Google Drive with Folder Categories:** ```json {     \"content\": {         \"target_type\": \"blob\",         \"source\": {\"type\": \"file\"},         \"blob_type\": \"auto\"     },     \"department\": {         \"target_type\": \"field\",         \"source\": {\"type\": \"folder_path\", \"segment\": 0},         \"transform\": \"lowercase\"     },     \"description\": {         \"target_type\": \"field\",         \"source\": {\"type\": \"drive_property\", \"key\": \"description\"}     } } ```  Attributes:     mappings: Dictionary mapping target field names to their source extractors

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mappings** | [**Dict[str, MappingsValue]**](MappingsValue.md) | Dictionary mapping target field names to their source extractors. Keys are bucket schema field names (e.g., &#39;content&#39;, &#39;category&#39;). Values are mapping entries defining how to extract and store the data. At least one blob mapping (target_type&#x3D;&#39;blob&#39;) is recommended for file syncs. | 

## Example

```python
from mixpeek.models.schema_mapping_output import SchemaMappingOutput

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaMappingOutput from a JSON string
schema_mapping_output_instance = SchemaMappingOutput.from_json(json)
# print the JSON string representation of the object
print(SchemaMappingOutput.to_json())

# convert the object into a dict
schema_mapping_output_dict = schema_mapping_output_instance.to_dict()
# create an instance of SchemaMappingOutput from a dict
schema_mapping_output_from_dict = SchemaMappingOutput.from_dict(schema_mapping_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


