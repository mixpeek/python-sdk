from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NamespaceListStats")


@_attrs_define
class NamespaceListStats:
    """Aggregate statistics for a list of namespaces.

    Attributes:
        total_feature_extractors (int | Unset): Total number of feature extractors across all namespaces Default: 0.
        total_payload_indexes (int | Unset): Total number of payload indexes across all namespaces Default: 0.
        total_documents (int | Unset): Total number of documents across all namespaces Default: 0.
        total_buckets (int | Unset): Total number of buckets across all namespaces Default: 0.
        total_collections (int | Unset): Total number of collections across all namespaces Default: 0.
        total_objects (int | Unset): Total number of objects across all namespaces Default: 0.
        avg_feature_extractors_per_namespace (float | Unset): Average number of feature extractors per namespace
            Default: 0.0.
        avg_payload_indexes_per_namespace (float | Unset): Average number of payload indexes per namespace Default: 0.0.
        avg_documents_per_namespace (float | Unset): Average number of documents per namespace Default: 0.0.
        avg_buckets_per_namespace (float | Unset): Average number of buckets per namespace Default: 0.0.
        avg_collections_per_namespace (float | Unset): Average number of collections per namespace Default: 0.0.
        avg_objects_per_namespace (float | Unset): Average number of objects per namespace Default: 0.0.
    """

    total_feature_extractors: int | Unset = 0
    total_payload_indexes: int | Unset = 0
    total_documents: int | Unset = 0
    total_buckets: int | Unset = 0
    total_collections: int | Unset = 0
    total_objects: int | Unset = 0
    avg_feature_extractors_per_namespace: float | Unset = 0.0
    avg_payload_indexes_per_namespace: float | Unset = 0.0
    avg_documents_per_namespace: float | Unset = 0.0
    avg_buckets_per_namespace: float | Unset = 0.0
    avg_collections_per_namespace: float | Unset = 0.0
    avg_objects_per_namespace: float | Unset = 0.0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_feature_extractors = self.total_feature_extractors

        total_payload_indexes = self.total_payload_indexes

        total_documents = self.total_documents

        total_buckets = self.total_buckets

        total_collections = self.total_collections

        total_objects = self.total_objects

        avg_feature_extractors_per_namespace = self.avg_feature_extractors_per_namespace

        avg_payload_indexes_per_namespace = self.avg_payload_indexes_per_namespace

        avg_documents_per_namespace = self.avg_documents_per_namespace

        avg_buckets_per_namespace = self.avg_buckets_per_namespace

        avg_collections_per_namespace = self.avg_collections_per_namespace

        avg_objects_per_namespace = self.avg_objects_per_namespace

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_feature_extractors is not UNSET:
            field_dict["total_feature_extractors"] = total_feature_extractors
        if total_payload_indexes is not UNSET:
            field_dict["total_payload_indexes"] = total_payload_indexes
        if total_documents is not UNSET:
            field_dict["total_documents"] = total_documents
        if total_buckets is not UNSET:
            field_dict["total_buckets"] = total_buckets
        if total_collections is not UNSET:
            field_dict["total_collections"] = total_collections
        if total_objects is not UNSET:
            field_dict["total_objects"] = total_objects
        if avg_feature_extractors_per_namespace is not UNSET:
            field_dict["avg_feature_extractors_per_namespace"] = avg_feature_extractors_per_namespace
        if avg_payload_indexes_per_namespace is not UNSET:
            field_dict["avg_payload_indexes_per_namespace"] = avg_payload_indexes_per_namespace
        if avg_documents_per_namespace is not UNSET:
            field_dict["avg_documents_per_namespace"] = avg_documents_per_namespace
        if avg_buckets_per_namespace is not UNSET:
            field_dict["avg_buckets_per_namespace"] = avg_buckets_per_namespace
        if avg_collections_per_namespace is not UNSET:
            field_dict["avg_collections_per_namespace"] = avg_collections_per_namespace
        if avg_objects_per_namespace is not UNSET:
            field_dict["avg_objects_per_namespace"] = avg_objects_per_namespace

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_feature_extractors = d.pop("total_feature_extractors", UNSET)

        total_payload_indexes = d.pop("total_payload_indexes", UNSET)

        total_documents = d.pop("total_documents", UNSET)

        total_buckets = d.pop("total_buckets", UNSET)

        total_collections = d.pop("total_collections", UNSET)

        total_objects = d.pop("total_objects", UNSET)

        avg_feature_extractors_per_namespace = d.pop("avg_feature_extractors_per_namespace", UNSET)

        avg_payload_indexes_per_namespace = d.pop("avg_payload_indexes_per_namespace", UNSET)

        avg_documents_per_namespace = d.pop("avg_documents_per_namespace", UNSET)

        avg_buckets_per_namespace = d.pop("avg_buckets_per_namespace", UNSET)

        avg_collections_per_namespace = d.pop("avg_collections_per_namespace", UNSET)

        avg_objects_per_namespace = d.pop("avg_objects_per_namespace", UNSET)

        namespace_list_stats = cls(
            total_feature_extractors=total_feature_extractors,
            total_payload_indexes=total_payload_indexes,
            total_documents=total_documents,
            total_buckets=total_buckets,
            total_collections=total_collections,
            total_objects=total_objects,
            avg_feature_extractors_per_namespace=avg_feature_extractors_per_namespace,
            avg_payload_indexes_per_namespace=avg_payload_indexes_per_namespace,
            avg_documents_per_namespace=avg_documents_per_namespace,
            avg_buckets_per_namespace=avg_buckets_per_namespace,
            avg_collections_per_namespace=avg_collections_per_namespace,
            avg_objects_per_namespace=avg_objects_per_namespace,
        )

        namespace_list_stats.additional_properties = d
        return namespace_list_stats

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
