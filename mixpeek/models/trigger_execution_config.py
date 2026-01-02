from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.trigger_execution_config_config import TriggerExecutionConfigConfig


T = TypeVar("T", bound="TriggerExecutionConfig")


@_attrs_define
class TriggerExecutionConfig:
    """Configuration for cluster execution when trigger fires.

    Defines what clustering algorithm and parameters to use when the trigger executes.

    Examples:
        K-means clustering on 3 collections:
            {
                "collection_ids": ["col_abc123", "col_def456", "col_ghi789"],
                "config": {
                    "algorithm": "kmeans",
                    "n_clusters": 5,
                    "min_cluster_size": 2
                }
            }

        HDBSCAN clustering on single collection:
            {
                "collection_ids": ["col_products"],
                "config": {
                    "algorithm": "hdbscan",
                    "min_cluster_size": 10,
                    "min_samples": 5
                }
            }

        Attributes:
            collection_ids (list[str]): REQUIRED. List of collection IDs to cluster when trigger fires. Must contain at
                least one collection ID. All collections will be clustered together using the specified algorithm.
            config (TriggerExecutionConfigConfig): REQUIRED. Clustering algorithm configuration. Must include 'algorithm'
                field ('kmeans', 'hdbscan', 'hierarchical'). Additional fields depend on algorithm choice. K-means requires
                'n_clusters'. HDBSCAN requires 'min_cluster_size'.
    """

    collection_ids: list[str]
    config: TriggerExecutionConfigConfig
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        collection_ids = self.collection_ids

        config = self.config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "collection_ids": collection_ids,
                "config": config,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.trigger_execution_config_config import TriggerExecutionConfigConfig

        d = dict(src_dict)
        collection_ids = cast(list[str], d.pop("collection_ids"))

        config = TriggerExecutionConfigConfig.from_dict(d.pop("config"))

        trigger_execution_config = cls(
            collection_ids=collection_ids,
            config=config,
        )

        trigger_execution_config.additional_properties = d
        return trigger_execution_config

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
