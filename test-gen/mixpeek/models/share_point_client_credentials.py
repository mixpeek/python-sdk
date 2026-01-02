from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SharePointClientCredentials")


@_attrs_define
class SharePointClientCredentials:
    """SharePoint/OneDrive client credentials (app-only) authentication.

    Client credentials flow provides application-level access without user interaction.
    Recommended for automated sync operations in enterprise environments.

    Prerequisites:
        1. Register an application in Azure AD (portal.azure.com)
        2. Grant Microsoft Graph API permissions:
           - Sites.Read.All (Application) - for SharePoint site access
           - Files.Read.All (Application) - for file access
        3. Admin consent granted for the permissions
        4. Generate client secret

    Security:
        - client_secret encrypted at rest via CSFLE
        - Provides application-level access to all sites (based on permissions)
        - No user context - accesses files as the application itself
        - Consider using certificate-based auth for production

    Use Cases:
        - Automated enterprise-wide document ingestion
        - Background sync without user interaction
        - Multi-tenant applications with admin consent

        Attributes:
            tenant_id (str): REQUIRED. Azure AD tenant ID (directory ID). Find in: Azure Portal > Azure Active Directory >
                Overview. Format: UUID (e.g., '12345678-1234-1234-1234-123456789abc')
            client_id (str): REQUIRED. Azure AD application (client) ID. Find in: Azure Portal > App Registrations > Your
                App > Overview. Format: UUID
            client_secret (str): REQUIRED. Azure AD client secret for authentication. SECURITY: This field is encrypted at
                rest via CSFLE. Never log or expose. Generate in: Azure Portal > App Registrations > Your App > Certificates &
                secrets. Note: Secrets expire; consider using certificates for production.
            type_ (Literal['client_credentials'] | Unset):  Default: 'client_credentials'.
    """

    tenant_id: str
    client_id: str
    client_secret: str
    type_: Literal["client_credentials"] | Unset = "client_credentials"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tenant_id = self.tenant_id

        client_id = self.client_id

        client_secret = self.client_secret

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tenant_id": tenant_id,
                "client_id": client_id,
                "client_secret": client_secret,
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

        type_ = cast(Literal["client_credentials"] | Unset, d.pop("type", UNSET))
        if type_ != "client_credentials" and not isinstance(type_, Unset):
            raise ValueError(f"type must match const 'client_credentials', got '{type_}'")

        share_point_client_credentials = cls(
            tenant_id=tenant_id,
            client_id=client_id,
            client_secret=client_secret,
            type_=type_,
        )

        share_point_client_credentials.additional_properties = d
        return share_point_client_credentials

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
