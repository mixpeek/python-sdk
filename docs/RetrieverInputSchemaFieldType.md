# RetrieverInputSchemaFieldType

Supported data types for retriever input schema fields.  Retriever input schemas define what parameters users can provide when executing a retriever. This includes all bucket schema types plus additional reference types.  Types fall into three categories:  1. **Metadata Types** (JSON types):    - Standard JSON-compatible types    - Examples: string, number, boolean, date    - Inherited from BucketSchemaFieldType  2. **File Types** (blobs):    - Users can upload files/content as search inputs    - Examples: text, image, video, pdf    - Inherited from BucketSchemaFieldType  3. **Reference Types** (structured metadata):    - Special types for referencing existing documents    - Examples: document_reference    - Only available in retriever input schemas (NOT in bucket schemas)  **DOCUMENT_REFERENCE Usage**:     Accept document reference for \"find similar\" queries.      Example - Find similar products retriever:     {         \"reference_product\": {             \"type\": \"document_reference\",             \"description\": \"Find products similar to this one\",             \"required\": true         }     }      Execution input:     {         \"inputs\": {             \"reference_product\": {                 \"collection_id\": \"col_products\",                 \"document_id\": \"doc_item_123\"             }         }     }      The system will use the pre-computed features from doc_item_123     to find similar documents without re-processing.

## Enum

* `STRING` (value: `'string'`)

* `NUMBER` (value: `'number'`)

* `INTEGER` (value: `'integer'`)

* `FLOAT` (value: `'float'`)

* `BOOLEAN` (value: `'boolean'`)

* `OBJECT` (value: `'object'`)

* `ARRAY` (value: `'array'`)

* `DATE` (value: `'date'`)

* `DATETIME` (value: `'datetime'`)

* `TEXT` (value: `'text'`)

* `IMAGE` (value: `'image'`)

* `AUDIO` (value: `'audio'`)

* `VIDEO` (value: `'video'`)

* `PDF` (value: `'pdf'`)

* `EXCEL` (value: `'excel'`)

* `DOCUMENT_REFERENCE` (value: `'document_reference'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


