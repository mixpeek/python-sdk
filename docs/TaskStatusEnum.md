# TaskStatusEnum

Enumeration of task statuses for tracking asynchronous operations.  Task statuses indicate the current state of asynchronous operations like batch processing, object ingestion, clustering, and taxonomy execution.  Status Categories:     Operation Statuses: Track progress of async operations     Lifecycle Statuses: Track entity state (buckets, collections, namespaces)  Values:     PENDING: Task is queued but has not started processing yet     IN_PROGRESS: Task is currently being executed     PROCESSING: Task is actively processing data (similar to IN_PROGRESS)     COMPLETED: Task finished successfully with no errors     COMPLETED_WITH_ERRORS: Task finished but some items failed (partial success)     FAILED: Task encountered an error and could not complete     CANCELED: Task was manually canceled by a user or system     UNKNOWN: Task status could not be determined     SKIPPED: Task was intentionally skipped     DRAFT: Task is in draft state and not yet submitted      ACTIVE: Entity is active and operational (for buckets, collections, etc.)     ARCHIVED: Entity has been archived     SUSPENDED: Entity has been temporarily suspended  Terminal Statuses:     COMPLETED, COMPLETED_WITH_ERRORS, FAILED, CANCELED are terminal statuses.     Once a task reaches these states, it will not transition to another state.  Partial Success Handling:     COMPLETED_WITH_ERRORS indicates that the operation completed but some     documents/items failed. The task result includes:     - List of successful items     - List of failed items with error details     - Success rate percentage     This allows clients to handle partial success scenarios appropriately.  Polling Guidance:     - Poll tasks in PENDING, IN_PROGRESS, or PROCESSING states     - Stop polling when task reaches COMPLETED, COMPLETED_WITH_ERRORS, FAILED, or CANCELED     - Use exponential backoff (1s → 30s) when polling

## Enum

* `PENDING` (value: `'PENDING'`)

* `IN_PROGRESS` (value: `'IN_PROGRESS'`)

* `PROCESSING` (value: `'PROCESSING'`)

* `COMPLETED` (value: `'COMPLETED'`)

* `COMPLETED_WITH_ERRORS` (value: `'COMPLETED_WITH_ERRORS'`)

* `FAILED` (value: `'FAILED'`)

* `CANCELED` (value: `'CANCELED'`)

* `UNKNOWN` (value: `'UNKNOWN'`)

* `SKIPPED` (value: `'SKIPPED'`)

* `DRAFT` (value: `'DRAFT'`)

* `ACTIVE` (value: `'ACTIVE'`)

* `ARCHIVED` (value: `'ARCHIVED'`)

* `SUSPENDED` (value: `'SUSPENDED'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


