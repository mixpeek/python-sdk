from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListAdhocExecutionsRequest")


@_attrs_define
class ListAdhocExecutionsRequest:
    """Request to list ad-hoc retriever executions with filtering.

    Allows filtering by status, time range, and searching by query summary.
    Results are ordered by timestamp descending (most recent first).

        Attributes:
            status (None | str | Unset): Filter by execution status. Common values: 'completed', 'failed'. OPTIONAL - omit
                to see all statuses.
            start_time (Any | None | Unset): Filter executions after this timestamp (inclusive). OPTIONAL - omit for no
                start time filter.
            end_time (Any | None | Unset): Filter executions before this timestamp (inclusive). OPTIONAL - omit for no end
                time filter.
    """

    status: None | str | Unset = UNSET
    start_time: Any | None | Unset = UNSET
    end_time: Any | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        start_time: Any | None | Unset
        if isinstance(self.start_time, Unset):
            start_time = UNSET
        else:
            start_time = self.start_time

        end_time: Any | None | Unset
        if isinstance(self.end_time, Unset):
            end_time = UNSET
        else:
            end_time = self.end_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if end_time is not UNSET:
            field_dict["end_time"] = end_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_start_time(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        start_time = _parse_start_time(d.pop("start_time", UNSET))

        def _parse_end_time(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        end_time = _parse_end_time(d.pop("end_time", UNSET))

        list_adhoc_executions_request = cls(
            status=status,
            start_time=start_time,
            end_time=end_time,
        )

        list_adhoc_executions_request.additional_properties = d
        return list_adhoc_executions_request

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
