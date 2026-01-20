# ErrorHandling3

Error handling strategy for web scrape failures.  SKIP: Skip documents that fail to fetch, continue with others.     - Failed documents are passed through unchanged     - Best for optional enrichment where failures are acceptable     - Example: Adding extra context that isn't critical  REMOVE: Remove documents that fail to fetch from results.     - Failed documents are filtered out completely     - Best when enriched content is required     - Example: Must have full content to proceed  RAISE: Raise exception on first failure, halt pipeline.     - Pipeline stops immediately on any failure     - Best for critical enrichment where failures indicate problems     - Example: Required content for compliance/audit

## Enum

* `SKIP` (value: `'skip'`)

* `REMOVE` (value: `'remove'`)

* `RAISE` (value: `'raise'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


