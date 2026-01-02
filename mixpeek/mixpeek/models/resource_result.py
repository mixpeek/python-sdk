from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.resource_result_status import ResourceResultStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ResourceResult")


@_attrs_define
class ResourceResult:
    """Result of applying a single resource.

    Attributes:
        resource_type (str): Type of resource (namespace, bucket, etc.)
        name (str): Resource name from manifest
        status (ResourceResultStatus): Status of a resource creation attempt.
        resource_id (None | str | Unset): Created resource ID
        error (None | str | Unset): Error message if failed
    """

    resource_type: str
    name: str
    status: ResourceResultStatus
    resource_id: None | str | Unset = UNSET
    error: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource_type = self.resource_type

        name = self.name

        status = self.status.value

        resource_id: None | str | Unset
        if isinstance(self.resource_id, Unset):
            resource_id = UNSET
        else:
            resource_id = self.resource_id

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resource_type": resource_type,
                "name": name,
                "status": status,
            }
        )
        if resource_id is not UNSET:
            field_dict["resource_id"] = resource_id
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        resource_type = d.pop("resource_type")

        name = d.pop("name")

        status = ResourceResultStatus(d.pop("status"))

        def _parse_resource_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_id = _parse_resource_id(d.pop("resource_id", UNSET))

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        resource_result = cls(
            resource_type=resource_type,
            name=name,
            status=status,
            resource_id=resource_id,
            error=error,
        )

        resource_result.additional_properties = d
        return resource_result

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
