from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.trigger_status import TriggerStatus
from ..models.trigger_type import TriggerType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListTriggersRequest")


@_attrs_define
class ListTriggersRequest:
    """Request to list triggers with filters and pagination.

    Attributes:
        cluster_id (None | str | Unset): Filter by cluster ID
        trigger_type (None | TriggerType | Unset): Filter by trigger type
        status (None | TriggerStatus | Unset): Filter by status
        offset (int | Unset): Pagination offset Default: 0.
        limit (int | Unset): Results per page Default: 50.
        sort_by (str | Unset): Field to sort by Default: 'created_at'.
        direction (str | Unset): Sort direction (asc/desc) Default: 'desc'.
    """

    cluster_id: None | str | Unset = UNSET
    trigger_type: None | TriggerType | Unset = UNSET
    status: None | TriggerStatus | Unset = UNSET
    offset: int | Unset = 0
    limit: int | Unset = 50
    sort_by: str | Unset = "created_at"
    direction: str | Unset = "desc"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cluster_id: None | str | Unset
        if isinstance(self.cluster_id, Unset):
            cluster_id = UNSET
        else:
            cluster_id = self.cluster_id

        trigger_type: None | str | Unset
        if isinstance(self.trigger_type, Unset):
            trigger_type = UNSET
        elif isinstance(self.trigger_type, TriggerType):
            trigger_type = self.trigger_type.value
        else:
            trigger_type = self.trigger_type

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, TriggerStatus):
            status = self.status.value
        else:
            status = self.status

        offset = self.offset

        limit = self.limit

        sort_by = self.sort_by

        direction = self.direction

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cluster_id is not UNSET:
            field_dict["cluster_id"] = cluster_id
        if trigger_type is not UNSET:
            field_dict["trigger_type"] = trigger_type
        if status is not UNSET:
            field_dict["status"] = status
        if offset is not UNSET:
            field_dict["offset"] = offset
        if limit is not UNSET:
            field_dict["limit"] = limit
        if sort_by is not UNSET:
            field_dict["sort_by"] = sort_by
        if direction is not UNSET:
            field_dict["direction"] = direction

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_cluster_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cluster_id = _parse_cluster_id(d.pop("cluster_id", UNSET))

        def _parse_trigger_type(data: object) -> None | TriggerType | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                trigger_type_type_0 = TriggerType(data)

                return trigger_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TriggerType | Unset, data)

        trigger_type = _parse_trigger_type(d.pop("trigger_type", UNSET))

        def _parse_status(data: object) -> None | TriggerStatus | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_0 = TriggerStatus(data)

                return status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TriggerStatus | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        offset = d.pop("offset", UNSET)

        limit = d.pop("limit", UNSET)

        sort_by = d.pop("sort_by", UNSET)

        direction = d.pop("direction", UNSET)

        list_triggers_request = cls(
            cluster_id=cluster_id,
            trigger_type=trigger_type,
            status=status,
            offset=offset,
            limit=limit,
            sort_by=sort_by,
            direction=direction,
        )

        list_triggers_request.additional_properties = d
        return list_triggers_request

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
