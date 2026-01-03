# SharedOrganizationsEnumsResourceType

Resource surfaces supported by scoped API keys and audit events.  These resource types can be used in: - API key scopes to restrict access to specific resources - Audit logs to identify what type of resource was affected - Permission systems to grant/deny access to resource categories  Resource hierarchy:     ORGANIZATION -> USER, API_KEY, STORAGE_CONNECTION     NAMESPACE -> COLLECTION, BUCKET, RETRIEVER, CLUSTER, TAXONOMY  Resource types:     - ORGANIZATION: Top-level tenant entity     - USER: Organization member with authentication credentials     - API_KEY: Authentication token for programmatic access     - NAMESPACE: Isolated environment for data and compute resources     - COLLECTION: Vector database collection for searchable documents     - BUCKET: Object storage container for raw files     - RETRIEVER: Configured search/retrieval pipeline     - CLUSTER: Ray compute cluster for distributed processing     - TAXONOMY: Hierarchical classification system for documents     - STORAGE_CONNECTION: External storage provider integration

## Enum

* `ORGANIZATION` (value: `'organization'`)

* `USER` (value: `'user'`)

* `API_KEY` (value: `'api_key'`)

* `NAMESPACE` (value: `'namespace'`)

* `COLLECTION` (value: `'collection'`)

* `BUCKET` (value: `'bucket'`)

* `RETRIEVER` (value: `'retriever'`)

* `CLUSTER` (value: `'cluster'`)

* `TAXONOMY` (value: `'taxonomy'`)

* `STORAGE_CONNECTION` (value: `'storage_connection'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


