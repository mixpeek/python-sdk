# CollectionExportRequest

Request model for exporting collection data.  **Export Formats:** - **JSON**: Line-delimited JSON (JSONL) format, one document per line. Good for streaming and large files. - **CSV**: Comma-separated values. Best for tabular data analysis in spreadsheets. - **PARQUET**: Columnar format optimized for analytics. Best for large datasets and data pipelines.  **Vector Export:** Vectors are stored separately from document metadata due to their large size. When `include_vectors=True`, vectors are exported to a separate file with the naming convention: `{collection_name}_vectors.{format}`  **Field Selection:** Use `select_fields` to export only specific fields, reducing file size for large collections. Supports dot notation for nested fields (e.g., \"metadata.title\").  **Filtering:** Apply filters to export a subset of documents. Uses the same LogicalOperator format as the documents list endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | [**ExportFormat**](ExportFormat.md) | Export format: json (line-delimited), csv, or parquet (default). | [optional] 
**include_vectors** | **bool** | Whether to include vectors in the export. Vectors are exported to a separate file due to their large size. This significantly increases export time and file size. | [optional] [default to False]
**select_fields** | **List[str]** | Specific fields to include in the export. If not provided, all fields are exported. Supports dot notation for nested fields (e.g., &#39;metadata.title&#39;, &#39;metadata.author&#39;). | [optional] 
**filters** | [**LogicalOperatorInput**](LogicalOperatorInput.md) | Filter conditions to export only matching documents. Uses LogicalOperator format (AND/OR/NOT) same as document listing. | [optional] 
**sample_size** | **int** | Maximum number of documents to export. If not provided, exports all documents. Useful for testing exports or creating sample datasets. | [optional] 

## Example

```python
from mixpeek.models.collection_export_request import CollectionExportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionExportRequest from a JSON string
collection_export_request_instance = CollectionExportRequest.from_json(json)
# print the JSON string representation of the object
print(CollectionExportRequest.to_json())

# convert the object into a dict
collection_export_request_dict = collection_export_request_instance.to_dict()
# create an instance of CollectionExportRequest from a dict
collection_export_request_from_dict = CollectionExportRequest.from_dict(collection_export_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


