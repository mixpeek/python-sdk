# WebhookEventType

Enum for webhook event types.  Each event type includes a comment indicating cache invalidation scope: - [KEY] = Invalidate specific document keys - [COLLECTION] = Invalidate collection-level cache - [NAMESPACE] = Invalidate namespace-level cache

## Enum

* `OBJECT_DOT_CREATED` (value: `'object.created'`)

* `OBJECT_DOT_UPDATED` (value: `'object.updated'`)

* `OBJECT_DOT_DELETED` (value: `'object.deleted'`)

* `COLLECTION_DOT_CREATED` (value: `'collection.created'`)

* `COLLECTION_DOT_UPDATED` (value: `'collection.updated'`)

* `COLLECTION_DOT_DELETED` (value: `'collection.deleted'`)

* `CLUSTER_DOT_CREATED` (value: `'cluster.created'`)

* `CLUSTER_DOT_UPDATED` (value: `'cluster.updated'`)

* `CLUSTER_DOT_DELETED` (value: `'cluster.deleted'`)

* `CLUSTER_DOT_EXECUTION_DOT_STARTED` (value: `'cluster.execution.started'`)

* `CLUSTER_DOT_EXECUTION_DOT_COMPLETED` (value: `'cluster.execution.completed'`)

* `CLUSTER_DOT_EXECUTION_DOT_FAILED` (value: `'cluster.execution.failed'`)

* `TRIGGER_DOT_CREATED` (value: `'trigger.created'`)

* `TRIGGER_DOT_UPDATED` (value: `'trigger.updated'`)

* `TRIGGER_DOT_DELETED` (value: `'trigger.deleted'`)

* `TRIGGER_DOT_PAUSED` (value: `'trigger.paused'`)

* `TRIGGER_DOT_RESUMED` (value: `'trigger.resumed'`)

* `TRIGGER_DOT_FIRED` (value: `'trigger.fired'`)

* `TRIGGER_DOT_EXECUTION_DOT_COMPLETED` (value: `'trigger.execution.completed'`)

* `TRIGGER_DOT_EXECUTION_DOT_FAILED` (value: `'trigger.execution.failed'`)

* `TAXONOMY_DOT_CREATED` (value: `'taxonomy.created'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


