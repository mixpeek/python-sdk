from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.storage_connection_test_response_details_type_0 import StorageConnectionTestResponseDetailsType0


T = TypeVar("T", bound="StorageConnectionTestResponse")


@_attrs_define
class StorageConnectionTestResponse:
    """Response payload for connection test endpoint.

    Returns the result of testing connection credentials against the external
    provider. Used to validate credentials before saving or to diagnose issues.

        Attributes:
            success (bool): Whether the connection test succeeded. True: Credentials are valid and connection is accessible.
                False: Authentication failed, network error, or permissions denied.
            message (str): Human-readable message describing the test result. Success: 'Connection test succeeded' or
                similar. Failure: Error message explaining what went wrong.
            details (None | StorageConnectionTestResponseDetailsType0 | Unset): OPTIONAL. Additional diagnostic information
                about the test result. May include error details, provider-specific information, or success metadata. Format
                varies by provider.
    """

    success: bool
    message: str
    details: None | StorageConnectionTestResponseDetailsType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.storage_connection_test_response_details_type_0 import StorageConnectionTestResponseDetailsType0

        success = self.success

        message = self.message

        details: dict[str, Any] | None | Unset
        if isinstance(self.details, Unset):
            details = UNSET
        elif isinstance(self.details, StorageConnectionTestResponseDetailsType0):
            details = self.details.to_dict()
        else:
            details = self.details

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "message": message,
            }
        )
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.storage_connection_test_response_details_type_0 import StorageConnectionTestResponseDetailsType0

        d = dict(src_dict)
        success = d.pop("success")

        message = d.pop("message")

        def _parse_details(data: object) -> None | StorageConnectionTestResponseDetailsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                details_type_0 = StorageConnectionTestResponseDetailsType0.from_dict(data)

                return details_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | StorageConnectionTestResponseDetailsType0 | Unset, data)

        details = _parse_details(d.pop("details", UNSET))

        storage_connection_test_response = cls(
            success=success,
            message=message,
            details=details,
        )

        storage_connection_test_response.additional_properties = d
        return storage_connection_test_response

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
