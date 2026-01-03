# NamespaceOperation

Granular operations that can be scoped inside a namespace.  These operations are used to define fine-grained permissions for API keys and users within specific namespaces. Operations can be granted individually or in combination to implement least-privilege access control.  Data operations:     - READ_DATA: View and search documents, retrieve objects from buckets     - WRITE_DATA: Create and update documents, upload objects to buckets     - DELETE_DATA: Remove documents and objects permanently  Retrieval operations:     - EXECUTE_RETRIEVER: Run search queries using configured retrievers     - CREATE_RETRIEVER: Define new retrieval pipelines with custom stages     - DELETE_RETRIEVER: Remove retrieval pipeline configurations  Job execution:     - EXECUTE_JOB: Trigger ingestion pipelines and batch processing jobs     - CANCEL_JOB: Abort running jobs before completion  Cluster management (Ray infrastructure):     - CREATE_CLUSTER: Provision new Ray compute clusters     - DELETE_CLUSTER: Tear down existing compute clusters     - MODIFY_CLUSTER: Scale or reconfigure running clusters  Infrastructure configuration:     - MODIFY_INFRASTRUCTURE: Change namespace settings, storage connections     - MANAGE_PERMISSIONS: Grant and revoke user access within the namespace  Examples:     - Read-only access: [READ_DATA, EXECUTE_RETRIEVER]     - Data engineer access: [READ_DATA, WRITE_DATA, EXECUTE_JOB]     - Full namespace admin: All operations granted

## Enum

* `READ_DATA` (value: `'read_data'`)

* `WRITE_DATA` (value: `'write_data'`)

* `DELETE_DATA` (value: `'delete_data'`)

* `EXECUTE_RETRIEVER` (value: `'execute_retriever'`)

* `CREATE_RETRIEVER` (value: `'create_retriever'`)

* `DELETE_RETRIEVER` (value: `'delete_retriever'`)

* `EXECUTE_JOB` (value: `'execute_job'`)

* `CANCEL_JOB` (value: `'cancel_job'`)

* `CREATE_CLUSTER` (value: `'create_cluster'`)

* `DELETE_CLUSTER` (value: `'delete_cluster'`)

* `MODIFY_CLUSTER` (value: `'modify_cluster'`)

* `MODIFY_INFRASTRUCTURE` (value: `'modify_infrastructure'`)

* `MANAGE_PERMISSIONS` (value: `'manage_permissions'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


