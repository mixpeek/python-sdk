from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.google_drive_o_auth_credentials import GoogleDriveOAuthCredentials
    from ..models.google_drive_service_account_credentials import GoogleDriveServiceAccountCredentials


T = TypeVar("T", bound="GoogleDriveConfig")


@_attrs_define
class GoogleDriveConfig:
    """Google Drive and Google Workspace shared drive configuration.

    This configuration enables Mixpeek to connect to Google Drive for automated
    file ingestion and synchronization. Supports both personal Drive and Google
    Workspace shared drives (formerly Team Drives).

    Authentication Options:
        - Service Account: Recommended for production. No user interaction required.
        - OAuth2: Suitable for personal Drive access or development.

    Requirements:
        - Google Drive API enabled in Google Cloud Console
        - Appropriate authentication credentials configured
        - Files/folders shared with the service account or OAuth user
        - Network connectivity to drive.googleapis.com

    Use Cases:
        - Sync marketing materials from shared drives
        - Ingest documents from team collaboration folders
        - Monitor and process uploaded media files
        - Archive and search historical documents

        Attributes:
            credentials (GoogleDriveOAuthCredentials | GoogleDriveServiceAccountCredentials): REQUIRED. Authentication
                credentials for Google Drive API access. Choose service_account for production (recommended) or oauth for
                personal access. The 'type' field determines which credential type is used.
            provider_type (Literal['google_drive'] | Unset):  Default: 'google_drive'.
            shared_drive_id (None | str | Unset): NOT REQUIRED. Google Workspace shared drive (Team Drive) identifier. When
                provided, sync operations are scoped to this shared drive only. When omitted, syncs from 'My Drive' of the
                authenticated account. Find ID: Open shared drive in browser, copy ID from URL. Format: 0A{alphanumeric-string}
            impersonate_user (None | str | Unset): NOT REQUIRED. Email address to impersonate when using service account
                credentials. Requires domain-wide delegation to be enabled for the service account. Used in G Suite environments
                to access files as a specific user. When omitted, uses the service account's own access. Format: Valid email
                address in the G Suite domain.
    """

    credentials: GoogleDriveOAuthCredentials | GoogleDriveServiceAccountCredentials
    provider_type: Literal["google_drive"] | Unset = "google_drive"
    shared_drive_id: None | str | Unset = UNSET
    impersonate_user: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.google_drive_service_account_credentials import GoogleDriveServiceAccountCredentials

        credentials: dict[str, Any]
        if isinstance(self.credentials, GoogleDriveServiceAccountCredentials):
            credentials = self.credentials.to_dict()
        else:
            credentials = self.credentials.to_dict()

        provider_type = self.provider_type

        shared_drive_id: None | str | Unset
        if isinstance(self.shared_drive_id, Unset):
            shared_drive_id = UNSET
        else:
            shared_drive_id = self.shared_drive_id

        impersonate_user: None | str | Unset
        if isinstance(self.impersonate_user, Unset):
            impersonate_user = UNSET
        else:
            impersonate_user = self.impersonate_user

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "credentials": credentials,
            }
        )
        if provider_type is not UNSET:
            field_dict["provider_type"] = provider_type
        if shared_drive_id is not UNSET:
            field_dict["shared_drive_id"] = shared_drive_id
        if impersonate_user is not UNSET:
            field_dict["impersonate_user"] = impersonate_user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.google_drive_o_auth_credentials import GoogleDriveOAuthCredentials
        from ..models.google_drive_service_account_credentials import GoogleDriveServiceAccountCredentials

        d = dict(src_dict)

        def _parse_credentials(data: object) -> GoogleDriveOAuthCredentials | GoogleDriveServiceAccountCredentials:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                credentials_type_0 = GoogleDriveServiceAccountCredentials.from_dict(data)

                return credentials_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            credentials_type_1 = GoogleDriveOAuthCredentials.from_dict(data)

            return credentials_type_1

        credentials = _parse_credentials(d.pop("credentials"))

        provider_type = cast(Literal["google_drive"] | Unset, d.pop("provider_type", UNSET))
        if provider_type != "google_drive" and not isinstance(provider_type, Unset):
            raise ValueError(f"provider_type must match const 'google_drive', got '{provider_type}'")

        def _parse_shared_drive_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        shared_drive_id = _parse_shared_drive_id(d.pop("shared_drive_id", UNSET))

        def _parse_impersonate_user(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        impersonate_user = _parse_impersonate_user(d.pop("impersonate_user", UNSET))

        google_drive_config = cls(
            credentials=credentials,
            provider_type=provider_type,
            shared_drive_id=shared_drive_id,
            impersonate_user=impersonate_user,
        )

        google_drive_config.additional_properties = d
        return google_drive_config

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
