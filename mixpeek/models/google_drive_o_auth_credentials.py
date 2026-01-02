from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GoogleDriveOAuthCredentials")


@_attrs_define
class GoogleDriveOAuthCredentials:
    """Credentials for Google Drive OAuth2 user authentication.

    OAuth2 credentials provide access to Google Drive on behalf of a specific user.
    This authentication method is suitable when accessing personal Drive files or
    when service account delegation is not available.

    Prerequisites:
        - Create OAuth 2.0 credentials in Google Cloud Console
        - Configure authorized redirect URIs
        - Complete OAuth consent flow to obtain refresh token
        - Ensure appropriate OAuth scopes are granted (drive.readonly or drive)

    Security:
        - client_secret and refresh_token are encrypted at rest
        - Access tokens are automatically refreshed and cached temporarily
        - Credentials are scoped to the user who granted consent

    Use Cases:
        - Personal Drive file access for individual users
        - Prototyping and development without service account setup
        - Environments where service account delegation is not feasible

    Limitations:
        - Requires user interaction during initial setup
        - Access is limited to files the consenting user can access
        - Refresh tokens can be revoked by the user

        Attributes:
            client_id (str): REQUIRED. OAuth 2.0 client ID from Google Cloud Console. Found in the API credentials section.
                Format: {id}.apps.googleusercontent.com
            client_secret (str): REQUIRED. OAuth 2.0 client secret from Google Cloud Console. SECURITY: This field is
                encrypted at rest. Never log or expose this value. Format: Alphanumeric string from Google Cloud Console.
            refresh_token (str): REQUIRED. Long-lived refresh token obtained during OAuth consent flow. Used to
                automatically obtain new access tokens without user interaction. SECURITY: Encrypted at rest. Can be revoked by
                user at any time. Obtain via: Complete OAuth flow with drive.readonly or drive scope.
            type_ (Literal['oauth'] | Unset):  Default: 'oauth'.
    """

    client_id: str
    client_secret: str
    refresh_token: str
    type_: Literal["oauth"] | Unset = "oauth"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client_id = self.client_id

        client_secret = self.client_secret

        refresh_token = self.refresh_token

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "client_id": client_id,
                "client_secret": client_secret,
                "refresh_token": refresh_token,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        client_id = d.pop("client_id")

        client_secret = d.pop("client_secret")

        refresh_token = d.pop("refresh_token")

        type_ = cast(Literal["oauth"] | Unset, d.pop("type", UNSET))
        if type_ != "oauth" and not isinstance(type_, Unset):
            raise ValueError(f"type must match const 'oauth', got '{type_}'")

        google_drive_o_auth_credentials = cls(
            client_id=client_id,
            client_secret=client_secret,
            refresh_token=refresh_token,
            type_=type_,
        )

        google_drive_o_auth_credentials.additional_properties = d
        return google_drive_o_auth_credentials

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
