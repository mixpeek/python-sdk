from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_taxonomy_request_metadata_type_0 import PatchTaxonomyRequestMetadataType0


T = TypeVar("T", bound="PatchTaxonomyRequest")


@_attrs_define
class PatchTaxonomyRequest:
    """Request to update a taxonomy's metadata.

    **IMPORTANT: Partial Updates with Controlled Mutability**

    This endpoint allows updating ONLY metadata fields. Core taxonomy logic is immutable
    to ensure consistency for join history and dependent resources.

    **✅ Fields You CAN Update (Metadata Only):**
    - `taxonomy_name`: Rename the taxonomy
    - `description`: Update documentation
    - `metadata`: Update custom metadata fields

    **❌ Fields You CANNOT Update (Immutable Core Logic):**
    - `config`: Taxonomy configuration (retriever_id, input_mappings, collections, hierarchy)
    - `taxonomy_type`: Type (flat vs hierarchical)
    - `retriever_id`: Associated retriever
    - `input_mappings`: Field mappings
    - `enrichment_fields`: Enrichment configuration

    **Need to Modify Core Logic?**
    Use POST /taxonomies/{taxonomy_id}/clone instead. Cloning creates a new taxonomy
    with a new ID, allowing you to:
    - Change retriever or input mappings
    - Modify enrichment fields
    - Update collection configuration
    - Change taxonomy hierarchy

    **Behavior:**
    - All fields are OPTIONAL - provide only what you want to update
    - Empty updates (no fields provided) will be rejected with 400 error
    - Original taxonomy remains unchanged (no destructive operations)

    **Why This Design?**
    - Join history is tied to specific taxonomy configuration
    - Changing retriever would invalidate previous joins
    - Version tracking enables auditing and rollback

        Attributes:
            taxonomy_name (None | str | Unset): Updated name for the taxonomy
            description (None | str | Unset): Updated description for the taxonomy
            metadata (None | PatchTaxonomyRequestMetadataType0 | Unset): Updated metadata for the taxonomy
    """

    taxonomy_name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    metadata: None | PatchTaxonomyRequestMetadataType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.patch_taxonomy_request_metadata_type_0 import PatchTaxonomyRequestMetadataType0

        taxonomy_name: None | str | Unset
        if isinstance(self.taxonomy_name, Unset):
            taxonomy_name = UNSET
        else:
            taxonomy_name = self.taxonomy_name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, PatchTaxonomyRequestMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if taxonomy_name is not UNSET:
            field_dict["taxonomy_name"] = taxonomy_name
        if description is not UNSET:
            field_dict["description"] = description
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.patch_taxonomy_request_metadata_type_0 import PatchTaxonomyRequestMetadataType0

        d = dict(src_dict)

        def _parse_taxonomy_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        taxonomy_name = _parse_taxonomy_name(d.pop("taxonomy_name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_metadata(data: object) -> None | PatchTaxonomyRequestMetadataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = PatchTaxonomyRequestMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PatchTaxonomyRequestMetadataType0 | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        patch_taxonomy_request = cls(
            taxonomy_name=taxonomy_name,
            description=description,
            metadata=metadata,
        )

        patch_taxonomy_request.additional_properties = d
        return patch_taxonomy_request

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
