from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="FailureMetric")


@_attrs_define
class FailureMetric:
    """Cluster failure metrics.

    Attributes:
        timestamp (datetime.datetime):
        execution_id (str):
        error_message (str):
        error_type (str):
    """

    timestamp: datetime.datetime
    execution_id: str
    error_message: str
    error_type: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp.isoformat()

        execution_id = self.execution_id

        error_message = self.error_message

        error_type = self.error_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
                "execution_id": execution_id,
                "error_message": error_message,
                "error_type": error_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        timestamp = isoparse(d.pop("timestamp"))

        execution_id = d.pop("execution_id")

        error_message = d.pop("error_message")

        error_type = d.pop("error_type")

        failure_metric = cls(
            timestamp=timestamp,
            execution_id=execution_id,
            error_message=error_message,
            error_type=error_type,
        )

        failure_metric.additional_properties = d
        return failure_metric

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
