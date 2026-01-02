from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.clone_namespace_resources_config import CloneNamespaceResourcesConfig


T = TypeVar("T", bound="CloneNamespaceRequest")


@_attrs_define
class CloneNamespaceRequest:
    """Request to clone a namespace with all its data.

    Clone creates a full copy of a namespace including:
    - Namespace configuration (extractors, indexes)
    - Buckets (metadata, references same S3 files)
    - Collections (full copy of all vectors/embeddings)
    - Retrievers (pipeline configuration)

    **Use Cases:**
    - Create staging environment from production
    - Backup namespace with all data
    - Fork namespace for experimentation

    **For config-only copy (no data), use templates instead:**
    - POST /templates/namespaces/from-namespace/{id}
    - POST /templates/namespaces/{template_id}/instantiate

        Attributes:
            namespace_name (str): Name for the cloned namespace (must be unique)
            include_resources (CloneNamespaceResourcesConfig | None | Unset): Which resources to include. Defaults to
                collections + retrievers.
            description (None | str | Unset): Override description. If omitted, copies from source.
            source_organization_id (None | str | Unset): Source org ID for cross-org cloning (admin only).
    """

    namespace_name: str
    include_resources: CloneNamespaceResourcesConfig | None | Unset = UNSET
    description: None | str | Unset = UNSET
    source_organization_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.clone_namespace_resources_config import CloneNamespaceResourcesConfig

        namespace_name = self.namespace_name

        include_resources: dict[str, Any] | None | Unset
        if isinstance(self.include_resources, Unset):
            include_resources = UNSET
        elif isinstance(self.include_resources, CloneNamespaceResourcesConfig):
            include_resources = self.include_resources.to_dict()
        else:
            include_resources = self.include_resources

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        source_organization_id: None | str | Unset
        if isinstance(self.source_organization_id, Unset):
            source_organization_id = UNSET
        else:
            source_organization_id = self.source_organization_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "namespace_name": namespace_name,
            }
        )
        if include_resources is not UNSET:
            field_dict["include_resources"] = include_resources
        if description is not UNSET:
            field_dict["description"] = description
        if source_organization_id is not UNSET:
            field_dict["source_organization_id"] = source_organization_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.clone_namespace_resources_config import CloneNamespaceResourcesConfig

        d = dict(src_dict)
        namespace_name = d.pop("namespace_name")

        def _parse_include_resources(data: object) -> CloneNamespaceResourcesConfig | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                include_resources_type_0 = CloneNamespaceResourcesConfig.from_dict(data)

                return include_resources_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CloneNamespaceResourcesConfig | None | Unset, data)

        include_resources = _parse_include_resources(d.pop("include_resources", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_source_organization_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_organization_id = _parse_source_organization_id(d.pop("source_organization_id", UNSET))

        clone_namespace_request = cls(
            namespace_name=namespace_name,
            include_resources=include_resources,
            description=description,
            source_organization_id=source_organization_id,
        )

        clone_namespace_request.additional_properties = d
        return clone_namespace_request

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
