from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.sync_config_metric import SyncConfigMetric
    from ..models.time_range import TimeRange


T = TypeVar("T", bound="SyncComparisonResponse")


@_attrs_define
class SyncComparisonResponse:
    """Sync configuration comparison response.

    Attributes:
        bucket_id (str): Bucket identifier
        time_range (TimeRange): Time range for analytics queries.
        configs (list[SyncConfigMetric]): Metrics per sync config
    """

    bucket_id: str
    time_range: TimeRange
    configs: list[SyncConfigMetric]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bucket_id = self.bucket_id

        time_range = self.time_range.to_dict()

        configs = []
        for configs_item_data in self.configs:
            configs_item = configs_item_data.to_dict()
            configs.append(configs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bucket_id": bucket_id,
                "time_range": time_range,
                "configs": configs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sync_config_metric import SyncConfigMetric
        from ..models.time_range import TimeRange

        d = dict(src_dict)
        bucket_id = d.pop("bucket_id")

        time_range = TimeRange.from_dict(d.pop("time_range"))

        configs = []
        _configs = d.pop("configs")
        for configs_item_data in _configs:
            configs_item = SyncConfigMetric.from_dict(configs_item_data)

            configs.append(configs_item)

        sync_comparison_response = cls(
            bucket_id=bucket_id,
            time_range=time_range,
            configs=configs,
        )

        sync_comparison_response.additional_properties = d
        return sync_comparison_response

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
