from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_detail import ErrorDetail


T = TypeVar("T", bound="ErrorResponse")


@_attrs_define
class ErrorResponse:
    """Error response model.

    Attributes:
        status (int): HTTP status code for this error
        error (ErrorDetail): Error detail model.
        success (bool | Unset): Always false for error responses Default: False.
    """

    status: int
    error: ErrorDetail
    success: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        error = self.error.to_dict()

        success = self.success

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "error": error,
            }
        )
        if success is not UNSET:
            field_dict["success"] = success

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error_detail import ErrorDetail

        d = dict(src_dict)
        status = d.pop("status")

        error = ErrorDetail.from_dict(d.pop("error"))

        success = d.pop("success", UNSET)

        error_response = cls(
            status=status,
            error=error,
            success=success,
        )

        error_response.additional_properties = d
        return error_response

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
