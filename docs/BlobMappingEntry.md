# BlobMappingEntry

Maps a source to a blob in the bucket object.  Used for mapping files or URL references to blob fields. The blob_type determines how the content is processed by extractors. This is the primary way to map synced files into the Mixpeek extraction pipeline.  Example: Map the synced file to the primary \"content\" blob     {         \"target_type\": \"blob\",         \"source\": {\"type\": \"file\"},         \"blob_type\": \"auto\",         \"blob_property\": \"content\"     }  Example: Map a database column URL to an image blob     {         \"target_type\": \"blob\",         \"source\": {\"type\": \"column\", \"name\": \"AVATAR_URL\"},         \"blob_type\": \"image\",         \"blob_property\": \"profile_image\"     }  Example: Map with explicit mime_type override     {         \"target_type\": \"blob\",         \"source\": {\"type\": \"file\"},         \"blob_type\": \"video\",         \"blob_property\": \"content\",         \"mime_type_override\": \"video/mp4\"     }  Attributes:     target_type: Must be \"blob\" for blob mappings     source: The source extractor (usually \"file\" for synced content)     blob_type: Content type hint for extractors (auto, image, video, etc.)     blob_property: Name of the blob property in the bucket schema     mime_type_override: Optional explicit mime_type to use

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_type** | **str** | Target type. Must be &#39;blob&#39; for blob mappings. | [optional] [default to 'blob']
**source** | [**Source**](Source.md) |  | 
**blob_type** | [**BlobType**](BlobType.md) | Type of blob content. Determines which extractors can process it. &#39;auto&#39; (default) infers type from mime_type - recommended for files. Explicit types: &#39;image&#39;, &#39;video&#39;, &#39;audio&#39;, &#39;text&#39;, &#39;document&#39;, &#39;json&#39;, &#39;binary&#39;. Use explicit types when mime_type detection is unreliable. | [optional] 
**blob_property** | **str** | The blob property name in the bucket schema. This identifies which blob in the object&#39;s blobs array. Default: &#39;content&#39; (the primary blob). Must match a blob property defined in the bucket schema. | [optional] [default to 'content']
**mime_type_override** | **str** | Optional mime_type to use instead of auto-detection. Useful when the source doesn&#39;t provide accurate mime_type. Format: &#39;type/subtype&#39; (e.g., &#39;image/jpeg&#39;, &#39;video/mp4&#39;). When set, this value is used for blob.details.mime_type. | [optional] 

## Example

```python
from mixpeek.models.blob_mapping_entry import BlobMappingEntry

# TODO update the JSON string below
json = "{}"
# create an instance of BlobMappingEntry from a JSON string
blob_mapping_entry_instance = BlobMappingEntry.from_json(json)
# print the JSON string representation of the object
print(BlobMappingEntry.to_json())

# convert the object into a dict
blob_mapping_entry_dict = blob_mapping_entry_instance.to_dict()
# create an instance of BlobMappingEntry from a dict
blob_mapping_entry_from_dict = BlobMappingEntry.from_dict(blob_mapping_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


