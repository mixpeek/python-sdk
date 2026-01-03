# SubmitBatchRequest

Request model for submitting a batch for processing.  This model allows configuration of processing behavior for the batch, such as whether to track processing history in document metadata.  Use Cases:     - Submit batch with full audit trail (include_processing_history=True)     - Submit batch without processing history for cleaner metadata (include_processing_history=False)     - Default behavior includes processing history for debugging and lineage tracking  Requirements:     - include_processing_history: OPTIONAL, defaults to True

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_processing_history** | **bool** | OPTIONAL (defaults to True). Controls whether processing operations are tracked in document internal_metadata.processing_history. When True: Each enrichment operation (taxonomy application, clustering, etc.) adds an audit trail entry. When False: Documents are enriched without processing history tracking, resulting in cleaner metadata. Use True for: Debugging, audit requirements, lineage tracking, understanding document transformations. Use False for: Production workloads where metadata size matters, simplified document structure. Processing history entries include: operation type, timestamp, and IDs of applied resources (taxonomies, clusters, etc.). | [optional] [default to True]

## Example

```python
from mixpeek.models.submit_batch_request import SubmitBatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SubmitBatchRequest from a JSON string
submit_batch_request_instance = SubmitBatchRequest.from_json(json)
# print the JSON string representation of the object
print(SubmitBatchRequest.to_json())

# convert the object into a dict
submit_batch_request_dict = submit_batch_request_instance.to_dict()
# create an instance of SubmitBatchRequest from a dict
submit_batch_request_from_dict = SubmitBatchRequest.from_dict(submit_batch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


