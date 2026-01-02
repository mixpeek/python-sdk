from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CollectionDetail")


@_attrs_define
class CollectionDetail:
    """Detailed information about a collection referenced by a retriever.

    Attributes:
        collection_id (str): Collection identifier
        collection_name (str): Human-readable collection name
        document_count (int | None | Unset): Number of documents in the collection
        enabled (bool | None | Unset): Whether the collection is active
        last_indexed_at (datetime.datetime | None | Unset): When the collection was last indexed
    """

    collection_id: str
    collection_name: str
    document_count: int | None | Unset = UNSET
    enabled: bool | None | Unset = UNSET
    last_indexed_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        collection_id = self.collection_id

        collection_name = self.collection_name

        document_count: int | None | Unset
        if isinstance(self.document_count, Unset):
            document_count = UNSET
        else:
            document_count = self.document_count

        enabled: bool | None | Unset
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

        last_indexed_at: None | str | Unset
        if isinstance(self.last_indexed_at, Unset):
            last_indexed_at = UNSET
        elif isinstance(self.last_indexed_at, datetime.datetime):
            last_indexed_at = self.last_indexed_at.isoformat()
        else:
            last_indexed_at = self.last_indexed_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "collection_id": collection_id,
                "collection_name": collection_name,
            }
        )
        if document_count is not UNSET:
            field_dict["document_count"] = document_count
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if last_indexed_at is not UNSET:
            field_dict["last_indexed_at"] = last_indexed_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        collection_id = d.pop("collection_id")

        collection_name = d.pop("collection_name")

        def _parse_document_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        document_count = _parse_document_count(d.pop("document_count", UNSET))

        def _parse_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))

        def _parse_last_indexed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_indexed_at_type_0 = isoparse(data)

                return last_indexed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_indexed_at = _parse_last_indexed_at(d.pop("last_indexed_at", UNSET))

        collection_detail = cls(
            collection_id=collection_id,
            collection_name=collection_name,
            document_count=document_count,
            enabled=enabled,
            last_indexed_at=last_indexed_at,
        )

        collection_detail.additional_properties = d
        return collection_detail

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
