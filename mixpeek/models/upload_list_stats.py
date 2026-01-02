from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.upload_list_stats_uploads_by_status import UploadListStatsUploadsByStatus


T = TypeVar("T", bound="UploadListStats")


@_attrs_define
class UploadListStats:
    """Aggregate statistics for a list of uploads.

    Attributes:
        total_uploads (int): Total number of uploads in the result set
        total_size_bytes (int): Total size of all files in bytes
        uploads_by_status (UploadListStatsUploadsByStatus): Count of uploads grouped by status
        avg_file_size_bytes (float): Average file size across all uploads
        unique_buckets (int): Number of unique buckets in the result set
    """

    total_uploads: int
    total_size_bytes: int
    uploads_by_status: UploadListStatsUploadsByStatus
    avg_file_size_bytes: float
    unique_buckets: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_uploads = self.total_uploads

        total_size_bytes = self.total_size_bytes

        uploads_by_status = self.uploads_by_status.to_dict()

        avg_file_size_bytes = self.avg_file_size_bytes

        unique_buckets = self.unique_buckets

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_uploads": total_uploads,
                "total_size_bytes": total_size_bytes,
                "uploads_by_status": uploads_by_status,
                "avg_file_size_bytes": avg_file_size_bytes,
                "unique_buckets": unique_buckets,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.upload_list_stats_uploads_by_status import UploadListStatsUploadsByStatus

        d = dict(src_dict)
        total_uploads = d.pop("total_uploads")

        total_size_bytes = d.pop("total_size_bytes")

        uploads_by_status = UploadListStatsUploadsByStatus.from_dict(d.pop("uploads_by_status"))

        avg_file_size_bytes = d.pop("avg_file_size_bytes")

        unique_buckets = d.pop("unique_buckets")

        upload_list_stats = cls(
            total_uploads=total_uploads,
            total_size_bytes=total_size_bytes,
            uploads_by_status=uploads_by_status,
            avg_file_size_bytes=avg_file_size_bytes,
            unique_buckets=unique_buckets,
        )

        upload_list_stats.additional_properties = d
        return upload_list_stats

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
