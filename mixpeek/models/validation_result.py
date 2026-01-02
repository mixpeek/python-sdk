from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.validation_error import ValidationError
    from ..models.validation_result_estimated_resources import ValidationResultEstimatedResources


T = TypeVar("T", bound="ValidationResult")


@_attrs_define
class ValidationResult:
    """Result of pre-flight validation.

    Attributes:
        valid (bool): Whether migration can proceed
        errors (list[ValidationError] | Unset): Validation errors
        warnings (list[ValidationError] | Unset): Validation warnings
        estimated_resources (ValidationResultEstimatedResources | Unset): Estimated resource counts
        estimated_duration_seconds (int | None | Unset): Estimated migration duration
    """

    valid: bool
    errors: list[ValidationError] | Unset = UNSET
    warnings: list[ValidationError] | Unset = UNSET
    estimated_resources: ValidationResultEstimatedResources | Unset = UNSET
    estimated_duration_seconds: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        valid = self.valid

        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        warnings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = []
            for warnings_item_data in self.warnings:
                warnings_item = warnings_item_data.to_dict()
                warnings.append(warnings_item)

        estimated_resources: dict[str, Any] | Unset = UNSET
        if not isinstance(self.estimated_resources, Unset):
            estimated_resources = self.estimated_resources.to_dict()

        estimated_duration_seconds: int | None | Unset
        if isinstance(self.estimated_duration_seconds, Unset):
            estimated_duration_seconds = UNSET
        else:
            estimated_duration_seconds = self.estimated_duration_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "valid": valid,
            }
        )
        if errors is not UNSET:
            field_dict["errors"] = errors
        if warnings is not UNSET:
            field_dict["warnings"] = warnings
        if estimated_resources is not UNSET:
            field_dict["estimated_resources"] = estimated_resources
        if estimated_duration_seconds is not UNSET:
            field_dict["estimated_duration_seconds"] = estimated_duration_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.validation_error import ValidationError
        from ..models.validation_result_estimated_resources import ValidationResultEstimatedResources

        d = dict(src_dict)
        valid = d.pop("valid")

        _errors = d.pop("errors", UNSET)
        errors: list[ValidationError] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = ValidationError.from_dict(errors_item_data)

                errors.append(errors_item)

        _warnings = d.pop("warnings", UNSET)
        warnings: list[ValidationError] | Unset = UNSET
        if _warnings is not UNSET:
            warnings = []
            for warnings_item_data in _warnings:
                warnings_item = ValidationError.from_dict(warnings_item_data)

                warnings.append(warnings_item)

        _estimated_resources = d.pop("estimated_resources", UNSET)
        estimated_resources: ValidationResultEstimatedResources | Unset
        if isinstance(_estimated_resources, Unset):
            estimated_resources = UNSET
        else:
            estimated_resources = ValidationResultEstimatedResources.from_dict(_estimated_resources)

        def _parse_estimated_duration_seconds(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        estimated_duration_seconds = _parse_estimated_duration_seconds(d.pop("estimated_duration_seconds", UNSET))

        validation_result = cls(
            valid=valid,
            errors=errors,
            warnings=warnings,
            estimated_resources=estimated_resources,
            estimated_duration_seconds=estimated_duration_seconds,
        )

        validation_result.additional_properties = d
        return validation_result

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
