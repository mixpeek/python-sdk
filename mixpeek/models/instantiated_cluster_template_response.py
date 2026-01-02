from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="InstantiatedClusterTemplateResponse")


@_attrs_define
class InstantiatedClusterTemplateResponse:
    """Response after instantiating a cluster template.

    Attributes:
        cluster_id (str): ID of the created cluster
        cluster_name (str): Name of the created cluster
        template_id (str): ID of the template used
        status (str | Unset): Status of the instantiation Default: 'created'.
        created_at (datetime.datetime | Unset): Timestamp when cluster was created
    """

    cluster_id: str
    cluster_name: str
    template_id: str
    status: str | Unset = "created"
    created_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cluster_id = self.cluster_id

        cluster_name = self.cluster_name

        template_id = self.template_id

        status = self.status

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cluster_id": cluster_id,
                "cluster_name": cluster_name,
                "template_id": template_id,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cluster_id = d.pop("cluster_id")

        cluster_name = d.pop("cluster_name")

        template_id = d.pop("template_id")

        status = d.pop("status", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        instantiated_cluster_template_response = cls(
            cluster_id=cluster_id,
            cluster_name=cluster_name,
            template_id=template_id,
            status=status,
            created_at=created_at,
        )

        instantiated_cluster_template_response.additional_properties = d
        return instantiated_cluster_template_response

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
