from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UpdateSecretRequest")


@_attrs_define
class UpdateSecretRequest:
    """Request to update an existing secret in the organization vault.

    Updates the encrypted value of an existing secret. The old value is
    permanently overwritten with no history or rollback capability.

    **Use Cases**:
    - Rotate API keys periodically for security
    - Update expired tokens
    - Change credentials after security incident
    - Switch from test to production keys

    **Security**:
    - Old value is permanently overwritten (no history)
    - New value is encrypted before storage
    - No rollback or undo capability
    - Update is logged for audit trail

    **Requirements**:
    - secret_value: REQUIRED, new plaintext value
    - Secret must already exist (use POST to create)

    **Permissions**: Requires ADMIN permission to update secrets.

        Attributes:
            secret_value (str): REQUIRED. New plaintext value for the secret. This will replace the existing encrypted
                value. The old value is permanently overwritten with no history. The new value will be encrypted at rest using
                Fernet encryption. Use this to rotate keys, update expired tokens, or change credentials. Format: any string
                (will be encrypted as-is).
    """

    secret_value: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        secret_value = self.secret_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "secret_value": secret_value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        secret_value = d.pop("secret_value")

        update_secret_request = cls(
            secret_value=secret_value,
        )

        update_secret_request.additional_properties = d
        return update_secret_request

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
