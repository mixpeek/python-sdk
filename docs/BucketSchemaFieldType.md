# BucketSchemaFieldType

Supported data types for bucket schema fields.  Types fall into two categories:  1. **Metadata Types** (JSON types):    - Stored as object metadata    - Standard JSON-compatible types    - Not processed by extractors (unless explicitly mapped)    - Examples: string, number, boolean, date  2. **File Types** (blobs):    - Stored as files/blobs    - Processed by extractors    - Require file content (URL or base64)    - Examples: text, image, video, pdf  **GIF Special Handling**:     GIF files can be declared as either IMAGE or VIDEO type:      - As IMAGE: GIF is embedded as a single static image (first frame)     - As VIDEO: GIF is decomposed frame-by-frame with embeddings per frame      The multimodal extractor detects GIFs via MIME type (image/gif) and routes     them based on your schema declaration. Use VIDEO for animated GIFs where     frame-level search is needed, IMAGE for static/thumbnail use cases.  NOTE: For retriever input schemas that need to accept document references (e.g., \"find similar documents\"), use RetrieverInputSchemaFieldType instead, which includes all bucket types plus document_reference.

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

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


