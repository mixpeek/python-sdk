from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.resource_result import ResourceResult


T = TypeVar("T", bound="ApplyResult")


@_attrs_define
class ApplyResult:
    """Result of applying a manifest.

    Attributes:
        success (bool): Whether all resources were created successfully
        resources (list[ResourceResult] | Unset): Results for each resource
        created_count (int | Unset): Number of resources created Default: 0.
        failed_count (int | Unset): Number of resources that failed Default: 0.
        skipped_count (int | Unset): Number of resources skipped Default: 0.
        errors (list[str] | Unset): Error messages
        rollback_performed (bool | Unset): Whether rollback was performed due to failure Default: False.
        dry_run (bool | Unset): Whether this was a dry run (no changes made) Default: False.
    """

    success: bool
    resources: list[ResourceResult] | Unset = UNSET
    created_count: int | Unset = 0
    failed_count: int | Unset = 0
    skipped_count: int | Unset = 0
    errors: list[str] | Unset = UNSET
    rollback_performed: bool | Unset = False
    dry_run: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        resources: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.resources, Unset):
            resources = []
            for resources_item_data in self.resources:
                resources_item = resources_item_data.to_dict()
                resources.append(resources_item)

        created_count = self.created_count

        failed_count = self.failed_count

        skipped_count = self.skipped_count

        errors: list[str] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = self.errors

        rollback_performed = self.rollback_performed

        dry_run = self.dry_run

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
            }
        )
        if resources is not UNSET:
            field_dict["resources"] = resources
        if created_count is not UNSET:
            field_dict["created_count"] = created_count
        if failed_count is not UNSET:
            field_dict["failed_count"] = failed_count
        if skipped_count is not UNSET:
            field_dict["skipped_count"] = skipped_count
        if errors is not UNSET:
            field_dict["errors"] = errors
        if rollback_performed is not UNSET:
            field_dict["rollback_performed"] = rollback_performed
        if dry_run is not UNSET:
            field_dict["dry_run"] = dry_run

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.resource_result import ResourceResult

        d = dict(src_dict)
        success = d.pop("success")

        _resources = d.pop("resources", UNSET)
        resources: list[ResourceResult] | Unset = UNSET
        if _resources is not UNSET:
            resources = []
            for resources_item_data in _resources:
                resources_item = ResourceResult.from_dict(resources_item_data)

                resources.append(resources_item)

        created_count = d.pop("created_count", UNSET)

        failed_count = d.pop("failed_count", UNSET)

        skipped_count = d.pop("skipped_count", UNSET)

        errors = cast(list[str], d.pop("errors", UNSET))

        rollback_performed = d.pop("rollback_performed", UNSET)

        dry_run = d.pop("dry_run", UNSET)

        apply_result = cls(
            success=success,
            resources=resources,
            created_count=created_count,
            failed_count=failed_count,
            skipped_count=skipped_count,
            errors=errors,
            rollback_performed=rollback_performed,
            dry_run=dry_run,
        )

        apply_result.additional_properties = d
        return apply_result

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
