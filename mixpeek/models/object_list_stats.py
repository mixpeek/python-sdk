from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.object_list_stats_objects_by_status import ObjectListStatsObjectsByStatus


T = TypeVar("T", bound="ObjectListStats")


@_attrs_define
class ObjectListStats:
    """Aggregate statistics for a list of objects.

    Attributes:
        total_objects (int | Unset): Total number of objects in the result Default: 0.
        total_blobs (int | Unset): Total number of blobs across all objects Default: 0.
        avg_blobs_per_object (float | Unset): Average number of blobs per object Default: 0.0.
        objects_by_status (ObjectListStatsObjectsByStatus | Unset): Count of objects grouped by status
    """

    total_objects: int | Unset = 0
    total_blobs: int | Unset = 0
    avg_blobs_per_object: float | Unset = 0.0
    objects_by_status: ObjectListStatsObjectsByStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_objects = self.total_objects

        total_blobs = self.total_blobs

        avg_blobs_per_object = self.avg_blobs_per_object

        objects_by_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.objects_by_status, Unset):
            objects_by_status = self.objects_by_status.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_objects is not UNSET:
            field_dict["total_objects"] = total_objects
        if total_blobs is not UNSET:
            field_dict["total_blobs"] = total_blobs
        if avg_blobs_per_object is not UNSET:
            field_dict["avg_blobs_per_object"] = avg_blobs_per_object
        if objects_by_status is not UNSET:
            field_dict["objects_by_status"] = objects_by_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.object_list_stats_objects_by_status import ObjectListStatsObjectsByStatus

        d = dict(src_dict)
        total_objects = d.pop("total_objects", UNSET)

        total_blobs = d.pop("total_blobs", UNSET)

        avg_blobs_per_object = d.pop("avg_blobs_per_object", UNSET)

        _objects_by_status = d.pop("objects_by_status", UNSET)
        objects_by_status: ObjectListStatsObjectsByStatus | Unset
        if isinstance(_objects_by_status, Unset):
            objects_by_status = UNSET
        else:
            objects_by_status = ObjectListStatsObjectsByStatus.from_dict(_objects_by_status)

        object_list_stats = cls(
            total_objects=total_objects,
            total_blobs=total_blobs,
            avg_blobs_per_object=avg_blobs_per_object,
            objects_by_status=objects_by_status,
        )

        object_list_stats.additional_properties = d
        return object_list_stats

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
