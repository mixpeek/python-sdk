from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateSecretRequest")


@_attrs_define
class CreateSecretRequest:
    """Request to create a new secret in the organization vault.

    Secrets are encrypted at rest using Fernet encryption and stored in the
    organization document. Use secrets to securely store API keys, tokens,
    and credentials for external services.

    **Use Cases**:
    - Store API keys for Stripe, GitHub, OpenAI, etc.
    - Manage authentication tokens for api_call retriever stage
    - Store credentials for third-party integrations

    **Security**:
    - Secret values are encrypted using ENCRYPTION_KEY from environment
    - Decrypted values are NEVER returned in API responses
    - Only secret names are exposed in list operations
    - Access is logged for audit trail

    **Requirements**:
    - secret_name: REQUIRED, must be unique within organization
    - secret_value: REQUIRED, plaintext value to encrypt

    **Permissions**: Requires ADMIN permission to create secrets.

        Attributes:
            secret_name (str): REQUIRED. Name/key for the secret. Use descriptive names that indicate the service and
                purpose. Must be unique within the organization. Format: lowercase with underscores (e.g., 'stripe_api_key').
                Common patterns: '{service}_{type}_{environment}' like 'stripe_api_key_prod'. This name is used to reference the
                secret in api_call stage configuration. Examples: 'stripe_api_key', 'github_token', 'openai_api_key',
                'weather_api_key'.
            secret_value (str): REQUIRED. Plaintext secret value to encrypt and store. This value will be encrypted at rest
                using Fernet encryption. The encrypted value is stored in MongoDB with the organization document. The plaintext
                value is NEVER logged or exposed in API responses. Only the secret name is visible when listing secrets. Use
                this field to store: API keys, tokens, passwords, credentials. Format: any string (will be encrypted as-is). For
                Basic auth, use format 'username:password'.
    """

    secret_name: str
    secret_value: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        secret_name = self.secret_name

        secret_value = self.secret_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "secret_name": secret_name,
                "secret_value": secret_value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        secret_name = d.pop("secret_name")

        secret_value = d.pop("secret_value")

        create_secret_request = cls(
            secret_name=secret_name,
            secret_value=secret_value,
        )

        create_secret_request.additional_properties = d
        return create_secret_request

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
