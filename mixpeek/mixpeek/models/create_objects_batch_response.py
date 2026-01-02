from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.failed_object_error import FailedObjectError
    from ..models.object_response import ObjectResponse


T = TypeVar("T", bound="CreateObjectsBatchResponse")


@_attrs_define
class CreateObjectsBatchResponse:
    """Response model for batch object creation with partial success support.

    This endpoint uses partial success: valid objects are created even if some fail.
    Failed objects are tracked separately so users can fix and retry them.

        Attributes:
            succeeded (list[ObjectResponse]): List of successfully created objects
            failed (list[FailedObjectError]): List of objects that failed to create with error details
            total_requested (int): Total number of objects in the batch request
            succeeded_count (int): Number of objects successfully created
            failed_count (int): Number of objects that failed
    """

    succeeded: list[ObjectResponse]
    failed: list[FailedObjectError]
    total_requested: int
    succeeded_count: int
    failed_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        succeeded = []
        for succeeded_item_data in self.succeeded:
            succeeded_item = succeeded_item_data.to_dict()
            succeeded.append(succeeded_item)

        failed = []
        for failed_item_data in self.failed:
            failed_item = failed_item_data.to_dict()
            failed.append(failed_item)

        total_requested = self.total_requested

        succeeded_count = self.succeeded_count

        failed_count = self.failed_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "succeeded": succeeded,
                "failed": failed,
                "total_requested": total_requested,
                "succeeded_count": succeeded_count,
                "failed_count": failed_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.failed_object_error import FailedObjectError
        from ..models.object_response import ObjectResponse

        d = dict(src_dict)
        succeeded = []
        _succeeded = d.pop("succeeded")
        for succeeded_item_data in _succeeded:
            succeeded_item = ObjectResponse.from_dict(succeeded_item_data)

            succeeded.append(succeeded_item)

        failed = []
        _failed = d.pop("failed")
        for failed_item_data in _failed:
            failed_item = FailedObjectError.from_dict(failed_item_data)

            failed.append(failed_item)

        total_requested = d.pop("total_requested")

        succeeded_count = d.pop("succeeded_count")

        failed_count = d.pop("failed_count")

        create_objects_batch_response = cls(
            succeeded=succeeded,
            failed=failed,
            total_requested=total_requested,
            succeeded_count=succeeded_count,
            failed_count=failed_count,
        )

        create_objects_batch_response.additional_properties = d
        return create_objects_batch_response

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
