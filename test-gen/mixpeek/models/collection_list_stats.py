from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CollectionListStats")


@_attrs_define
class CollectionListStats:
    """Aggregate statistics for a list of collections.

    Attributes:
        total_documents (int | Unset): Total number of documents across all collections Default: 0.
        avg_documents_per_collection (float | Unset): Average number of documents per collection Default: 0.0.
        collections_with_taxonomies (int | Unset): Number of collections with taxonomy applications Default: 0.
        total_feature_extractors (int | Unset): Total number of feature extractors across all collections Default: 0.
        total_taxonomies (int | Unset): Total number of taxonomy connections across all collections Default: 0.
        total_retrievers (int | Unset): Total number of retriever connections across all collections Default: 0.
    """

    total_documents: int | Unset = 0
    avg_documents_per_collection: float | Unset = 0.0
    collections_with_taxonomies: int | Unset = 0
    total_feature_extractors: int | Unset = 0
    total_taxonomies: int | Unset = 0
    total_retrievers: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_documents = self.total_documents

        avg_documents_per_collection = self.avg_documents_per_collection

        collections_with_taxonomies = self.collections_with_taxonomies

        total_feature_extractors = self.total_feature_extractors

        total_taxonomies = self.total_taxonomies

        total_retrievers = self.total_retrievers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_documents is not UNSET:
            field_dict["total_documents"] = total_documents
        if avg_documents_per_collection is not UNSET:
            field_dict["avg_documents_per_collection"] = avg_documents_per_collection
        if collections_with_taxonomies is not UNSET:
            field_dict["collections_with_taxonomies"] = collections_with_taxonomies
        if total_feature_extractors is not UNSET:
            field_dict["total_feature_extractors"] = total_feature_extractors
        if total_taxonomies is not UNSET:
            field_dict["total_taxonomies"] = total_taxonomies
        if total_retrievers is not UNSET:
            field_dict["total_retrievers"] = total_retrievers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_documents = d.pop("total_documents", UNSET)

        avg_documents_per_collection = d.pop("avg_documents_per_collection", UNSET)

        collections_with_taxonomies = d.pop("collections_with_taxonomies", UNSET)

        total_feature_extractors = d.pop("total_feature_extractors", UNSET)

        total_taxonomies = d.pop("total_taxonomies", UNSET)

        total_retrievers = d.pop("total_retrievers", UNSET)

        collection_list_stats = cls(
            total_documents=total_documents,
            avg_documents_per_collection=avg_documents_per_collection,
            collections_with_taxonomies=collections_with_taxonomies,
            total_feature_extractors=total_feature_extractors,
            total_taxonomies=total_taxonomies,
            total_retrievers=total_retrievers,
        )

        collection_list_stats.additional_properties = d
        return collection_list_stats

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
