from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateBatchRequest")


@_attrs_define
class CreateBatchRequest:
    """Request model for creating a new batch.

    Batches group bucket objects for processing into collections. When you submit a batch,
    all objects in the batch are processed through the collections associated with the bucket.

    - object_ids: REQUIRED. List of object IDs that exist in the bucket
    - Collections are auto-discovered from the bucket at batch creation time

    Batch Processing Flow:
    1. Create batch with object_ids → Batch created in DRAFT status, collections auto-discovered
    2. Submit batch → Processing begins for discovered collections
    3. Collections with collection sources (tier 2/3) are processed automatically
    4. Processing happens in topological order based on collection dependencies

    Examples:
        Single object batch:
        {"object_ids": ["obj_123"]}

        Multiple objects batch:
        {"object_ids": ["obj_123", "obj_456", "obj_789"]}

        Attributes:
            object_ids (list[str]): REQUIRED. List of object IDs to include in the batch. Objects must exist in the bucket
                where the batch is created. Minimum 1 object, no maximum limit. All objects will be processed when the batch is
                submitted. Collections with collection sources (decomposition trees) are processed automatically via DAG
                resolution - no need to create separate batches.
    """

    object_ids: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_ids = self.object_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object_ids": object_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        object_ids = cast(list[str], d.pop("object_ids"))

        create_batch_request = cls(
            object_ids=object_ids,
        )

        create_batch_request.additional_properties = d
        return create_batch_request

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
