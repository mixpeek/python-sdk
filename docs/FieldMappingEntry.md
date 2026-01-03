# FieldMappingEntry

Maps a source value to a bucket schema field.  Used for mapping metadata, tags, columns, or extracted values to regular fields in the bucket schema (strings, numbers, arrays, etc.). Does NOT handle file content - use BlobMappingEntry for that.  Example: Map S3 tag \"category\" to bucket field \"content_category\"     {         \"target_type\": \"field\",         \"source\": {\"type\": \"tag\", \"key\": \"category\"}     }  Example: Map folder name to \"department\" with lowercase transform     {         \"target_type\": \"field\",         \"source\": {\"type\": \"folder_path\", \"segment\": 0},         \"transform\": \"lowercase\"     }  Example: Map filename regex capture to \"date\" field     {         \"target_type\": \"field\",         \"source\": {\"type\": \"filename_regex\", \"pattern\": \"^(\\d{4}-\\d{2}-\\d{2})\"},         \"required\": true     }  Attributes:     target_type: Must be \"field\" for schema field mappings     source: The source extractor defining where to get the value     transform: Optional transformation to apply (lowercase, uppercase, trim)     required: Whether missing values should fail the sync

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_type** | **str** | Target type. Must be &#39;field&#39; for regular schema fields. | [optional] [default to 'field']
**source** | [**Source1**](Source1.md) |  | 
**transform** | **str** | Optional transformation to apply to the extracted value. Supported transforms: &#39;lowercase&#39; - convert to lowercase, &#39;uppercase&#39; - convert to uppercase, &#39;trim&#39; - remove leading/trailing whitespace, &#39;json_parse&#39; - parse JSON string to object/array. Transforms are applied after extraction, before storage. | [optional] 
**required** | **bool** | If True, the sync will fail if this field cannot be extracted. If False (default), missing values result in the field being omitted. Use required&#x3D;True for critical fields that must be present. | [optional] [default to False]

## Example

```python
from mixpeek.models.field_mapping_entry import FieldMappingEntry

# TODO update the JSON string below
json = "{}"
# create an instance of FieldMappingEntry from a JSON string
field_mapping_entry_instance = FieldMappingEntry.from_json(json)
# print the JSON string representation of the object
print(FieldMappingEntry.to_json())

# convert the object into a dict
field_mapping_entry_dict = field_mapping_entry_instance.to_dict()
# create an instance of FieldMappingEntry from a dict
field_mapping_entry_from_dict = FieldMappingEntry.from_dict(field_mapping_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


