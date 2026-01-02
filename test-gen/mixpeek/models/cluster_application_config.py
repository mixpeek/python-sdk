from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClusterApplicationConfig")


@_attrs_define
class ClusterApplicationConfig:
    """Configuration for automatic cluster execution on collection.

    Similar to TaxonomyApplicationConfig, this attaches a cluster to a collection
    and defines when/how it should be automatically executed.

    Used in CollectionModel.cluster_applications field.

        Attributes:
            cluster_id (str): ID of the cluster to execute (must exist and use this collection as input)
            auto_execute_on_batch (bool | Unset): Automatically execute cluster when batch processing completes for this
                collection. If False, cluster must be executed manually via API. Default: True.
            min_document_threshold (int | None | Unset): Minimum number of documents required before executing cluster. If
                document_count < threshold, clustering is skipped. Useful to avoid clustering on small datasets.
            cooldown_seconds (int | Unset): Minimum time (in seconds) between automatic cluster executions. Prevents
                excessive re-clustering on frequent batch completions. Default: 3600 seconds (1 hour). Default: 3600.
    """

    cluster_id: str
    auto_execute_on_batch: bool | Unset = True
    min_document_threshold: int | None | Unset = UNSET
    cooldown_seconds: int | Unset = 3600
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cluster_id = self.cluster_id

        auto_execute_on_batch = self.auto_execute_on_batch

        min_document_threshold: int | None | Unset
        if isinstance(self.min_document_threshold, Unset):
            min_document_threshold = UNSET
        else:
            min_document_threshold = self.min_document_threshold

        cooldown_seconds = self.cooldown_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cluster_id": cluster_id,
            }
        )
        if auto_execute_on_batch is not UNSET:
            field_dict["auto_execute_on_batch"] = auto_execute_on_batch
        if min_document_threshold is not UNSET:
            field_dict["min_document_threshold"] = min_document_threshold
        if cooldown_seconds is not UNSET:
            field_dict["cooldown_seconds"] = cooldown_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cluster_id = d.pop("cluster_id")

        auto_execute_on_batch = d.pop("auto_execute_on_batch", UNSET)

        def _parse_min_document_threshold(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        min_document_threshold = _parse_min_document_threshold(d.pop("min_document_threshold", UNSET))

        cooldown_seconds = d.pop("cooldown_seconds", UNSET)

        cluster_application_config = cls(
            cluster_id=cluster_id,
            auto_execute_on_batch=auto_execute_on_batch,
            min_document_threshold=min_document_threshold,
            cooldown_seconds=cooldown_seconds,
        )

        cluster_application_config.additional_properties = d
        return cluster_application_config

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
