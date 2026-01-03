# BaseRateLimits

Rate limits by operation type (requests per minute).  The rate limiting system uses 5 categories aligned with actual resource consumption:  Categories:     metadata: Infrastructure and configuration operations (namespaces, collections,              retrievers, taxonomies, clusters CRUD). Zero-credit operations with              highest rate limits.      data: Data operations (objects, documents CRUD). Low-credit operations with           high rate limits.      search: Search and retrieval operations (retriever/taxonomy execution).             Medium-credit operations with moderate rate limits.      upload: File upload operations (credit-intensive: 1 credit/MB). Variable-credit             operations with lower rate limits.      compute: Compute operations (cluster execution, batch processing). High-credit              operations (10 credits/min video) with lowest rate limits.  Rate Limit Strategy:     Higher limits for low-cost operations (metadata, data)     Lower limits for high-cost operations (upload, compute)     This aligns API throttling with actual infrastructure costs  Examples:     - Creating a namespace: Uses 'metadata' category (fast, cheap)     - Uploading a file: Uses 'upload' category (slow, expensive per MB)     - Executing a retriever: Uses 'search' category (moderate cost)     - Running batch processing: Uses 'compute' category (very expensive)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **int** | REQUIRED. Rate limit for infrastructure and configuration operations (namespaces, collections, retrievers, taxonomies, clusters CRUD). These are zero-credit operations with highest rate limits since they&#39;re cheap to execute. Examples: creating collections, updating retrievers, listing namespaces. | [optional] [default to 10]
**data** | **int** | REQUIRED. Rate limit for data operations (objects, documents CRUD). Low-credit operations with high rate limits. Examples: creating documents, updating objects, batch document updates. | [optional] [default to 10]
**search** | **int** | REQUIRED. Rate limit for search and retrieval operations (retriever/taxonomy execution). Medium-credit operations with moderate rate limits. Examples: executing retrievers, running taxonomy matching. | [optional] [default to 10]
**upload** | **int** | REQUIRED. Rate limit for file upload operations. Credit-intensive (1 credit/MB) with lower rate limits to prevent excessive resource consumption. Examples: uploading files, generating presigned URLs. | [optional] [default to 10]
**compute** | **int** | REQUIRED. Rate limit for compute operations (cluster execution, batch processing). High-credit operations (10 credits/min video) with lowest rate limits. Examples: submitting batches, executing clusters, triggering syncs. | [optional] [default to 10]

## Example

```python
from mixpeek.models.base_rate_limits import BaseRateLimits

# TODO update the JSON string below
json = "{}"
# create an instance of BaseRateLimits from a JSON string
base_rate_limits_instance = BaseRateLimits.from_json(json)
# print the JSON string representation of the object
print(BaseRateLimits.to_json())

# convert the object into a dict
base_rate_limits_dict = base_rate_limits_instance.to_dict()
# create an instance of BaseRateLimits from a dict
base_rate_limits_from_dict = BaseRateLimits.from_dict(base_rate_limits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


