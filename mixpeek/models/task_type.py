from enum import Enum


class TaskType(str, Enum):
    API_BUCKETS_BATCHES_PROCESS = "api_buckets_batches_process"
    API_BUCKETS_BATCHES_SUBMIT = "api_buckets_batches_submit"
    API_BUCKETS_DELETE = "api_buckets_delete"
    API_BUCKETS_OBJECTS_CREATE = "api_buckets_objects_create"
    API_BUCKETS_UPLOADS_BATCH_CONFIRM = "api_buckets_uploads_batch_confirm"
    API_BUCKETS_UPLOADS_CONFIRM = "api_buckets_uploads_confirm"
    API_BUCKETS_UPLOADS_CREATE = "api_buckets_uploads_create"
    API_COLLECTIONS_DOCUMENTS_CREATE = "api_collections_documents_create"
    API_COLLECTIONS_EXTRACTION_ARTIFACTS = "api_collections_extraction_artifacts"
    API_EVALUATIONS_DATASET_CREATE = "api_evaluations_dataset_create"
    API_EVALUATIONS_RUN = "api_evaluations_run"
    API_NAMESPACES_CREATE = "api_namespaces_create"
    API_NAMESPACES_DELETE = "api_namespaces_delete"
    API_NAMESPACES_MIGRATIONS_RUN = "api_namespaces_migrations_run"
    API_RETRIEVERS_PUBLISH = "api_retrievers_publish"
    API_TAXONOMIES_CREATE = "api_taxonomies_create"
    API_TAXONOMIES_EXECUTE = "api_taxonomies_execute"
    API_TAXONOMIES_MATERIALIZE = "api_taxonomies_materialize"
    AUDIO_SEGMENT = "audio_segment"
    ENGINE_CLUSTER_BUILD = "engine_cluster_build"
    ENGINE_FEATURE_EXTRACTOR_RUN = "engine_feature_extractor_run"
    ENGINE_INFERENCE_RUN = "engine_inference_run"
    ENGINE_OBJECT_PROCESSING = "engine_object_processing"
    MATERIALIZE = "materialize"
    THUMBNAIL = "thumbnail"
    VIDEO_SEGMENT = "video_segment"

    def __str__(self) -> str:
        return str(self.value)
