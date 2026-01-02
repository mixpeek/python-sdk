from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.task_status_enum import TaskStatusEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListBatchesRequest")


@_attrs_define
class ListBatchesRequest:
    """The request model for listing batches.

    Attributes:
        status (None | TaskStatusEnum | Unset): Filter batches by status.
        offset (int | Unset): The number of batches to skip. Default: 0.
        limit (int | Unset): The maximum number of batches to return. Default: 100.
    """

    status: None | TaskStatusEnum | Unset = UNSET
    offset: int | Unset = 0
    limit: int | Unset = 100
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, TaskStatusEnum):
            status = self.status.value
        else:
            status = self.status

        offset = self.offset

        limit = self.limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if offset is not UNSET:
            field_dict["offset"] = offset
        if limit is not UNSET:
            field_dict["limit"] = limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_status(data: object) -> None | TaskStatusEnum | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_0 = TaskStatusEnum(data)

                return status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TaskStatusEnum | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        offset = d.pop("offset", UNSET)

        limit = d.pop("limit", UNSET)

        list_batches_request = cls(
            status=status,
            offset=offset,
            limit=limit,
        )

        list_batches_request.additional_properties = d
        return list_batches_request

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
