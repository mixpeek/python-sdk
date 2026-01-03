# TemplateMode

Mode of template instantiation.  scaffold: Create from pre-built preset     - Creates: namespace + bucket + collection + retriever     - Endpoint: POST /templates/scaffolds/{id}/instantiate     - All resources empty, ready for data  config: Copy resource configuration only     - Creates: empty resource with same settings     - Endpoint: POST /templates/{resource}/{id}/instantiate     - No data copied  clone: Copy resource with all data     - Creates: full copy including vectors/embeddings     - Endpoint: POST /namespaces/{id}/clone     - For config-only, use templates instead

## Enum

* `SCAFFOLD` (value: `'scaffold'`)

* `CONFIG` (value: `'config'`)

* `CLONE` (value: `'clone'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


