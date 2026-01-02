from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="ClusterExecutionMetric")


@_attrs_define
class ClusterExecutionMetric:
    """Single cluster execution metrics.

    Attributes:
        execution_id (str): Execution identifier
        started_at (datetime.datetime): Execution start time
        duration_seconds (float): Execution duration
        num_documents (int): Number of documents clustered
        num_clusters (int): Number of clusters created
        status (str): Execution status
        algorithm (str): Clustering algorithm used
    """

    execution_id: str
    started_at: datetime.datetime
    duration_seconds: float
    num_documents: int
    num_clusters: int
    status: str
    algorithm: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        execution_id = self.execution_id

        started_at = self.started_at.isoformat()

        duration_seconds = self.duration_seconds

        num_documents = self.num_documents

        num_clusters = self.num_clusters

        status = self.status

        algorithm = self.algorithm

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "execution_id": execution_id,
                "started_at": started_at,
                "duration_seconds": duration_seconds,
                "num_documents": num_documents,
                "num_clusters": num_clusters,
                "status": status,
                "algorithm": algorithm,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        execution_id = d.pop("execution_id")

        started_at = isoparse(d.pop("started_at"))

        duration_seconds = d.pop("duration_seconds")

        num_documents = d.pop("num_documents")

        num_clusters = d.pop("num_clusters")

        status = d.pop("status")

        algorithm = d.pop("algorithm")

        cluster_execution_metric = cls(
            execution_id=execution_id,
            started_at=started_at,
            duration_seconds=duration_seconds,
            num_documents=num_documents,
            num_clusters=num_clusters,
            status=status,
            algorithm=algorithm,
        )

        cluster_execution_metric.additional_properties = d
        return cluster_execution_metric

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
