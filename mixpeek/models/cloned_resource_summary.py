from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClonedResourceSummary")


@_attrs_define
class ClonedResourceSummary:
    """Summary of cloned resources.

    Attributes:
        collections (int | Unset): Collections cloned Default: 0.
        retrievers (int | Unset): Retrievers cloned Default: 0.
        taxonomies (int | Unset): Taxonomies cloned Default: 0.
        buckets (int | Unset): Buckets cloned Default: 0.
        objects (int | Unset): Objects cloned Default: 0.
        points (int | Unset): Vector points cloned Default: 0.
    """

    collections: int | Unset = 0
    retrievers: int | Unset = 0
    taxonomies: int | Unset = 0
    buckets: int | Unset = 0
    objects: int | Unset = 0
    points: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        collections = self.collections

        retrievers = self.retrievers

        taxonomies = self.taxonomies

        buckets = self.buckets

        objects = self.objects

        points = self.points

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if collections is not UNSET:
            field_dict["collections"] = collections
        if retrievers is not UNSET:
            field_dict["retrievers"] = retrievers
        if taxonomies is not UNSET:
            field_dict["taxonomies"] = taxonomies
        if buckets is not UNSET:
            field_dict["buckets"] = buckets
        if objects is not UNSET:
            field_dict["objects"] = objects
        if points is not UNSET:
            field_dict["points"] = points

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        collections = d.pop("collections", UNSET)

        retrievers = d.pop("retrievers", UNSET)

        taxonomies = d.pop("taxonomies", UNSET)

        buckets = d.pop("buckets", UNSET)

        objects = d.pop("objects", UNSET)

        points = d.pop("points", UNSET)

        cloned_resource_summary = cls(
            collections=collections,
            retrievers=retrievers,
            taxonomies=taxonomies,
            buckets=buckets,
            objects=objects,
            points=points,
        )

        cloned_resource_summary.additional_properties = d
        return cloned_resource_summary

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
