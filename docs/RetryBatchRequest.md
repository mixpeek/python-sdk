# RetryBatchRequest

Request to retry failed documents in a batch.  Allows selective retry of failed documents with intelligent filtering by error type and tier. Retries use exponential backoff and respect max retry limits.  Use Cases:     - Retry only transient errors after resolving temporary infrastructure issues     - Retry specific processing tiers that failed     - Retry all failed documents regardless of error type (force retry)  Requirements:     - retry_mode: REQUIRED. Determines which documents to retry     - tier_nums: OPTIONAL. Only retry failures from specific tiers (empty = all tiers)     - max_retry_count: OPTIONAL. Skip documents that have been retried this many times  Behavior:     - 'transient_only': Retries only transient errors (network, timeout, rate limit)     - 'all': Retries both transient and permanent errors     - Documents beyond max_retry_count are excluded from retry     - Each retry increments the document's retry_count

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retry_mode** | **str** | Determines which types of failed documents to retry. &#39;transient_only&#39;: Only retry documents that failed with transient errors (network issues, timeouts, rate limits). This is the recommended default as it avoids retrying documents with permanent failures (invalid data, missing fields, incompatible formats). &#39;all&#39;: Retry all failed documents regardless of error type. Use this for force retries after fixing data issues or updating extraction logic. | [optional] [default to 'transient_only']
**tier_nums** | **List[int]** | List of specific tier numbers to retry failures from. OPTIONAL - If not provided or empty list, retries failures from all tiers. Use this to selectively retry a specific processing stage. Example: [2] would only retry failures from tier 2 (the third processing stage). Tier numbering starts at 0 (bucket → collection), tier 1+ are collection → collection. | [optional] 
**max_retry_count** | **int** | Maximum number of times a document can be retried. Documents that have been retried this many times already are excluded. Prevents infinite retry loops for documents with persistent issues. Default is 3 retries per document. Set to higher value for more aggressive retries. | [optional] [default to 3]

## Example

```python
from mixpeek.models.retry_batch_request import RetryBatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RetryBatchRequest from a JSON string
retry_batch_request_instance = RetryBatchRequest.from_json(json)
# print the JSON string representation of the object
print(RetryBatchRequest.to_json())

# convert the object into a dict
retry_batch_request_dict = retry_batch_request_instance.to_dict()
# create an instance of RetryBatchRequest from a dict
retry_batch_request_from_dict = RetryBatchRequest.from_dict(retry_batch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


