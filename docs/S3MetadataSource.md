# S3MetadataSource

Extract value from S3/Tigris object user metadata.  S3 user metadata (x-amz-meta-*) provides custom key-value pairs stored with the object. Unlike tags, metadata is set at upload time and is immutable without re-uploading the object.  Provider Compatibility: S3, Tigris, MinIO, DigitalOcean Spaces, Wasabi  Example S3 CLI to set metadata:     aws s3 cp video.mp4 s3://bucket/ --metadata '{\"author\":\"john\",\"version\":\"1.0\"}'  Example boto3 upload with metadata:     s3.put_object(Bucket='b', Key='k', Body=data, Metadata={'author': 'john'})  Example mapping:     {\"type\": \"metadata\", \"key\": \"author\"} -> extracts \"john\" from x-amz-meta-author  Attributes:     type: Must be \"metadata\" to identify this source type     key: The metadata key without 'x-amz-meta-' prefix (case-insensitive)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Source type identifier. Must be &#39;metadata&#39; for S3/Tigris user metadata. | [optional] [default to 'metadata']
**key** | **str** | The metadata key to extract (without &#39;x-amz-meta-&#39; prefix). Case-insensitive (S3 lowercases all metadata keys). Common examples: &#39;author&#39;, &#39;version&#39;, &#39;source-system&#39;, &#39;original-filename&#39;. Note: S3 automatically lowercases keys, so &#39;Author&#39; becomes &#39;author&#39;. | 

## Example

```python
from mixpeek.models.s3_metadata_source import S3MetadataSource

# TODO update the JSON string below
json = "{}"
# create an instance of S3MetadataSource from a JSON string
s3_metadata_source_instance = S3MetadataSource.from_json(json)
# print the JSON string representation of the object
print(S3MetadataSource.to_json())

# convert the object into a dict
s3_metadata_source_dict = s3_metadata_source_instance.to_dict()
# create an instance of S3MetadataSource from a dict
s3_metadata_source_from_dict = S3MetadataSource.from_dict(s3_metadata_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


