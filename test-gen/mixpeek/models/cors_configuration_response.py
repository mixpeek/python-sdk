from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.cors_configuration_response_applied_configuration import CORSConfigurationResponseAppliedConfiguration


T = TypeVar("T", bound="CORSConfigurationResponse")


@_attrs_define
class CORSConfigurationResponse:
    """Response model for CORS configuration operations.

    Attributes:
        success (bool): Whether the CORS configuration was successful
        bucket (str): The object storage bucket name where CORS was configured
        applied_configuration (CORSConfigurationResponseAppliedConfiguration): The CORS configuration that was applied
            to the bucket
        message (str): Human-readable status message
    """

    success: bool
    bucket: str
    applied_configuration: CORSConfigurationResponseAppliedConfiguration
    message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        bucket = self.bucket

        applied_configuration = self.applied_configuration.to_dict()

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "bucket": bucket,
                "applied_configuration": applied_configuration,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cors_configuration_response_applied_configuration import (
            CORSConfigurationResponseAppliedConfiguration,
        )

        d = dict(src_dict)
        success = d.pop("success")

        bucket = d.pop("bucket")

        applied_configuration = CORSConfigurationResponseAppliedConfiguration.from_dict(d.pop("applied_configuration"))

        message = d.pop("message")

        cors_configuration_response = cls(
            success=success,
            bucket=bucket,
            applied_configuration=applied_configuration,
            message=message,
        )

        cors_configuration_response.additional_properties = d
        return cors_configuration_response

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
