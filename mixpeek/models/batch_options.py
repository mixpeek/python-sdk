from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BatchOptions")


@_attrs_define
class BatchOptions:
    """Options for batch processing in migration.

    Attributes:
        batch_size (int | Unset): Documents per batch Default: 100.
        max_workers (int | Unset): Maximum parallel workers Default: 10.
        retry_failed (bool | Unset): Retry failed batches Default: True.
    """

    batch_size: int | Unset = 100
    max_workers: int | Unset = 10
    retry_failed: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        batch_size = self.batch_size

        max_workers = self.max_workers

        retry_failed = self.retry_failed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if batch_size is not UNSET:
            field_dict["batch_size"] = batch_size
        if max_workers is not UNSET:
            field_dict["max_workers"] = max_workers
        if retry_failed is not UNSET:
            field_dict["retry_failed"] = retry_failed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        batch_size = d.pop("batch_size", UNSET)

        max_workers = d.pop("max_workers", UNSET)

        retry_failed = d.pop("retry_failed", UNSET)

        batch_options = cls(
            batch_size=batch_size,
            max_workers=max_workers,
            retry_failed=retry_failed,
        )

        batch_options.additional_properties = d
        return batch_options

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
