# TaskType

Types of asynchronous tasks that can be performed in the system.  Task types identify the specific operation being performed. This helps with tracking, debugging, and filtering tasks by operation type.  Categories:     API Tasks: User-initiated operations via API endpoints     Engine Tasks: Background processing tasks     Inference Tasks: Specialized inference operations  API Task Types:     API_NAMESPACES_CREATE: Creating a new namespace     API_NAMESPACES_MIGRATIONS_RUN: Running a namespace migration     API_BUCKETS_OBJECTS_CREATE: Creating objects in a bucket     API_BUCKETS_DELETE: Deleting a bucket and its contents     API_BUCKETS_BATCHES_PROCESS: Processing a batch of objects     API_BUCKETS_BATCHES_SUBMIT: Submitting a batch for processing     API_BUCKETS_UPLOADS_CREATE: Creating an upload session     API_BUCKETS_UPLOADS_CONFIRM: Confirming an upload completion     API_BUCKETS_UPLOADS_BATCH_CONFIRM: Confirming batch upload completion     API_TAXONOMIES_CREATE: Creating a new taxonomy     API_TAXONOMIES_EXECUTE: Executing taxonomy classification     API_TAXONOMIES_MATERIALIZE: Materializing taxonomy results     API_RETRIEVERS_PUBLISH: Publishing retriever assets (OG images, etc.)  Engine Task Types:     ENGINE_FEATURE_EXTRACTOR_RUN: Running feature extraction on data     ENGINE_INFERENCE_RUN: Running inference operations     ENGINE_OBJECT_PROCESSING: Processing object data     ENGINE_CLUSTER_BUILD: Building clusters from data  Inference Task Types:     THUMBNAIL: Generating thumbnails     MATERIALIZE: Materializing processed data  Usage:     Task types are automatically assigned when tasks are created. You can     filter tasks by type when listing or searching for specific operations.

## Enum

* `API_NAMESPACES_CREATE` (value: `'api_namespaces_create'`)

* `API_NAMESPACES_DELETE` (value: `'api_namespaces_delete'`)

* `API_NAMESPACES_MIGRATIONS_RUN` (value: `'api_namespaces_migrations_run'`)

* `API_BUCKETS_OBJECTS_CREATE` (value: `'api_buckets_objects_create'`)

* `API_BUCKETS_DELETE` (value: `'api_buckets_delete'`)

* `API_BUCKETS_BATCHES_PROCESS` (value: `'api_buckets_batches_process'`)

* `API_BUCKETS_BATCHES_SUBMIT` (value: `'api_buckets_batches_submit'`)

* `API_BUCKETS_UPLOADS_CREATE` (value: `'api_buckets_uploads_create'`)

* `API_BUCKETS_UPLOADS_CONFIRM` (value: `'api_buckets_uploads_confirm'`)

* `API_BUCKETS_UPLOADS_BATCH_CONFIRM` (value: `'api_buckets_uploads_batch_confirm'`)

* `API_COLLECTIONS_DOCUMENTS_CREATE` (value: `'api_collections_documents_create'`)

* `API_COLLECTIONS_EXTRACTION_ARTIFACTS` (value: `'api_collections_extraction_artifacts'`)

* `API_TAXONOMIES_CREATE` (value: `'api_taxonomies_create'`)

* `API_TAXONOMIES_EXECUTE` (value: `'api_taxonomies_execute'`)

* `API_TAXONOMIES_MATERIALIZE` (value: `'api_taxonomies_materialize'`)

* `API_EVALUATIONS_RUN` (value: `'api_evaluations_run'`)

* `API_EVALUATIONS_DATASET_CREATE` (value: `'api_evaluations_dataset_create'`)

* `API_RETRIEVERS_PUBLISH` (value: `'api_retrievers_publish'`)

* `API_COLLECTIONS_EXPORT` (value: `'api_collections_export'`)

* `ENGINE_FEATURE_EXTRACTOR_RUN` (value: `'engine_feature_extractor_run'`)

* `ENGINE_INFERENCE_RUN` (value: `'engine_inference_run'`)

* `ENGINE_OBJECT_PROCESSING` (value: `'engine_object_processing'`)

* `ENGINE_CLUSTER_BUILD` (value: `'engine_cluster_build'`)

* `THUMBNAIL` (value: `'thumbnail'`)

* `VIDEO_SEGMENT` (value: `'video_segment'`)

* `AUDIO_SEGMENT` (value: `'audio_segment'`)

* `MATERIALIZE` (value: `'materialize'`)

* `PLUGIN_CUSTOM` (value: `'plugin_custom'`)

* `MODEL_CUSTOM` (value: `'model_custom'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


