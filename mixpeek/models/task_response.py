from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.task_status_enum import TaskStatusEnum
from ..models.task_type import TaskType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.task_response_additional_data_type_0 import TaskResponseAdditionalDataType0
    from ..models.task_response_inputs_type_0_item_type_1 import TaskResponseInputsType0ItemType1
    from ..models.task_response_outputs_type_0_item_type_1 import TaskResponseOutputsType0ItemType1


T = TypeVar("T", bound="TaskResponse")


@_attrs_define
class TaskResponse:
    """Task response model returned by the API.

    Extends TaskModel with additional convenience fields for API responses.
    This is the model returned when you GET /v1/tasks/{task_id}.

    Additional Fields:
        error_message: Convenience field that surfaces errors from additional_data
                      for easier error handling in client code.

    Inheritance:
        Inherits all fields and documentation from TaskModel, including:
        - task_id: Unique identifier
        - task_type: Operation type
        - status: Current status
        - inputs: Input parameters
        - outputs: Output results
        - additional_data: Metadata and context

    Storage Architecture:
        Same as TaskModel - stored in Redis (24hr TTL) with MongoDB fallback.

    Usage:
        This model is automatically returned by task API endpoints. You don't
        need to construct it manually - just call GET /v1/tasks/{task_id}.

    Error Handling:
        Check the error_message field for a user-friendly error string, or
        additional_data['error'] for the full error details.

    Example Response:
        {
            "task_id": "task_abc123",
            "task_type": "api_buckets_batches_process",
            "status": "FAILED",
            "inputs": ["batch_xyz"],
            "outputs": null,
            "additional_data": {
                "error": "Failed to process batch: Object not found",
                "batch_id": "batch_xyz"
            },
            "error_message": "Failed to process batch: Object not found"
        }

        Attributes:
            task_id (str): Unique identifier for the task. REQUIRED. Used to poll task status via GET /v1/tasks/{task_id}.
                This ID is also stored on parent resources (batches, clusters, etc.) for cross-referencing. Format: UUID v4 or
                custom string identifier.
            task_type (TaskType): Types of asynchronous tasks that can be performed in the system.

                Task types identify the specific operation being performed. This helps with
                tracking, debugging, and filtering tasks by operation type.

                Categories:
                    API Tasks: User-initiated operations via API endpoints
                    Engine Tasks: Background processing tasks
                    Inference Tasks: Specialized inference operations

                API Task Types:
                    API_NAMESPACES_CREATE: Creating a new namespace
                    API_NAMESPACES_MIGRATIONS_RUN: Running a namespace migration
                    API_BUCKETS_OBJECTS_CREATE: Creating objects in a bucket
                    API_BUCKETS_DELETE: Deleting a bucket and its contents
                    API_BUCKETS_BATCHES_PROCESS: Processing a batch of objects
                    API_BUCKETS_BATCHES_SUBMIT: Submitting a batch for processing
                    API_BUCKETS_UPLOADS_CREATE: Creating an upload session
                    API_BUCKETS_UPLOADS_CONFIRM: Confirming an upload completion
                    API_BUCKETS_UPLOADS_BATCH_CONFIRM: Confirming batch upload completion
                    API_TAXONOMIES_CREATE: Creating a new taxonomy
                    API_TAXONOMIES_EXECUTE: Executing taxonomy classification
                    API_TAXONOMIES_MATERIALIZE: Materializing taxonomy results
                    API_RETRIEVERS_PUBLISH: Publishing retriever assets (OG images, etc.)

                Engine Task Types:
                    ENGINE_FEATURE_EXTRACTOR_RUN: Running feature extraction on data
                    ENGINE_INFERENCE_RUN: Running inference operations
                    ENGINE_OBJECT_PROCESSING: Processing object data
                    ENGINE_CLUSTER_BUILD: Building clusters from data

                Inference Task Types:
                    THUMBNAIL: Generating thumbnails
                    MATERIALIZE: Materializing processed data

                Usage:
                    Task types are automatically assigned when tasks are created. You can
                    filter tasks by type when listing or searching for specific operations.
            status (TaskStatusEnum): Enumeration of task statuses for tracking asynchronous operations.

                Task statuses indicate the current state of asynchronous operations like
                batch processing, object ingestion, clustering, and taxonomy execution.

                Status Categories:
                    Operation Statuses: Track progress of async operations
                    Lifecycle Statuses: Track entity state (buckets, collections, namespaces)

                Values:
                    PENDING: Task is queued but has not started processing yet
                    IN_PROGRESS: Task is currently being executed
                    PROCESSING: Task is actively processing data (similar to IN_PROGRESS)
                    COMPLETED: Task finished successfully with no errors
                    COMPLETED_WITH_ERRORS: Task finished but some items failed (partial success)
                    FAILED: Task encountered an error and could not complete
                    CANCELED: Task was manually canceled by a user or system
                    UNKNOWN: Task status could not be determined
                    SKIPPED: Task was intentionally skipped
                    DRAFT: Task is in draft state and not yet submitted

                    ACTIVE: Entity is active and operational (for buckets, collections, etc.)
                    ARCHIVED: Entity has been archived
                    SUSPENDED: Entity has been temporarily suspended

                Terminal Statuses:
                    COMPLETED, COMPLETED_WITH_ERRORS, FAILED, CANCELED are terminal statuses.
                    Once a task reaches these states, it will not transition to another state.

                Partial Success Handling:
                    COMPLETED_WITH_ERRORS indicates that the operation completed but some
                    documents/items failed. The task result includes:
                    - List of successful items
                    - List of failed items with error details
                    - Success rate percentage
                    This allows clients to handle partial success scenarios appropriately.

                Polling Guidance:
                    - Poll tasks in PENDING, IN_PROGRESS, or PROCESSING states
                    - Stop polling when task reaches COMPLETED, COMPLETED_WITH_ERRORS, FAILED, or CANCELED
                    - Use exponential backoff (1s → 30s) when polling
            inputs (list[str | TaskResponseInputsType0ItemType1] | None | Unset): Input parameters or data used to start the
                task. OPTIONAL. May include IDs, configuration objects, or file references. Useful for debugging and
                understanding what data the task processed. Format: List of strings (IDs) or objects (configuration). Example:
                ['batch_id_123'] or [{'bucket_id': 'bkt_abc', 'config': {...}}]
            outputs (list[str | TaskResponseOutputsType0ItemType1] | None | Unset): Output results produced by the task.
                OPTIONAL. Populated when task completes successfully. May include processed file IDs, result metrics, or status
                summaries. Check this field after task reaches COMPLETED status to get results. Format: List of strings (output
                IDs) or objects (result data).
            additional_data (None | TaskResponseAdditionalDataType0 | Unset): Additional metadata and context for the task.
                OPTIONAL. Contains job IDs, error details, progress info, and other task-specific metadata.

                Common fields (all task types): - 'error': Error message if task failed - 'job_id': Ray job ID for engine tasks
                - 'from_mongodb': True if retrieved from MongoDB fallback (not Redis)

                Batch-specific fields (task_type=api_buckets_batches_process): - 'batch_id': Batch identifier (REQUIRED) -
                'bucket_id': Source bucket identifier (REQUIRED) - 'namespace_id': Namespace identifier (REQUIRED) -
                'current_tier': Currently processing tier number, 0-indexed (OPTIONAL, None if not started) - 'total_tiers':
                Total number of tiers in the batch pipeline (REQUIRED) - 'collection_ids': Array of ALL collection IDs across
                all tiers (REQUIRED) - 'object_count': Number of objects being processed (REQUIRED) - 'sample_object_ids': First
                5 object IDs for debugging/display (OPTIONAL)

                Performance Note: Full object_ids array is NOT stored in task metadata to avoid bloating task documents (batches
                with 10k+ objects would add 200KB+ per task). For full object list, query the batch directly via GET
                /v1/buckets/{bucket_id}/batches/{batch_id}.

                Note: For detailed per-tier status, use GET /v1/buckets/{bucket_id}/batches/{batch_id} to access the
                tier_tasks[] array which contains individual tier statuses, collection_ids, and timestamps for each tier.
            error (None | str | Unset): Flattened error message for convenient error handling. OPTIONAL. Automatically
                populated from additional_data['error'] when the task has FAILED status. This is a convenience field - the full
                error details are always available in additional_data['error']. Use this field for displaying errors to users or
                logging. Will be None if task has not failed or if no error details are available. Serialized as 'error' in API
                responses for backward compatibility.
    """

    task_id: str
    task_type: TaskType
    status: TaskStatusEnum
    inputs: list[str | TaskResponseInputsType0ItemType1] | None | Unset = UNSET
    outputs: list[str | TaskResponseOutputsType0ItemType1] | None | Unset = UNSET
    additional_data: None | TaskResponseAdditionalDataType0 | Unset = UNSET
    error: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.task_response_additional_data_type_0 import TaskResponseAdditionalDataType0
        from ..models.task_response_inputs_type_0_item_type_1 import TaskResponseInputsType0ItemType1
        from ..models.task_response_outputs_type_0_item_type_1 import TaskResponseOutputsType0ItemType1

        task_id = self.task_id

        task_type = self.task_type.value

        status = self.status.value

        inputs: list[dict[str, Any] | str] | None | Unset
        if isinstance(self.inputs, Unset):
            inputs = UNSET
        elif isinstance(self.inputs, list):
            inputs = []
            for inputs_type_0_item_data in self.inputs:
                inputs_type_0_item: dict[str, Any] | str
                if isinstance(inputs_type_0_item_data, TaskResponseInputsType0ItemType1):
                    inputs_type_0_item = inputs_type_0_item_data.to_dict()
                else:
                    inputs_type_0_item = inputs_type_0_item_data
                inputs.append(inputs_type_0_item)

        else:
            inputs = self.inputs

        outputs: list[dict[str, Any] | str] | None | Unset
        if isinstance(self.outputs, Unset):
            outputs = UNSET
        elif isinstance(self.outputs, list):
            outputs = []
            for outputs_type_0_item_data in self.outputs:
                outputs_type_0_item: dict[str, Any] | str
                if isinstance(outputs_type_0_item_data, TaskResponseOutputsType0ItemType1):
                    outputs_type_0_item = outputs_type_0_item_data.to_dict()
                else:
                    outputs_type_0_item = outputs_type_0_item_data
                outputs.append(outputs_type_0_item)

        else:
            outputs = self.outputs

        additional_data: dict[str, Any] | None | Unset
        if isinstance(self.additional_data, Unset):
            additional_data = UNSET
        elif isinstance(self.additional_data, TaskResponseAdditionalDataType0):
            additional_data = self.additional_data.to_dict()
        else:
            additional_data = self.additional_data

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "task_id": task_id,
                "task_type": task_type,
                "status": status,
            }
        )
        if inputs is not UNSET:
            field_dict["inputs"] = inputs
        if outputs is not UNSET:
            field_dict["outputs"] = outputs
        if additional_data is not UNSET:
            field_dict["additional_data"] = additional_data
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.task_response_additional_data_type_0 import TaskResponseAdditionalDataType0
        from ..models.task_response_inputs_type_0_item_type_1 import TaskResponseInputsType0ItemType1
        from ..models.task_response_outputs_type_0_item_type_1 import TaskResponseOutputsType0ItemType1

        d = dict(src_dict)
        task_id = d.pop("task_id")

        task_type = TaskType(d.pop("task_type"))

        status = TaskStatusEnum(d.pop("status"))

        def _parse_inputs(data: object) -> list[str | TaskResponseInputsType0ItemType1] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                inputs_type_0 = []
                _inputs_type_0 = data
                for inputs_type_0_item_data in _inputs_type_0:

                    def _parse_inputs_type_0_item(data: object) -> str | TaskResponseInputsType0ItemType1:
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            inputs_type_0_item_type_1 = TaskResponseInputsType0ItemType1.from_dict(data)

                            return inputs_type_0_item_type_1
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(str | TaskResponseInputsType0ItemType1, data)

                    inputs_type_0_item = _parse_inputs_type_0_item(inputs_type_0_item_data)

                    inputs_type_0.append(inputs_type_0_item)

                return inputs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str | TaskResponseInputsType0ItemType1] | None | Unset, data)

        inputs = _parse_inputs(d.pop("inputs", UNSET))

        def _parse_outputs(data: object) -> list[str | TaskResponseOutputsType0ItemType1] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                outputs_type_0 = []
                _outputs_type_0 = data
                for outputs_type_0_item_data in _outputs_type_0:

                    def _parse_outputs_type_0_item(data: object) -> str | TaskResponseOutputsType0ItemType1:
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            outputs_type_0_item_type_1 = TaskResponseOutputsType0ItemType1.from_dict(data)

                            return outputs_type_0_item_type_1
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(str | TaskResponseOutputsType0ItemType1, data)

                    outputs_type_0_item = _parse_outputs_type_0_item(outputs_type_0_item_data)

                    outputs_type_0.append(outputs_type_0_item)

                return outputs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str | TaskResponseOutputsType0ItemType1] | None | Unset, data)

        outputs = _parse_outputs(d.pop("outputs", UNSET))

        def _parse_additional_data(data: object) -> None | TaskResponseAdditionalDataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                additional_data_type_0 = TaskResponseAdditionalDataType0.from_dict(data)

                return additional_data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TaskResponseAdditionalDataType0 | Unset, data)

        additional_data = _parse_additional_data(d.pop("additional_data", UNSET))

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        task_response = cls(
            task_id=task_id,
            task_type=task_type,
            status=status,
            inputs=inputs,
            outputs=outputs,
            additional_data=additional_data,
            error=error,
        )

        task_response.additional_properties = d
        return task_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
