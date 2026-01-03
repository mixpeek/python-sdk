# AuditAction

Canonical audit log actions captured for organization events.  These events are written to the audit trail for compliance, security monitoring, and debugging. Each action includes actor, resource, timestamp, and change details.  User lifecycle actions:     - USER_CREATED: New user added to organization     - USER_UPDATED: User role, status, or metadata modified     - USER_DELETED: User removed from organization  API key lifecycle actions:     - API_KEY_CREATED: New API key generated     - API_KEY_ROTATED: Key regenerated (old key revoked, new key issued)     - API_KEY_REVOKED: Key manually revoked     - API_KEY_SCOPE_UPDATED: Key permissions or scopes modified  Permission actions:     - PERMISSION_UPDATED: User or key permissions modified  Storage connection actions:     - STORAGE_CONNECTION_CREATED: New external storage connection configured     - STORAGE_CONNECTION_UPDATED: Connection settings or credentials updated     - STORAGE_CONNECTION_DELETED: Connection permanently removed     - STORAGE_CONNECTION_TESTED: Connection health check performed     - STORAGE_CONNECTION_FAILED: Connection health check or sync failed  Namespace actions:     - NAMESPACE_CREATED: New namespace created     - NAMESPACE_UPDATED: Namespace configuration modified     - NAMESPACE_DELETED: Namespace permanently removed     - NAMESPACE_ACCESSED: Namespace read (when read auditing enabled)  Collection actions:     - COLLECTION_CREATED: New collection created     - COLLECTION_UPDATED: Collection configuration modified     - COLLECTION_DELETED: Collection permanently removed     - COLLECTION_ACCESSED: Collection read (when read auditing enabled)  Bucket actions:     - BUCKET_CREATED: New bucket created     - BUCKET_UPDATED: Bucket configuration modified     - BUCKET_DELETED: Bucket permanently removed     - BUCKET_ACCESSED: Bucket read (when read auditing enabled)  Retriever actions:     - RETRIEVER_CREATED: New retriever pipeline created     - RETRIEVER_UPDATED: Retriever configuration modified     - RETRIEVER_DELETED: Retriever permanently removed     - RETRIEVER_ACCESSED: Retriever read (when read auditing enabled)     - RETRIEVER_QUERIED: Retriever query executed (when read auditing enabled)  Cluster actions:     - CLUSTER_CREATED: New cluster created     - CLUSTER_UPDATED: Cluster configuration modified     - CLUSTER_DELETED: Cluster permanently removed     - CLUSTER_EXECUTED: Cluster job executed     - CLUSTER_ACCESSED: Cluster read (when read auditing enabled)  Taxonomy actions:     - TAXONOMY_CREATED: New taxonomy created     - TAXONOMY_UPDATED: Taxonomy configuration modified     - TAXONOMY_DELETED: Taxonomy permanently removed     - TAXONOMY_ACCESSED: Taxonomy read (when read auditing enabled)

## Enum

* `USER_CREATED` (value: `'user_created'`)

* `USER_UPDATED` (value: `'user_updated'`)

* `USER_DELETED` (value: `'user_deleted'`)

* `API_KEY_CREATED` (value: `'api_key_created'`)

* `API_KEY_ROTATED` (value: `'api_key_rotated'`)

* `API_KEY_REVOKED` (value: `'api_key_revoked'`)

* `API_KEY_SCOPE_UPDATED` (value: `'api_key_scope_updated'`)

* `PERMISSION_UPDATED` (value: `'permission_updated'`)

* `STORAGE_CONNECTION_CREATED` (value: `'storage_connection_created'`)

* `STORAGE_CONNECTION_UPDATED` (value: `'storage_connection_updated'`)

* `STORAGE_CONNECTION_DELETED` (value: `'storage_connection_deleted'`)

* `STORAGE_CONNECTION_TESTED` (value: `'storage_connection_tested'`)

* `STORAGE_CONNECTION_FAILED` (value: `'storage_connection_failed'`)

* `NAMESPACE_CREATED` (value: `'namespace_created'`)

* `NAMESPACE_UPDATED` (value: `'namespace_updated'`)

* `NAMESPACE_DELETED` (value: `'namespace_deleted'`)

* `NAMESPACE_ACCESSED` (value: `'namespace_accessed'`)

* `COLLECTION_CREATED` (value: `'collection_created'`)

* `COLLECTION_UPDATED` (value: `'collection_updated'`)

* `COLLECTION_DELETED` (value: `'collection_deleted'`)

* `COLLECTION_ACCESSED` (value: `'collection_accessed'`)

* `BUCKET_CREATED` (value: `'bucket_created'`)

* `BUCKET_UPDATED` (value: `'bucket_updated'`)

* `BUCKET_DELETED` (value: `'bucket_deleted'`)

* `BUCKET_ACCESSED` (value: `'bucket_accessed'`)

* `RETRIEVER_CREATED` (value: `'retriever_created'`)

* `RETRIEVER_UPDATED` (value: `'retriever_updated'`)

* `RETRIEVER_DELETED` (value: `'retriever_deleted'`)

* `RETRIEVER_ACCESSED` (value: `'retriever_accessed'`)

* `RETRIEVER_QUERIED` (value: `'retriever_queried'`)

* `CLUSTER_CREATED` (value: `'cluster_created'`)

* `CLUSTER_UPDATED` (value: `'cluster_updated'`)

* `CLUSTER_DELETED` (value: `'cluster_deleted'`)

* `CLUSTER_EXECUTED` (value: `'cluster_executed'`)

* `CLUSTER_ACCESSED` (value: `'cluster_accessed'`)

* `TAXONOMY_CREATED` (value: `'taxonomy_created'`)

* `TAXONOMY_UPDATED` (value: `'taxonomy_updated'`)

* `TAXONOMY_DELETED` (value: `'taxonomy_deleted'`)

* `TAXONOMY_ACCESSED` (value: `'taxonomy_accessed'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


