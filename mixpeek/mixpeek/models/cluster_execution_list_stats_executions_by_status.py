from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ClusterExecutionListStatsExecutionsByStatus")


@_attrs_define
class ClusterExecutionListStatsExecutionsByStatus:
    """OPTIONAL (always provided). Count of executions grouped by status. Keys: 'pending', 'processing', 'completed',
    'failed'. Values: Number of executions in each status. Use for:   - Status distribution chart (pie/bar chart).   -
    Health monitoring (high failed count = problem).   - Progress tracking (pending + processing = in-flight jobs).
    Example: {'completed': 45, 'failed': 3, 'processing': 2, 'pending': 0}. Empty dict {} if no executions in result
    set.

    """

    additional_properties: dict[str, int] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cluster_execution_list_stats_executions_by_status = cls()

        cluster_execution_list_stats_executions_by_status.additional_properties = d
        return cluster_execution_list_stats_executions_by_status

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> int:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: int) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
