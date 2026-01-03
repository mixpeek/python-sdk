# BatchErrorDetail

Detailed error information for batch processing failures.  Provides structured error tracking at both object and batch levels. Enables better debugging, retry logic, and error analytics.  Use Cases:     - Track specific errors that occurred during processing     - Identify error patterns across multiple documents     - Provide actionable recovery suggestions     - Enable intelligent retry logic based on error type  Object-level tracking: Attached to individual document processing failures Batch-level tracking: Aggregated summaries in batch metadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_type** | [**ErrorCategory**](ErrorCategory.md) | REQUIRED. Category of error that occurred. Used for filtering, retry logic, and error analytics. DEPENDENCY: Missing packages/modules (e.g., google-genai not installed). AUTHENTICATION: Invalid credentials or expired tokens. VALIDATION: Schema mismatches or invalid input data. RUNTIME: Code exceptions or processing failures. NETWORK: Connectivity issues or timeouts. RESOURCE: Out of memory or disk space. | 
**message** | **str** | REQUIRED. Human-readable error message. Concise description of what went wrong. Should be actionable and help users understand the issue. | 
**component** | **str** | OPTIONAL. Component or service where the error occurred. Helps identify which part of the system failed. Examples: service class names, module names, or feature names. | [optional] 
**stage** | **str** | OPTIONAL. Processing stage where the error occurred. Identifies which pipeline stage failed. Examples: pipeline stage names from collection configuration. | [optional] 
**traceback** | **str** | OPTIONAL. Full Python traceback for debugging. Includes stack trace for code-level troubleshooting. Should be truncated if too long (e.g., max 2000 chars). | [optional] 
**timestamp** | **datetime** | REQUIRED. ISO 8601 timestamp when the error occurred. Used for chronological error tracking and debugging. | [optional] 
**affected_document_ids** | **List[str]** | OPTIONAL. List of document IDs affected by this error. For object-level errors: contains single document ID. For batch-level aggregation: contains all affected document IDs. Used to identify scope of impact. | [optional] 
**affected_count** | **int** | REQUIRED. Number of documents affected by this error. For object-level: typically 1. For batch-level aggregation: total count of affected documents. Used for error impact analysis. | [optional] [default to 1]
**recovery_suggestion** | **str** | OPTIONAL. Actionable suggestion for resolving the error. Helps users quickly fix common issues. Examples: install missing package, check credentials, update schema. | [optional] 
**metadata** | **Dict[str, object]** | OPTIONAL. Additional error context and metadata. Free-form dictionary for error-specific details. Examples: retry_count, last_retry_at, error_code, http_status. | [optional] 

## Example

```python
from mixpeek.models.batch_error_detail import BatchErrorDetail

# TODO update the JSON string below
json = "{}"
# create an instance of BatchErrorDetail from a JSON string
batch_error_detail_instance = BatchErrorDetail.from_json(json)
# print the JSON string representation of the object
print(BatchErrorDetail.to_json())

# convert the object into a dict
batch_error_detail_dict = batch_error_detail_instance.to_dict()
# create an instance of BatchErrorDetail from a dict
batch_error_detail_from_dict = BatchErrorDetail.from_dict(batch_error_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


