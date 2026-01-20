# ContentInput1

Generic content input for automatic content-type detection.  Used for URL or base64 inputs where the content type is not known upfront. The system will automatically detect the content type (image, video, text, etc.) and route to the appropriate feature extractor.  **IMPORTANT**: Exactly one of `url` or `base64` must be provided (mutually exclusive).  Use Cases:     - User provides a URL without specifying content type     - Client sends base64-encoded content     - Generic search where query can be any modality  Requirements:     - Provide exactly ONE: url OR base64 (mutually exclusive)     - System performs automatic content type detection     - Supported content types: images, videos, audio, documents  Examples:     URL input:         ```json         {\"url\": \"https://example.com/image.jpg\"}         ```      Base64 image input:         ```json         {\"base64\": \"data:image/jpeg;base64,/9j/4AAQSkZJRg...\"}         ```      Base64 video input:         ```json         {\"base64\": \"data:video/mp4;base64,AAAAIGZ0eXBpc2...\"}         ```

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | OPTIONAL. URL to content for embedding generation. Mutually exclusive with base64 - provide exactly one. System will automatically detect content type (image, video, text, etc.) via HTTP HEAD request and/or file extension analysis. Supported protocols: HTTP, HTTPS, S3 (for Mixpeek-managed buckets). S3 URLs must point to the configured AWS_BUCKET. Examples: image URL, video URL, text file URL, S3 object path. | [optional] 
**var_base64** | **str** | OPTIONAL. Base64-encoded content for embedding generation. Mutually exclusive with url - provide exactly one. Can include data URI scheme (data:mime/type;base64,...) or just base64 string. System will automatically detect content type from data URI or by decoding. Supported types: images, videos, audio, documents. Maximum size: Limited by your namespace configuration. | [optional] 

## Example

```python
from mixpeek.models.content_input1 import ContentInput1

# TODO update the JSON string below
json = "{}"
# create an instance of ContentInput1 from a JSON string
content_input1_instance = ContentInput1.from_json(json)
# print the JSON string representation of the object
print(ContentInput1.to_json())

# convert the object into a dict
content_input1_dict = content_input1_instance.to_dict()
# create an instance of ContentInput1 from a dict
content_input1_from_dict = ContentInput1.from_dict(content_input1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


