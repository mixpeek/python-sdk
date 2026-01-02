from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SecretsListResponse")


@_attrs_define
class SecretsListResponse:
    """Response for listing secrets in the organization vault.

    Returns ONLY secret names, never decrypted values. Use this endpoint to
    discover which secrets are configured in your organization.

    **Security**:
    - Returns ONLY secret names, never values
    - Decrypted values never exposed via API
    - Use for auditing which secrets are configured

    **Use Cases**:
    - Discover which secrets are configured
    - Audit secret inventory
    - Check if a secret exists before using it
    - Verify secret name spelling before referencing in api_call

    **Permissions**: Requires READ permission to list secrets.

        Attributes:
            secrets (list[str]): List of secret names in the organization vault. Only names are returned, never decrypted
                values. Use these names as references in api_call stage configuration. Names are unique within the organization.
                Empty list if no secrets are configured.
            count (int): Total number of secrets in the organization vault. This is the length of the secrets array. Useful
                for monitoring and auditing secret inventory.
    """

    secrets: list[str]
    count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        secrets = self.secrets

        count = self.count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "secrets": secrets,
                "count": count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        secrets = cast(list[str], d.pop("secrets"))

        count = d.pop("count")

        secrets_list_response = cls(
            secrets=secrets,
            count=count,
        )

        secrets_list_response.additional_properties = d
        return secrets_list_response

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
