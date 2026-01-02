from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SharePointDelegatedCredentials")


@_attrs_define
class SharePointDelegatedCredentials:
    """SharePoint/OneDrive delegated (user) authentication via OAuth2.

    Delegated flow provides access on behalf of a specific user.
    Useful when you need to access files with user-level permissions.

    Prerequisites:
        1. Register an application in Azure AD
        2. Grant Microsoft Graph API permissions:
           - Sites.Read.All (Delegated) or Sites.Selected
           - Files.Read.All (Delegated) or Files.Read
        3. Configure redirect URI for OAuth flow
        4. Complete OAuth consent to obtain refresh token

    Security:
        - client_secret and refresh_token encrypted at rest
        - Access scoped to what the consenting user can access
        - Refresh tokens can be revoked by user or admin

    Use Cases:
        - Personal OneDrive access
        - User-specific SharePoint sites
        - Respecting per-user permissions

        Attributes:
            tenant_id (str): REQUIRED. Azure AD tenant ID. Use 'common' for multi-tenant apps, or specific tenant ID for
                single-tenant.
            client_id (str): REQUIRED. Azure AD application (client) ID.
            client_secret (str): REQUIRED. Azure AD client secret. SECURITY: Encrypted at rest via CSFLE.
            refresh_token (str): REQUIRED. OAuth2 refresh token obtained from consent flow. SECURITY: Encrypted at rest. Can
                be revoked by user. Obtain via: Complete OAuth flow with Files.Read.All scope.
            type_ (Literal['delegated'] | Unset):  Default: 'delegated'.
    """

    tenant_id: str
    client_id: str
    client_secret: str
    refresh_token: str
    type_: Literal["delegated"] | Unset = "delegated"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tenant_id = self.tenant_id

        client_id = self.client_id

        client_secret = self.client_secret

        refresh_token = self.refresh_token

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tenant_id": tenant_id,
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
        tenant_id = d.pop("tenant_id")

        client_id = d.pop("client_id")

        client_secret = d.pop("client_secret")

        refresh_token = d.pop("refresh_token")

        type_ = cast(Literal["delegated"] | Unset, d.pop("type", UNSET))
        if type_ != "delegated" and not isinstance(type_, Unset):
            raise ValueError(f"type must match const 'delegated', got '{type_}'")

        share_point_delegated_credentials = cls(
            tenant_id=tenant_id,
            client_id=client_id,
            client_secret=client_secret,
            refresh_token=refresh_token,
            type_=type_,
        )

        share_point_delegated_credentials.additional_properties = d
        return share_point_delegated_credentials

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
