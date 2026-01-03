# S3TagSource

Extract value from an S3/Tigris object tag.  S3 object tags are key-value pairs attached to objects, commonly used for categorization, cost allocation, and metadata. Tags are limited to 10 per object with keys up to 128 chars and values up to 256 chars.  Provider Compatibility: S3, Tigris, MinIO, DigitalOcean Spaces, Wasabi  Example S3 CLI to set tag:     aws s3api put-object-tagging --bucket my-bucket --key video.mp4 \\         --tagging 'TagSet=[{Key=category,Value=marketing}]'  Example mapping:     {\"type\": \"tag\", \"key\": \"category\"} -> extracts \"marketing\" from the tag  Attributes:     type: Must be \"tag\" to identify this source type     key: The tag key to extract (case-sensitive, max 128 chars)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Source type identifier. Must be &#39;tag&#39; for S3/Tigris object tags. | [optional] [default to 'tag']
**key** | **str** | The tag key to extract. Case-sensitive. Must match the exact tag key on the S3/Tigris object. Common examples: &#39;category&#39;, &#39;project&#39;, &#39;owner&#39;, &#39;environment&#39;. Maximum length: 128 characters. | 

## Example

```python
from mixpeek.models.s3_tag_source import S3TagSource

# TODO update the JSON string below
json = "{}"
# create an instance of S3TagSource from a JSON string
s3_tag_source_instance = S3TagSource.from_json(json)
# print the JSON string representation of the object
print(S3TagSource.to_json())

# convert the object into a dict
s3_tag_source_dict = s3_tag_source_instance.to_dict()
# create an instance of S3TagSource from a dict
s3_tag_source_from_dict = S3TagSource.from_dict(s3_tag_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


