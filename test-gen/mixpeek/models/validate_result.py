from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.validate_result_resources import ValidateResultResources


T = TypeVar("T", bound="ValidateResult")


@_attrs_define
class ValidateResult:
    """Result of validating a manifest.

    Attributes:
        valid (bool): Whether the manifest is valid
        resources (ValidateResultResources | Unset): Count of each resource type
        missing_secrets (list[str] | Unset): Secret names referenced but not configured
        errors (list[str] | Unset): Validation errors
        warnings (list[str] | Unset): Validation warnings
    """

    valid: bool
    resources: ValidateResultResources | Unset = UNSET
    missing_secrets: list[str] | Unset = UNSET
    errors: list[str] | Unset = UNSET
    warnings: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        valid = self.valid

        resources: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resources, Unset):
            resources = self.resources.to_dict()

        missing_secrets: list[str] | Unset = UNSET
        if not isinstance(self.missing_secrets, Unset):
            missing_secrets = self.missing_secrets

        errors: list[str] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = self.errors

        warnings: list[str] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = self.warnings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "valid": valid,
            }
        )
        if resources is not UNSET:
            field_dict["resources"] = resources
        if missing_secrets is not UNSET:
            field_dict["missing_secrets"] = missing_secrets
        if errors is not UNSET:
            field_dict["errors"] = errors
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.validate_result_resources import ValidateResultResources

        d = dict(src_dict)
        valid = d.pop("valid")

        _resources = d.pop("resources", UNSET)
        resources: ValidateResultResources | Unset
        if isinstance(_resources, Unset):
            resources = UNSET
        else:
            resources = ValidateResultResources.from_dict(_resources)

        missing_secrets = cast(list[str], d.pop("missing_secrets", UNSET))

        errors = cast(list[str], d.pop("errors", UNSET))

        warnings = cast(list[str], d.pop("warnings", UNSET))

        validate_result = cls(
            valid=valid,
            resources=resources,
            missing_secrets=missing_secrets,
            errors=errors,
            warnings=warnings,
        )

        validate_result.additional_properties = d
        return validate_result

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
