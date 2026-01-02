from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CollectionOverviewResponse")


@_attrs_define
class CollectionOverviewResponse:
    """Collection overview metrics.

    Attributes:
        collection_id (str):
        collection_name (str):
        total_documents (int):
        documents_last_24h (int):
        documents_last_7d (int):
        avg_processing_time_ms (float):
        success_rate (float):
        active_taxonomies (int):
        active_clusters (int):
        last_indexed (datetime.datetime | None | Unset):
    """

    collection_id: str
    collection_name: str
    total_documents: int
    documents_last_24h: int
    documents_last_7d: int
    avg_processing_time_ms: float
    success_rate: float
    active_taxonomies: int
    active_clusters: int
    last_indexed: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        collection_id = self.collection_id

        collection_name = self.collection_name

        total_documents = self.total_documents

        documents_last_24h = self.documents_last_24h

        documents_last_7d = self.documents_last_7d

        avg_processing_time_ms = self.avg_processing_time_ms

        success_rate = self.success_rate

        active_taxonomies = self.active_taxonomies

        active_clusters = self.active_clusters

        last_indexed: None | str | Unset
        if isinstance(self.last_indexed, Unset):
            last_indexed = UNSET
        elif isinstance(self.last_indexed, datetime.datetime):
            last_indexed = self.last_indexed.isoformat()
        else:
            last_indexed = self.last_indexed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "collection_id": collection_id,
                "collection_name": collection_name,
                "total_documents": total_documents,
                "documents_last_24h": documents_last_24h,
                "documents_last_7d": documents_last_7d,
                "avg_processing_time_ms": avg_processing_time_ms,
                "success_rate": success_rate,
                "active_taxonomies": active_taxonomies,
                "active_clusters": active_clusters,
            }
        )
        if last_indexed is not UNSET:
            field_dict["last_indexed"] = last_indexed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        collection_id = d.pop("collection_id")

        collection_name = d.pop("collection_name")

        total_documents = d.pop("total_documents")

        documents_last_24h = d.pop("documents_last_24h")

        documents_last_7d = d.pop("documents_last_7d")

        avg_processing_time_ms = d.pop("avg_processing_time_ms")

        success_rate = d.pop("success_rate")

        active_taxonomies = d.pop("active_taxonomies")

        active_clusters = d.pop("active_clusters")

        def _parse_last_indexed(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_indexed_type_0 = isoparse(data)

                return last_indexed_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_indexed = _parse_last_indexed(d.pop("last_indexed", UNSET))

        collection_overview_response = cls(
            collection_id=collection_id,
            collection_name=collection_name,
            total_documents=total_documents,
            documents_last_24h=documents_last_24h,
            documents_last_7d=documents_last_7d,
            avg_processing_time_ms=avg_processing_time_ms,
            success_rate=success_rate,
            active_taxonomies=active_taxonomies,
            active_clusters=active_clusters,
            last_indexed=last_indexed,
        )

        collection_overview_response.additional_properties = d
        return collection_overview_response

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
