from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_detail_details_type_0 import ErrorDetailDetailsType0


T = TypeVar("T", bound="ErrorDetail")


@_attrs_define
class ErrorDetail:
    """Error detail model.

    Attributes:
        message (str): Human-readable error message
        type_ (str): Stable error type identifier (machine-readable)
        details (ErrorDetailDetailsType0 | None | Unset): Optional structured details to help debugging (validation
            errors, IDs, etc.)
    """

    message: str
    type_: str
    details: ErrorDetailDetailsType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.error_detail_details_type_0 import ErrorDetailDetailsType0

        message = self.message

        type_ = self.type_

        details: dict[str, Any] | None | Unset
        if isinstance(self.details, Unset):
            details = UNSET
        elif isinstance(self.details, ErrorDetailDetailsType0):
            details = self.details.to_dict()
        else:
            details = self.details

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
                "type": type_,
            }
        )
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error_detail_details_type_0 import ErrorDetailDetailsType0

        d = dict(src_dict)
        message = d.pop("message")

        type_ = d.pop("type")

        def _parse_details(data: object) -> ErrorDetailDetailsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                details_type_0 = ErrorDetailDetailsType0.from_dict(data)

                return details_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ErrorDetailDetailsType0 | None | Unset, data)

        details = _parse_details(d.pop("details", UNSET))

        error_detail = cls(
            message=message,
            type_=type_,
            details=details,
        )

        error_detail.additional_properties = d
        return error_detail

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
