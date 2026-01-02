from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TriggerHistoryRequest")


@_attrs_define
class TriggerHistoryRequest:
    """Request for trigger execution history.

    Attributes:
        offset (int | Unset): Pagination offset Default: 0.
        limit (int | Unset): Results per page Default: 50.
        status_filter (None | str | Unset): Filter by execution status
    """

    offset: int | Unset = 0
    limit: int | Unset = 50
    status_filter: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        offset = self.offset

        limit = self.limit

        status_filter: None | str | Unset
        if isinstance(self.status_filter, Unset):
            status_filter = UNSET
        else:
            status_filter = self.status_filter

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if offset is not UNSET:
            field_dict["offset"] = offset
        if limit is not UNSET:
            field_dict["limit"] = limit
        if status_filter is not UNSET:
            field_dict["status_filter"] = status_filter

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        offset = d.pop("offset", UNSET)

        limit = d.pop("limit", UNSET)

        def _parse_status_filter(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status_filter = _parse_status_filter(d.pop("status_filter", UNSET))

        trigger_history_request = cls(
            offset=offset,
            limit=limit,
            status_filter=status_filter,
        )

        trigger_history_request.additional_properties = d
        return trigger_history_request

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
