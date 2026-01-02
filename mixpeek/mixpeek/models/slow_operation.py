from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.slow_operation_metadata import SlowOperationMetadata


T = TypeVar("T", bound="SlowOperation")


@_attrs_define
class SlowOperation:
    """Details of a slow operation.

    Attributes:
        timestamp (datetime.datetime): When the operation occurred
        stage_name (str): Stage name
        component (str): Component
        latency_ms (float): Operation latency
        metadata (SlowOperationMetadata | Unset): Additional context from profiling
    """

    timestamp: datetime.datetime
    stage_name: str
    component: str
    latency_ms: float
    metadata: SlowOperationMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp.isoformat()

        stage_name = self.stage_name

        component = self.component

        latency_ms = self.latency_ms

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
                "stage_name": stage_name,
                "component": component,
                "latency_ms": latency_ms,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.slow_operation_metadata import SlowOperationMetadata

        d = dict(src_dict)
        timestamp = isoparse(d.pop("timestamp"))

        stage_name = d.pop("stage_name")

        component = d.pop("component")

        latency_ms = d.pop("latency_ms")

        _metadata = d.pop("metadata", UNSET)
        metadata: SlowOperationMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = SlowOperationMetadata.from_dict(_metadata)

        slow_operation = cls(
            timestamp=timestamp,
            stage_name=stage_name,
            component=component,
            latency_ms=latency_ms,
            metadata=metadata,
        )

        slow_operation.additional_properties = d
        return slow_operation

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
