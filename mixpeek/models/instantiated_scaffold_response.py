from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="InstantiatedScaffoldResponse")


@_attrs_define
class InstantiatedScaffoldResponse:
    """Response after successful scaffold instantiation.

    Contains IDs and names of all four created resources.
    Use these IDs for subsequent operations:
    - Upload data: POST /v1/buckets/{bucket_id}/objects
    - Process: POST /v1/collections/{collection_id}/batches
    - Search: POST /v1/retrievers/{retriever_id}/retrieve

        Attributes:
            namespace_id (str): Created namespace ID (ns_xxx)
            namespace_name (str): Created namespace name
            bucket_id (str): Created bucket ID (bkt_xxx)
            bucket_name (str): Created bucket name
            collection_id (str): Created collection ID (col_xxx)
            collection_name (str): Created collection name
            retriever_id (str): Created retriever ID (ret_xxx)
            retriever_name (str): Created retriever name
            template_id (str): Scaffold template ID used
            status (str | Unset): Status: 'created' on success Default: 'created'.
            created_at (datetime.datetime | Unset): UTC timestamp of creation
    """

    namespace_id: str
    namespace_name: str
    bucket_id: str
    bucket_name: str
    collection_id: str
    collection_name: str
    retriever_id: str
    retriever_name: str
    template_id: str
    status: str | Unset = "created"
    created_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        namespace_id = self.namespace_id

        namespace_name = self.namespace_name

        bucket_id = self.bucket_id

        bucket_name = self.bucket_name

        collection_id = self.collection_id

        collection_name = self.collection_name

        retriever_id = self.retriever_id

        retriever_name = self.retriever_name

        template_id = self.template_id

        status = self.status

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "namespace_id": namespace_id,
                "namespace_name": namespace_name,
                "bucket_id": bucket_id,
                "bucket_name": bucket_name,
                "collection_id": collection_id,
                "collection_name": collection_name,
                "retriever_id": retriever_id,
                "retriever_name": retriever_name,
                "template_id": template_id,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        namespace_id = d.pop("namespace_id")

        namespace_name = d.pop("namespace_name")

        bucket_id = d.pop("bucket_id")

        bucket_name = d.pop("bucket_name")

        collection_id = d.pop("collection_id")

        collection_name = d.pop("collection_name")

        retriever_id = d.pop("retriever_id")

        retriever_name = d.pop("retriever_name")

        template_id = d.pop("template_id")

        status = d.pop("status", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        instantiated_scaffold_response = cls(
            namespace_id=namespace_id,
            namespace_name=namespace_name,
            bucket_id=bucket_id,
            bucket_name=bucket_name,
            collection_id=collection_id,
            collection_name=collection_name,
            retriever_id=retriever_id,
            retriever_name=retriever_name,
            template_id=template_id,
            status=status,
            created_at=created_at,
        )

        instantiated_scaffold_response.additional_properties = d
        return instantiated_scaffold_response

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
