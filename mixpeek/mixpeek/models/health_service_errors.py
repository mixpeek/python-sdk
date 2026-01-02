from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HealthServiceErrors")


@_attrs_define
class HealthServiceErrors:
    """Optional error messages for dependent services (present when a check fails).

    Attributes:
        cache (None | str | Unset): Cache layer error message, if any
        metadata (None | str | Unset): Metadata store error message, if any
        vector_store (None | str | Unset): Vector database error message, if any
        object_storage (None | str | Unset): Object storage error message, if any
        task_queue (None | str | Unset): Task queue error message, if any
        inference (None | str | Unset): Inference engine error message, if any
        analytics (None | str | Unset): Analytics backend error message, if any
    """

    cache: None | str | Unset = UNSET
    metadata: None | str | Unset = UNSET
    vector_store: None | str | Unset = UNSET
    object_storage: None | str | Unset = UNSET
    task_queue: None | str | Unset = UNSET
    inference: None | str | Unset = UNSET
    analytics: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cache: None | str | Unset
        if isinstance(self.cache, Unset):
            cache = UNSET
        else:
            cache = self.cache

        metadata: None | str | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        else:
            metadata = self.metadata

        vector_store: None | str | Unset
        if isinstance(self.vector_store, Unset):
            vector_store = UNSET
        else:
            vector_store = self.vector_store

        object_storage: None | str | Unset
        if isinstance(self.object_storage, Unset):
            object_storage = UNSET
        else:
            object_storage = self.object_storage

        task_queue: None | str | Unset
        if isinstance(self.task_queue, Unset):
            task_queue = UNSET
        else:
            task_queue = self.task_queue

        inference: None | str | Unset
        if isinstance(self.inference, Unset):
            inference = UNSET
        else:
            inference = self.inference

        analytics: None | str | Unset
        if isinstance(self.analytics, Unset):
            analytics = UNSET
        else:
            analytics = self.analytics

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cache is not UNSET:
            field_dict["cache"] = cache
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if vector_store is not UNSET:
            field_dict["vector_store"] = vector_store
        if object_storage is not UNSET:
            field_dict["object_storage"] = object_storage
        if task_queue is not UNSET:
            field_dict["task_queue"] = task_queue
        if inference is not UNSET:
            field_dict["inference"] = inference
        if analytics is not UNSET:
            field_dict["analytics"] = analytics

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_cache(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cache = _parse_cache(d.pop("cache", UNSET))

        def _parse_metadata(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        def _parse_vector_store(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vector_store = _parse_vector_store(d.pop("vector_store", UNSET))

        def _parse_object_storage(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        object_storage = _parse_object_storage(d.pop("object_storage", UNSET))

        def _parse_task_queue(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        task_queue = _parse_task_queue(d.pop("task_queue", UNSET))

        def _parse_inference(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        inference = _parse_inference(d.pop("inference", UNSET))

        def _parse_analytics(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        analytics = _parse_analytics(d.pop("analytics", UNSET))

        health_service_errors = cls(
            cache=cache,
            metadata=metadata,
            vector_store=vector_store,
            object_storage=object_storage,
            task_queue=task_queue,
            inference=inference,
            analytics=analytics,
        )

        health_service_errors.additional_properties = d
        return health_service_errors

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
