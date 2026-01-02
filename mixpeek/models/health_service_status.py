from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HealthServiceStatus")


@_attrs_define
class HealthServiceStatus:
    """Status flags for dependent services.

    Attributes:
        cache (bool): Cache layer connectivity successful
        metadata (bool): Metadata store connectivity successful
        vector_store (bool): Vector database connectivity successful
        object_storage (bool): Object storage connectivity successful
        task_queue (bool): Task queue execution successful
        inference (bool): Inference engine health check successful
        analytics (bool | None | Unset): Analytics backend healthy (optional, None if disabled)
    """

    cache: bool
    metadata: bool
    vector_store: bool
    object_storage: bool
    task_queue: bool
    inference: bool
    analytics: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cache = self.cache

        metadata = self.metadata

        vector_store = self.vector_store

        object_storage = self.object_storage

        task_queue = self.task_queue

        inference = self.inference

        analytics: bool | None | Unset
        if isinstance(self.analytics, Unset):
            analytics = UNSET
        else:
            analytics = self.analytics

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cache": cache,
                "metadata": metadata,
                "vector_store": vector_store,
                "object_storage": object_storage,
                "task_queue": task_queue,
                "inference": inference,
            }
        )
        if analytics is not UNSET:
            field_dict["analytics"] = analytics

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cache = d.pop("cache")

        metadata = d.pop("metadata")

        vector_store = d.pop("vector_store")

        object_storage = d.pop("object_storage")

        task_queue = d.pop("task_queue")

        inference = d.pop("inference")

        def _parse_analytics(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        analytics = _parse_analytics(d.pop("analytics", UNSET))

        health_service_status = cls(
            cache=cache,
            metadata=metadata,
            vector_store=vector_store,
            object_storage=object_storage,
            task_queue=task_queue,
            inference=inference,
            analytics=analytics,
        )

        health_service_status.additional_properties = d
        return health_service_status

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
