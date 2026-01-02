from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.share_point_client_credentials import SharePointClientCredentials
    from ..models.share_point_delegated_credentials import SharePointDelegatedCredentials


T = TypeVar("T", bound="SharePointConfig")


@_attrs_define
class SharePointConfig:
    """Microsoft SharePoint and OneDrive for Business configuration.

    Enables Mixpeek to connect to SharePoint sites, document libraries, and
    OneDrive for Business for automated file ingestion and synchronization.

    Architecture:
        SharePoint hierarchy: Tenant → Sites → Drives (Document Libraries) → Items
        - site_id: Identifies the SharePoint site
        - drive_id: Identifies a specific document library within the site
        - folder_path: Path within the document library

    Authentication Methods:
        1. Client Credentials (RECOMMENDED for production):
            - App-only access without user interaction
            - Requires admin consent for Graph API permissions
            - Access level determined by app permissions

        2. Delegated:
            - User-level access via OAuth consent
            - Access limited to user's permissions
            - Requires refresh token management

    Requirements:
        - Azure AD application registration
        - Microsoft Graph API permissions (Sites.Read.All, Files.Read.All)
        - Network connectivity to graph.microsoft.com

    Use Cases:
        - Sync SharePoint document libraries
        - Ingest enterprise collaboration files
        - Monitor and process uploaded documents
        - Archive compliance-sensitive materials

    Example:
        ```python
        config = {
            "provider_type": "sharepoint",
            "credentials": {
                "type": "client_credentials",
                "tenant_id": "12345678-...",
                "client_id": "87654321-...",
                "client_secret": "your-secret",
            },
            "site_id": "contoso.sharepoint.com,guid1,guid2",
            "drive_id": "b!abc123...",
            "folder_path": "/Shared Documents/Marketing",
        }
        ```

        Attributes:
            credentials (SharePointClientCredentials | SharePointDelegatedCredentials): REQUIRED. Azure AD authentication
                credentials. Choose client_credentials for production (app-only) or delegated for user-level access. The 'type'
                field determines which authentication flow is used.
            provider_type (Literal['sharepoint'] | Unset):  Default: 'sharepoint'.
            site_id (None | str | Unset): NOT REQUIRED if using personal OneDrive. SharePoint site identifier for targeting
                a specific site. Format: '{hostname},{site-collection-id},{web-id}' or site URL. Find via: Microsoft Graph API
                GET /sites?search={keyword} Example: 'contoso.sharepoint.com,12345678-...,87654321-...'
            drive_id (None | str | Unset): NOT REQUIRED if you want to use the default document library. Specific drive
                (document library) ID within the site. Find via: GET /sites/{site-id}/drives Format: Base64-encoded ID starting
                with 'b!'
            folder_path (None | str | Unset): NOT REQUIRED. Path within the drive to sync from. If omitted, syncs from the
                root of the drive. Format: Forward-slash separated path (e.g., '/Documents/Marketing'). Note: Leading slash is
                optional.
    """

    credentials: SharePointClientCredentials | SharePointDelegatedCredentials
    provider_type: Literal["sharepoint"] | Unset = "sharepoint"
    site_id: None | str | Unset = UNSET
    drive_id: None | str | Unset = UNSET
    folder_path: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.share_point_client_credentials import SharePointClientCredentials

        credentials: dict[str, Any]
        if isinstance(self.credentials, SharePointClientCredentials):
            credentials = self.credentials.to_dict()
        else:
            credentials = self.credentials.to_dict()

        provider_type = self.provider_type

        site_id: None | str | Unset
        if isinstance(self.site_id, Unset):
            site_id = UNSET
        else:
            site_id = self.site_id

        drive_id: None | str | Unset
        if isinstance(self.drive_id, Unset):
            drive_id = UNSET
        else:
            drive_id = self.drive_id

        folder_path: None | str | Unset
        if isinstance(self.folder_path, Unset):
            folder_path = UNSET
        else:
            folder_path = self.folder_path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "credentials": credentials,
            }
        )
        if provider_type is not UNSET:
            field_dict["provider_type"] = provider_type
        if site_id is not UNSET:
            field_dict["site_id"] = site_id
        if drive_id is not UNSET:
            field_dict["drive_id"] = drive_id
        if folder_path is not UNSET:
            field_dict["folder_path"] = folder_path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.share_point_client_credentials import SharePointClientCredentials
        from ..models.share_point_delegated_credentials import SharePointDelegatedCredentials

        d = dict(src_dict)

        def _parse_credentials(data: object) -> SharePointClientCredentials | SharePointDelegatedCredentials:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                credentials_type_0 = SharePointClientCredentials.from_dict(data)

                return credentials_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            credentials_type_1 = SharePointDelegatedCredentials.from_dict(data)

            return credentials_type_1

        credentials = _parse_credentials(d.pop("credentials"))

        provider_type = cast(Literal["sharepoint"] | Unset, d.pop("provider_type", UNSET))
        if provider_type != "sharepoint" and not isinstance(provider_type, Unset):
            raise ValueError(f"provider_type must match const 'sharepoint', got '{provider_type}'")

        def _parse_site_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        site_id = _parse_site_id(d.pop("site_id", UNSET))

        def _parse_drive_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        drive_id = _parse_drive_id(d.pop("drive_id", UNSET))

        def _parse_folder_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        folder_path = _parse_folder_path(d.pop("folder_path", UNSET))

        share_point_config = cls(
            credentials=credentials,
            provider_type=provider_type,
            site_id=site_id,
            drive_id=drive_id,
            folder_path=folder_path,
        )

        share_point_config.additional_properties = d
        return share_point_config

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
