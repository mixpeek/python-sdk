from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InstantiateCollectionTemplateRequest")


@_attrs_define
class InstantiateCollectionTemplateRequest:
    """Request to instantiate a collection from a template.

    Attributes:
        collection_name (str): Name for the new collection
        bucket_ids (list[str] | None | Unset): Bucket IDs to use for the collection (for bucket sources)
        collection_id (None | str | Unset): Collection ID to use for the collection (for collection sources)
        description (None | str | Unset): Optional description override for the collection
        tags (list[str] | Unset): Optional tags for the collection
    """

    collection_name: str
    bucket_ids: list[str] | None | Unset = UNSET
    collection_id: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    tags: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        collection_name = self.collection_name

        bucket_ids: list[str] | None | Unset
        if isinstance(self.bucket_ids, Unset):
            bucket_ids = UNSET
        elif isinstance(self.bucket_ids, list):
            bucket_ids = self.bucket_ids

        else:
            bucket_ids = self.bucket_ids

        collection_id: None | str | Unset
        if isinstance(self.collection_id, Unset):
            collection_id = UNSET
        else:
            collection_id = self.collection_id

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "collection_name": collection_name,
            }
        )
        if bucket_ids is not UNSET:
            field_dict["bucket_ids"] = bucket_ids
        if collection_id is not UNSET:
            field_dict["collection_id"] = collection_id
        if description is not UNSET:
            field_dict["description"] = description
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        collection_name = d.pop("collection_name")

        def _parse_bucket_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                bucket_ids_type_0 = cast(list[str], data)

                return bucket_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        bucket_ids = _parse_bucket_ids(d.pop("bucket_ids", UNSET))

        def _parse_collection_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        collection_id = _parse_collection_id(d.pop("collection_id", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        tags = cast(list[str], d.pop("tags", UNSET))

        instantiate_collection_template_request = cls(
            collection_name=collection_name,
            bucket_ids=bucket_ids,
            collection_id=collection_id,
            description=description,
            tags=tags,
        )

        instantiate_collection_template_request.additional_properties = d
        return instantiate_collection_template_request

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
