from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TriggerTierRequest")


@_attrs_define
class TriggerTierRequest:
    """Request to trigger next tier processing.

    Attributes:
        internal_id (str):
        namespace_id (str):
        ray_job_id (str):
        completed_tier (int):
        start_time_ms (int | None | Unset):
        end_time_ms (int | None | Unset):
    """

    internal_id: str
    namespace_id: str
    ray_job_id: str
    completed_tier: int
    start_time_ms: int | None | Unset = UNSET
    end_time_ms: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        internal_id = self.internal_id

        namespace_id = self.namespace_id

        ray_job_id = self.ray_job_id

        completed_tier = self.completed_tier

        start_time_ms: int | None | Unset
        if isinstance(self.start_time_ms, Unset):
            start_time_ms = UNSET
        else:
            start_time_ms = self.start_time_ms

        end_time_ms: int | None | Unset
        if isinstance(self.end_time_ms, Unset):
            end_time_ms = UNSET
        else:
            end_time_ms = self.end_time_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "internal_id": internal_id,
                "namespace_id": namespace_id,
                "ray_job_id": ray_job_id,
                "completed_tier": completed_tier,
            }
        )
        if start_time_ms is not UNSET:
            field_dict["start_time_ms"] = start_time_ms
        if end_time_ms is not UNSET:
            field_dict["end_time_ms"] = end_time_ms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        internal_id = d.pop("internal_id")

        namespace_id = d.pop("namespace_id")

        ray_job_id = d.pop("ray_job_id")

        completed_tier = d.pop("completed_tier")

        def _parse_start_time_ms(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        start_time_ms = _parse_start_time_ms(d.pop("start_time_ms", UNSET))

        def _parse_end_time_ms(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        end_time_ms = _parse_end_time_ms(d.pop("end_time_ms", UNSET))

        trigger_tier_request = cls(
            internal_id=internal_id,
            namespace_id=namespace_id,
            ray_job_id=ray_job_id,
            completed_tier=completed_tier,
            start_time_ms=start_time_ms,
            end_time_ms=end_time_ms,
        )

        trigger_tier_request.additional_properties = d
        return trigger_tier_request

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
