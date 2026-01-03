# ListUploadsRequest

Request model for listing uploads with filtering, sorting, and search.  Provides flexible querying capabilities using the same filter/sort framework as documents, objects, and other list endpoints.  Supports:     - Complex filters using LogicalOperator (AND, OR, NOT)     - Shorthand filter syntax: {\"metadata.campaign\": \"summer_2024\"}     - Full-text search across filename and metadata     - Multi-field sorting     - Pagination with limit/offset  Examples:     - List all pending uploads in a bucket     - Find uploads by metadata campaign     - Search for uploads by filename pattern     - Sort by file size or creation date

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**LogicalOperatorInput**](LogicalOperatorInput.md) | Complex filters using logical operators (AND, OR, NOT). Supports shorthand syntax: pass field-value pairs for equality matching. Examples:   - Filter by status: {&#39;status&#39;: &#39;PENDING&#39;}   - Filter by metadata: {&#39;metadata.campaign&#39;: &#39;summer_2024&#39;}   - Complex: {&#39;AND&#39;: [{&#39;field&#39;: &#39;status&#39;, &#39;operator&#39;: &#39;eq&#39;, &#39;value&#39;: &#39;PENDING&#39;},                       {&#39;field&#39;: &#39;file_size_bytes&#39;, &#39;operator&#39;: &#39;gte&#39;, &#39;value&#39;: 1000000}]} See LogicalOperator documentation for full syntax. | [optional] 
**sort** | [**SortOption**](SortOption.md) | Sort options for ordering results. Can sort by any field including metadata fields using dot notation. Default: created_at descending (newest first). Examples:   - Sort by creation date: {&#39;field&#39;: &#39;created_at&#39;, &#39;direction&#39;: &#39;desc&#39;}   - Sort by file size: {&#39;field&#39;: &#39;file_size_bytes&#39;, &#39;direction&#39;: &#39;asc&#39;}   - Sort by metadata: {&#39;field&#39;: &#39;metadata.priority&#39;, &#39;direction&#39;: &#39;desc&#39;} | [optional] 
**search** | **str** | Full-text search across filename and metadata fields. Case-insensitive partial matching. Searches in: filename, metadata values (converted to strings). Examples:   - &#39;video&#39; - finds &#39;product_video.mp4&#39;, &#39;tutorial_video.mov&#39;   - &#39;summer&#39; - finds uploads with metadata.campaign&#x3D;&#39;summer_2024&#39; | [optional] 
**return_presigned_urls** | **bool** | Whether to regenerate presigned URLs for S3 access in the response. OPTIONAL, defaults to false. If true:   - Generates new GET presigned URLs for completed uploads   - Useful for downloading files from S3   - Adds ~50ms per upload to response time. If false:   - No presigned URLs in response   - Faster response time. Note: Original PUT presigned URLs are never returned (security). | [optional] [default to False]
**limit** | **int** | Maximum number of uploads to return. OPTIONAL, defaults to 20. | [optional] [default to 20]
**offset** | **int** | Number of uploads to skip for pagination. OPTIONAL, defaults to 0. | [optional] [default to 0]

## Example

```python
from mixpeek.models.list_uploads_request import ListUploadsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListUploadsRequest from a JSON string
list_uploads_request_instance = ListUploadsRequest.from_json(json)
# print the JSON string representation of the object
print(ListUploadsRequest.to_json())

# convert the object into a dict
list_uploads_request_dict = list_uploads_request_instance.to_dict()
# create an instance of ListUploadsRequest from a dict
list_uploads_request_from_dict = ListUploadsRequest.from_dict(list_uploads_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


