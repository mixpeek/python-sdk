from enum import Enum


class WebhookEventType(str, Enum):
    CLUSTER_CREATED = "cluster.created"
    CLUSTER_DELETED = "cluster.deleted"
    CLUSTER_EXECUTION_COMPLETED = "cluster.execution.completed"
    CLUSTER_EXECUTION_FAILED = "cluster.execution.failed"
    CLUSTER_EXECUTION_STARTED = "cluster.execution.started"
    CLUSTER_UPDATED = "cluster.updated"
    COLLECTION_CREATED = "collection.created"
    COLLECTION_DELETED = "collection.deleted"
    COLLECTION_DOCUMENTS_WRITTEN = "collection.documents.written"
    COLLECTION_UPDATED = "collection.updated"
    OBJECTS_CREATED_BATCH = "objects.created.batch"
    OBJECT_CREATED = "object.created"
    OBJECT_DELETED = "object.deleted"
    OBJECT_UPDATED = "object.updated"
    TAXONOMY_CREATED = "taxonomy.created"
    TRIGGER_CREATED = "trigger.created"
    TRIGGER_DELETED = "trigger.deleted"
    TRIGGER_EXECUTION_COMPLETED = "trigger.execution.completed"
    TRIGGER_EXECUTION_FAILED = "trigger.execution.failed"
    TRIGGER_FIRED = "trigger.fired"
    TRIGGER_PAUSED = "trigger.paused"
    TRIGGER_RESUMED = "trigger.resumed"
    TRIGGER_UPDATED = "trigger.updated"

    def __str__(self) -> str:
        return str(self.value)
