# WebhookEventType

Webhook event types for real-time notifications.  These events are emitted when significant state changes occur in the system. Webhooks subscribe to specific event types and receive notifications via configured channels (email, Slack, HTTP webhooks, SMS).  Event Naming Convention:     {resource}.{action}[.{sub-resource}[.{sub-action}]]  Examples:     - object.created: New object ingested     - collection.documents.written: Documents indexed     - cluster.execution.completed: Cluster job finished  Cache Invalidation Annotations:     Each event type includes a comment indicating recommended cache invalidation scope:     - [KEY] = Invalidate specific document/object keys     - [COLLECTION] = Invalidate collection-level cache     - [NAMESPACE] = Invalidate namespace-level cache  Event Categories:     - Object Lifecycle: Events for individual objects (create, update, delete)     - Collection Lifecycle: Events for collections (create, update, delete, documents written)     - Cluster Lifecycle: Events for clusters (create, update, delete, execution status)     - Trigger Lifecycle: Events for cluster triggers (create, update, fire, execution status)     - Taxonomy Lifecycle: Events for taxonomies (create, update, delete)  Use Cases:     - Real-time sync with external systems     - Audit trail and compliance logging     - Automated workflows triggered by state changes     - Cache invalidation for distributed systems     - Notifications to team members via Slack/email

## Enum

* `OBJECT_DOT_CREATED` (value: `'object.created'`)

* `OBJECTS_DOT_CREATED_DOT_BATCH` (value: `'objects.created.batch'`)

* `OBJECT_DOT_UPDATED` (value: `'object.updated'`)

* `OBJECT_DOT_DELETED` (value: `'object.deleted'`)

* `COLLECTION_DOT_CREATED` (value: `'collection.created'`)

* `COLLECTION_DOT_UPDATED` (value: `'collection.updated'`)

* `COLLECTION_DOT_DELETED` (value: `'collection.deleted'`)

* `COLLECTION_DOT_DOCUMENTS_DOT_WRITTEN` (value: `'collection.documents.written'`)

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


