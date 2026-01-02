from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InstantiateClusterTemplateRequest")


@_attrs_define
class InstantiateClusterTemplateRequest:
    """Request to instantiate a cluster from a template.

    Attributes:
        cluster_name (str): Name for the new cluster
        collection_ids (list[str]): Collection IDs to use for the cluster
        description (None | str | Unset): Optional description override for the cluster
    """

    cluster_name: str
    collection_ids: list[str]
    description: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cluster_name = self.cluster_name

        collection_ids = self.collection_ids

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cluster_name": cluster_name,
                "collection_ids": collection_ids,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cluster_name = d.pop("cluster_name")

        collection_ids = cast(list[str], d.pop("collection_ids"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        instantiate_cluster_template_request = cls(
            cluster_name=cluster_name,
            collection_ids=collection_ids,
            description=description,
        )

        instantiate_cluster_template_request.additional_properties = d
        return instantiate_cluster_template_request

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
