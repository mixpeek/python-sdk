from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InstantiateTemplateRequest")


@_attrs_define
class InstantiateTemplateRequest:
    """Request to create a new namespace from a template.

    Instantiation clones all data from the template's source namespace including:
    - Namespace configuration (feature extractors, indexes)
    - Qdrant vectors and payloads (pre-computed embeddings)
    - MongoDB metadata (collections, documents)

    The process is fast (<5 seconds) because data is cloned, not reprocessed.

    Use Cases:
        - First-time user onboarding with working examples
        - Creating demo environments for sales/trials
        - Spinning up test environments with known data
        - Providing industry-specific starting points

    Requirements:
        - namespace_name: REQUIRED, must be unique within organization
        - description: OPTIONAL, defaults to template description if not provided

    Validation:
        - Checks namespace name uniqueness before creation
        - Validates template exists and is active
        - Ensures source namespace is accessible

        Attributes:
            namespace_name (str): Name for the new namespace. REQUIRED. Must be unique within your organization. Used as
                identifier and display name. Format: 3-50 characters, alphanumeric with underscores/hyphens, lowercase
                recommended. Cannot match existing namespace names.
            description (None | str | Unset): Optional description for the namespace. NOT REQUIRED. If not provided, uses
                the template's description. Useful for adding context about your specific use case. Format: 0-500 characters,
                plain text.
    """

    namespace_name: str
    description: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        namespace_name = self.namespace_name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "namespace_name": namespace_name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        namespace_name = d.pop("namespace_name")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        instantiate_template_request = cls(
            namespace_name=namespace_name,
            description=description,
        )

        instantiate_template_request.additional_properties = d
        return instantiate_template_request

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
