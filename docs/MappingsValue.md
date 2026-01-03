# MappingsValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_type** | **str** | Target type. Must be &#39;blob&#39; for blob mappings. | [optional] [default to 'blob']
**source** | [**Source**](Source.md) |  | 
**transform** | **str** | Optional transformation to apply to the extracted value. Supported transforms: &#39;lowercase&#39; - convert to lowercase, &#39;uppercase&#39; - convert to uppercase, &#39;trim&#39; - remove leading/trailing whitespace, &#39;json_parse&#39; - parse JSON string to object/array. Transforms are applied after extraction, before storage. | [optional] 
**required** | **bool** | If True, the sync will fail if this field cannot be extracted. If False (default), missing values result in the field being omitted. Use required&#x3D;True for critical fields that must be present. | [optional] [default to False]
**blob_type** | [**BlobType**](BlobType.md) | Type of blob content. Determines which extractors can process it. &#39;auto&#39; (default) infers type from mime_type - recommended for files. Explicit types: &#39;image&#39;, &#39;video&#39;, &#39;audio&#39;, &#39;text&#39;, &#39;document&#39;, &#39;json&#39;, &#39;binary&#39;. Use explicit types when mime_type detection is unreliable. | [optional] 
**blob_property** | **str** | The blob property name in the bucket schema. This identifies which blob in the object&#39;s blobs array. Default: &#39;content&#39; (the primary blob). Must match a blob property defined in the bucket schema. | [optional] [default to 'content']
**mime_type_override** | **str** | Optional mime_type to use instead of auto-detection. Useful when the source doesn&#39;t provide accurate mime_type. Format: &#39;type/subtype&#39; (e.g., &#39;image/jpeg&#39;, &#39;video/mp4&#39;). When set, this value is used for blob.details.mime_type. | [optional] 

## Example

```python
from mixpeek.models.mappings_value import MappingsValue

# TODO update the JSON string below
json = "{}"
# create an instance of MappingsValue from a JSON string
mappings_value_instance = MappingsValue.from_json(json)
# print the JSON string representation of the object
print(MappingsValue.to_json())

# convert the object into a dict
mappings_value_dict = mappings_value_instance.to_dict()
# create an instance of MappingsValue from a dict
mappings_value_from_dict = MappingsValue.from_dict(mappings_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


