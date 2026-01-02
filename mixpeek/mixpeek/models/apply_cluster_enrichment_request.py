from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApplyClusterEnrichmentRequest")


@_attrs_define
class ApplyClusterEnrichmentRequest:
    """Request to apply clustering enrichment to a collection.

    Supports applying multiple clustering results in one request via
    `clustering_ids`. For backward compatibility, a single `clustering_id`
    is also accepted and up-converted.

        Attributes:
            clustering_ids (list[str]): Clustering result IDs to apply
            source_collection_id (str): Collection to enrich
            target_collection_id (None | str | Unset): Target collection to write enriched docs to
            batch_size (int | Unset): Batch size for processing Default: 1000.
            parallelism (int | Unset): Parallel workers Default: 1.
    """

    clustering_ids: list[str]
    source_collection_id: str
    target_collection_id: None | str | Unset = UNSET
    batch_size: int | Unset = 1000
    parallelism: int | Unset = 1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        clustering_ids = self.clustering_ids

        source_collection_id = self.source_collection_id

        target_collection_id: None | str | Unset
        if isinstance(self.target_collection_id, Unset):
            target_collection_id = UNSET
        else:
            target_collection_id = self.target_collection_id

        batch_size = self.batch_size

        parallelism = self.parallelism

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clustering_ids": clustering_ids,
                "source_collection_id": source_collection_id,
            }
        )
        if target_collection_id is not UNSET:
            field_dict["target_collection_id"] = target_collection_id
        if batch_size is not UNSET:
            field_dict["batch_size"] = batch_size
        if parallelism is not UNSET:
            field_dict["parallelism"] = parallelism

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        clustering_ids = cast(list[str], d.pop("clustering_ids"))

        source_collection_id = d.pop("source_collection_id")

        def _parse_target_collection_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        target_collection_id = _parse_target_collection_id(d.pop("target_collection_id", UNSET))

        batch_size = d.pop("batch_size", UNSET)

        parallelism = d.pop("parallelism", UNSET)

        apply_cluster_enrichment_request = cls(
            clustering_ids=clustering_ids,
            source_collection_id=source_collection_id,
            target_collection_id=target_collection_id,
            batch_size=batch_size,
            parallelism=parallelism,
        )

        apply_cluster_enrichment_request.additional_properties = d
        return apply_cluster_enrichment_request

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
