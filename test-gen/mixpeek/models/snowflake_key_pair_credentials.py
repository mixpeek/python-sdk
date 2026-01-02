from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SnowflakeKeyPairCredentials")


@_attrs_define
class SnowflakeKeyPairCredentials:
    """Snowflake key pair authentication (RECOMMENDED for production).

    Key pair authentication provides secure, password-less access to Snowflake.
    The private key is encrypted at rest using MongoDB CSFLE.

    Prerequisites:
        1. Generate RSA key pair (2048-bit minimum)
        2. Extract public key and assign to Snowflake user
        3. Store private key securely (encrypted)

    Security:
        - Private key encrypted at rest via CSFLE
        - No password exposure
        - Key rotation supported
        - Recommended for production

    Example:
        Generate key pair:
        ```bash
        openssl genrsa 2048 | openssl pkcs8 -topk8 -inform PEM -out rsa_key.p8 -nocrypt
        openssl rsa -in rsa_key.p8 -pubout -out rsa_key.pub
        ```

        Assign public key to Snowflake user:
        ```sql
        ALTER USER mixpeek_sync SET RSA_PUBLIC_KEY='MIIBIjANBg...';
        ```

        Attributes:
            username (str): Snowflake username for authentication
            private_key (str): REQUIRED. PEM-encoded RSA private key for authentication. SECURITY: This field is encrypted
                at rest via CSFLE. Never log or expose. Format: -----BEGIN PRIVATE KEY-----...-----END PRIVATE KEY-----
            type_ (Literal['key_pair'] | Unset):  Default: 'key_pair'.
            private_key_passphrase (None | str | Unset): NOT REQUIRED. Passphrase for encrypted private key. SECURITY:
                Encrypted at rest if provided. Use only if private key is passphrase-protected.
    """

    username: str
    private_key: str
    type_: Literal["key_pair"] | Unset = "key_pair"
    private_key_passphrase: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        private_key = self.private_key

        type_ = self.type_

        private_key_passphrase: None | str | Unset
        if isinstance(self.private_key_passphrase, Unset):
            private_key_passphrase = UNSET
        else:
            private_key_passphrase = self.private_key_passphrase

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "username": username,
                "private_key": private_key,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if private_key_passphrase is not UNSET:
            field_dict["private_key_passphrase"] = private_key_passphrase

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        username = d.pop("username")

        private_key = d.pop("private_key")

        type_ = cast(Literal["key_pair"] | Unset, d.pop("type", UNSET))
        if type_ != "key_pair" and not isinstance(type_, Unset):
            raise ValueError(f"type must match const 'key_pair', got '{type_}'")

        def _parse_private_key_passphrase(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        private_key_passphrase = _parse_private_key_passphrase(d.pop("private_key_passphrase", UNSET))

        snowflake_key_pair_credentials = cls(
            username=username,
            private_key=private_key,
            type_=type_,
            private_key_passphrase=private_key_passphrase,
        )

        snowflake_key_pair_credentials.additional_properties = d
        return snowflake_key_pair_credentials

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
