from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.health_status import HealthStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="HealthCheck")


@_attrs_define
class HealthCheck:
    """Health check information for a retriever.

    Attributes:
        status (HealthStatus | Unset): Health status of a retriever.
        last_check (datetime.datetime | None | Unset): When the health was last checked
        issues (list[str] | Unset): List of current issues if any
    """

    status: HealthStatus | Unset = UNSET
    last_check: datetime.datetime | None | Unset = UNSET
    issues: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        last_check: None | str | Unset
        if isinstance(self.last_check, Unset):
            last_check = UNSET
        elif isinstance(self.last_check, datetime.datetime):
            last_check = self.last_check.isoformat()
        else:
            last_check = self.last_check

        issues: list[str] | Unset = UNSET
        if not isinstance(self.issues, Unset):
            issues = self.issues

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if last_check is not UNSET:
            field_dict["last_check"] = last_check
        if issues is not UNSET:
            field_dict["issues"] = issues

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: HealthStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = HealthStatus(_status)

        def _parse_last_check(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_check_type_0 = isoparse(data)

                return last_check_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_check = _parse_last_check(d.pop("last_check", UNSET))

        issues = cast(list[str], d.pop("issues", UNSET))

        health_check = cls(
            status=status,
            last_check=last_check,
            issues=issues,
        )

        health_check.additional_properties = d
        return health_check

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
