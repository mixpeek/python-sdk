# BlobType

Type of blob content for schema mapping.  Determines how the blob content is processed and what extractors can operate on it. This is critical for the extraction pipeline to route content correctly.  Values:     auto: Automatically infer blob type from mime_type (recommended for files)     image: Image files (JPEG, PNG, WebP, BMP, TIFF, or GIF as static)     video: Video files (MP4, MOV, WebM, AVI, MKV, or GIF as animated frames)     audio: Audio files (MP3, WAV, FLAC, AAC, OGG)     text: Text files (TXT, MD, HTML, XML)     pdf: PDF documents     excel: Spreadsheet files (XLSX, XLS, CSV)  **GIF Special Handling**:     GIF files are unique - they can be processed as either IMAGE or VIDEO:      - As IMAGE: Single static embedding (first frame), no decomposition     - As VIDEO: Frame-by-frame decomposition with per-frame embeddings      When using \"auto\", GIFs default to IMAGE. To get frame-level processing     for animated GIFs, explicitly set blob_type to VIDEO.  Usage Guidelines:     - Use \"auto\" when syncing files with accurate mime_type headers     - Use explicit types when mime_type is missing or unreliable     - Use \"video\" for animated GIFs requiring frame-level search

## Enum

* `AUTO` (value: `'auto'`)

* `IMAGE` (value: `'image'`)

* `VIDEO` (value: `'video'`)

* `AUDIO` (value: `'audio'`)

* `TEXT` (value: `'text'`)

* `PDF` (value: `'pdf'`)

* `EXCEL` (value: `'excel'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


