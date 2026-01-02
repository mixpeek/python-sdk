from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="S3AccessKeyCredentials")


@_attrs_define
class S3AccessKeyCredentials:
    """AWS S3 access key and secret credentials.

    Access keys provide programmatic access to S3 buckets using long-lived credentials.
    This authentication method is straightforward but less secure than IAM role assumption.

    Prerequisites:
        - IAM user or role with S3 access permissions
        - Access key and secret key generated in AWS Console
        - Appropriate bucket policies or IAM policies configured

    Security Considerations:
        - Access keys are long-lived and don't automatically expire
        - secret_access_key is encrypted at rest but should be rotated regularly
        - Consider using IAM role assumption (S3RoleCredentials) for production
        - Never commit access keys to version control

    Use Cases:
        - Quick prototyping and development
        - Testing S3 integrations
        - Temporary credentials with session_token for enhanced security
        - Accessing S3-compatible services (MinIO, DigitalOcean Spaces)

    Recommended Alternative:
        For production deployments, use S3RoleCredentials with IAM role assumption
        instead of access keys for better security and credential management.

        Attributes:
            access_key_id (str): REQUIRED. AWS access key ID for authentication. Format: 20-character alphanumeric string
                starting with 'AKIA' (long-term) or 'ASIA' (temporary). Obtain from: AWS Console > IAM > Users > Security
                Credentials
            secret_access_key (str): REQUIRED. AWS secret access key for authentication. SECURITY: This field is encrypted
                at rest. Never log or expose this value. Format: 40-character base64-encoded string. Obtain from: AWS Console
                when creating/viewing access key (shown only once)
            type_ (Literal['access_key'] | Unset):  Default: 'access_key'.
            session_token (None | str | Unset): NOT REQUIRED. Temporary session token for AWS STS credentials. REQUIRED when
                using temporary security credentials from AWS STS. NOT REQUIRED for long-term IAM user access keys. SECURITY:
                Encrypted at rest. Automatically expires after session duration. Format: Base64-encoded string, typically
                several hundred characters. Use case: Enhanced security with automatic credential rotation
    """

    access_key_id: str
    secret_access_key: str
    type_: Literal["access_key"] | Unset = "access_key"
    session_token: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_key_id = self.access_key_id

        secret_access_key = self.secret_access_key

        type_ = self.type_

        session_token: None | str | Unset
        if isinstance(self.session_token, Unset):
            session_token = UNSET
        else:
            session_token = self.session_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "access_key_id": access_key_id,
                "secret_access_key": secret_access_key,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if session_token is not UNSET:
            field_dict["session_token"] = session_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access_key_id = d.pop("access_key_id")

        secret_access_key = d.pop("secret_access_key")

        type_ = cast(Literal["access_key"] | Unset, d.pop("type", UNSET))
        if type_ != "access_key" and not isinstance(type_, Unset):
            raise ValueError(f"type must match const 'access_key', got '{type_}'")

        def _parse_session_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        session_token = _parse_session_token(d.pop("session_token", UNSET))

        s3_access_key_credentials = cls(
            access_key_id=access_key_id,
            secret_access_key=secret_access_key,
            type_=type_,
            session_token=session_token,
        )

        s3_access_key_credentials.additional_properties = d
        return s3_access_key_credentials

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
