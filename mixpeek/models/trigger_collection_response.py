from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TriggerCollectionResponse")


@_attrs_define
class TriggerCollectionResponse:
    """Response after triggering collection processing.

    Use `batch_id` or `task_id` to monitor progress via GET /v1/batches/{batch_id}
    or GET /v1/tasks/{task_id}.

        Attributes:
            batch_id (str): ID of the created batch for tracking progress.
            task_id (str): Task ID for monitoring via GET /v1/tasks/{task_id}.
            collection_id (str): ID of the collection being processed.
            total_tiers (int): Number of processing tiers in the DAG.
            message (str): Human-readable status message.
            source_bucket_ids (list[str] | None | Unset): Bucket IDs that objects were discovered from (bucket-sourced
                collections).
            source_collection_ids (list[str] | None | Unset): Collection IDs that documents were read from (collection-
                sourced collections).
            object_count (int | None | Unset): Total number of objects included in the batch (bucket-sourced collections).
            document_count (int | None | Unset): Total number of documents to process (collection-sourced collections).
    """

    batch_id: str
    task_id: str
    collection_id: str
    total_tiers: int
    message: str
    source_bucket_ids: list[str] | None | Unset = UNSET
    source_collection_ids: list[str] | None | Unset = UNSET
    object_count: int | None | Unset = UNSET
    document_count: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        batch_id = self.batch_id

        task_id = self.task_id

        collection_id = self.collection_id

        total_tiers = self.total_tiers

        message = self.message

        source_bucket_ids: list[str] | None | Unset
        if isinstance(self.source_bucket_ids, Unset):
            source_bucket_ids = UNSET
        elif isinstance(self.source_bucket_ids, list):
            source_bucket_ids = self.source_bucket_ids

        else:
            source_bucket_ids = self.source_bucket_ids

        source_collection_ids: list[str] | None | Unset
        if isinstance(self.source_collection_ids, Unset):
            source_collection_ids = UNSET
        elif isinstance(self.source_collection_ids, list):
            source_collection_ids = self.source_collection_ids

        else:
            source_collection_ids = self.source_collection_ids

        object_count: int | None | Unset
        if isinstance(self.object_count, Unset):
            object_count = UNSET
        else:
            object_count = self.object_count

        document_count: int | None | Unset
        if isinstance(self.document_count, Unset):
            document_count = UNSET
        else:
            document_count = self.document_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "batch_id": batch_id,
                "task_id": task_id,
                "collection_id": collection_id,
                "total_tiers": total_tiers,
                "message": message,
            }
        )
        if source_bucket_ids is not UNSET:
            field_dict["source_bucket_ids"] = source_bucket_ids
        if source_collection_ids is not UNSET:
            field_dict["source_collection_ids"] = source_collection_ids
        if object_count is not UNSET:
            field_dict["object_count"] = object_count
        if document_count is not UNSET:
            field_dict["document_count"] = document_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        batch_id = d.pop("batch_id")

        task_id = d.pop("task_id")

        collection_id = d.pop("collection_id")

        total_tiers = d.pop("total_tiers")

        message = d.pop("message")

        def _parse_source_bucket_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                source_bucket_ids_type_0 = cast(list[str], data)

                return source_bucket_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        source_bucket_ids = _parse_source_bucket_ids(d.pop("source_bucket_ids", UNSET))

        def _parse_source_collection_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                source_collection_ids_type_0 = cast(list[str], data)

                return source_collection_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        source_collection_ids = _parse_source_collection_ids(d.pop("source_collection_ids", UNSET))

        def _parse_object_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        object_count = _parse_object_count(d.pop("object_count", UNSET))

        def _parse_document_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        document_count = _parse_document_count(d.pop("document_count", UNSET))

        trigger_collection_response = cls(
            batch_id=batch_id,
            task_id=task_id,
            collection_id=collection_id,
            total_tiers=total_tiers,
            message=message,
            source_bucket_ids=source_bucket_ids,
            source_collection_ids=source_collection_ids,
            object_count=object_count,
            document_count=document_count,
        )

        trigger_collection_response.additional_properties = d
        return trigger_collection_response

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
