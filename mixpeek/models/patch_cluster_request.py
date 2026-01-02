from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_cluster_request_metadata_type_0 import PatchClusterRequestMetadataType0


T = TypeVar("T", bound="PatchClusterRequest")


@_attrs_define
class PatchClusterRequest:
    """Request model for partially updating a cluster (PATCH operation).

    Attributes:
        cluster_name (None | str | Unset): Updated name for the cluster
        description (None | str | Unset): Updated description for the cluster
        metadata (None | PatchClusterRequestMetadataType0 | Unset): Updated metadata for the cluster
    """

    cluster_name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    metadata: None | PatchClusterRequestMetadataType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.patch_cluster_request_metadata_type_0 import PatchClusterRequestMetadataType0

        cluster_name: None | str | Unset
        if isinstance(self.cluster_name, Unset):
            cluster_name = UNSET
        else:
            cluster_name = self.cluster_name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, PatchClusterRequestMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cluster_name is not UNSET:
            field_dict["cluster_name"] = cluster_name
        if description is not UNSET:
            field_dict["description"] = description
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.patch_cluster_request_metadata_type_0 import PatchClusterRequestMetadataType0

        d = dict(src_dict)

        def _parse_cluster_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cluster_name = _parse_cluster_name(d.pop("cluster_name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_metadata(data: object) -> None | PatchClusterRequestMetadataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = PatchClusterRequestMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PatchClusterRequestMetadataType0 | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        patch_cluster_request = cls(
            cluster_name=cluster_name,
            description=description,
            metadata=metadata,
        )

        patch_cluster_request.additional_properties = d
        return patch_cluster_request

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
