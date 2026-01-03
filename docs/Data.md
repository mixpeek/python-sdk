# Data

EITHER data OR upload_id must be provided (mutually exclusive).   File data in one of several INTERCHANGEABLE formats:   **Format 1: URL String (HTTP/HTTPS/S3)** - Direct URL to file on the web or in S3 - Examples: 'https://example.com/video.mp4', 's3://bucket/key' - Use for: Public files, existing S3 objects, pre-signed URLs - File is downloaded and uploaded to internal S3 (if canonicalize_source=True)   **Format 2: Data URI String (base64)** - Self-contained base64 data with MIME type - Format: 'data:<mime_type>;base64,<encoded_data>' - Example: 'data:image/jpeg;base64,/9j/4AAQSkZJRg...' - Use for: Small files (<5MB), mobile uploads, inline test data - MIME type automatically extracted from URI - Data is decoded, validated, and uploaded to S3 automatically   **Format 3: Base64 Dictionary** - Structured format with explicit metadata - Required keys: 'base64' (encoded data) - Optional keys: 'mime_type', 'filename' - Example: {'base64': '/9j/4AAQ...', 'mime_type': 'image/jpeg', 'filename': 'photo.jpg'} - Use for: When you need explicit MIME type control - Data is decoded, validated, and uploaded to S3 automatically   **Format 4: URL Dictionary** - Structured format for URL references - Required keys: 'url' - Example: {'url': 'https://example.com/file.jpg'} - Use for: Consistency with other dict formats   **Processing:** All formats are converted to internal S3 URLs before storage. The engine always receives S3 URLs regardless of input format.   **Size Limits (Base64 only):** Base64 data: 5MB (free), 10MB (pro), 50MB (enterprise). URLs: No limit (downloaded on-demand). For files exceeding limits, use presigned upload workflow: POST /buckets/{id}/uploads   **Validation:** - Base64: Encoding validated, MIME type detected, size checked - URLs: Accessibility verified, content-type validated - All: Schema type compatibility enforced

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from mixpeek.models.data import Data

# TODO update the JSON string below
json = "{}"
# create an instance of Data from a JSON string
data_instance = Data.from_json(json)
# print the JSON string representation of the object
print(Data.to_json())

# convert the object into a dict
data_dict = data_instance.to_dict()
# create an instance of Data from a dict
data_from_dict = Data.from_dict(data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


