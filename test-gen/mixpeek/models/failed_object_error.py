from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FailedObjectError")


@_attrs_define
class FailedObjectError:
    """Error details for a failed object in a batch.

    Attributes:
        object_index (int): 0-based index of the failed object in the batch request
        error (str): Error message describing why the object failed
        error_type (str): Type of error (e.g., 'ValidationError', 'URLValidationError')
    """

    object_index: int
    error: str
    error_type: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_index = self.object_index

        error = self.error

        error_type = self.error_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object_index": object_index,
                "error": error,
                "error_type": error_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        object_index = d.pop("object_index")

        error = d.pop("error")

        error_type = d.pop("error_type")

        failed_object_error = cls(
            object_index=object_index,
            error=error,
            error_type=error_type,
        )

        failed_object_error.additional_properties = d
        return failed_object_error

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
