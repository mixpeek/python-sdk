from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.task_status_enum import TaskStatusEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.task_response import TaskResponse


T = TypeVar("T", bound="BatchConfirmResponse")


@_attrs_define
class BatchConfirmResponse:
    """Response from batch confirmation.

    Attributes:
        task_id (str): Task ID for tracking batch confirmation progress
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
        confirmations_count (int): Number of confirmations being processed
        task (TaskResponse): Task response model returned by the API.

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
        message (str | Unset): Status message Default: 'Batch confirmation is being processed in the background.'.
    """

    task_id: str
    status: TaskStatusEnum
    confirmations_count: int
    task: TaskResponse
    message: str | Unset = "Batch confirmation is being processed in the background."
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        task_id = self.task_id

        status = self.status.value

        confirmations_count = self.confirmations_count

        task = self.task.to_dict()

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "task_id": task_id,
                "status": status,
                "confirmations_count": confirmations_count,
                "task": task,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.task_response import TaskResponse

        d = dict(src_dict)
        task_id = d.pop("task_id")

        status = TaskStatusEnum(d.pop("status"))

        confirmations_count = d.pop("confirmations_count")

        task = TaskResponse.from_dict(d.pop("task"))

        message = d.pop("message", UNSET)

        batch_confirm_response = cls(
            task_id=task_id,
            status=status,
            confirmations_count=confirmations_count,
            task=task,
            message=message,
        )

        batch_confirm_response.additional_properties = d
        return batch_confirm_response

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
