from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GoogleDriveServiceAccountCredentials")


@_attrs_define
class GoogleDriveServiceAccountCredentials:
    """Credentials for Google Drive service account authentication.

    Service accounts provide server-to-server authentication for Google Drive
    without requiring user interaction. They are ideal for automated sync operations.

    Prerequisites:
        - Create a service account in Google Cloud Console
        - Enable Google Drive API for the project
        - Download the JSON key file
        - Share target Drive files/folders with the service account email

    Security:
        - private_key field is encrypted at rest using MongoDB client-side field level encryption
        - Credentials never appear in logs or API responses
        - Use domain-wide delegation for G Suite environments

    Use Cases:
        - Automated ingestion pipelines from shared drives
        - Scheduled sync operations without user interaction
        - Service-to-service integration for enterprise deployments

        Attributes:
            project_id (str): REQUIRED. Google Cloud project ID where the service account was created. Found in the JSON key
                file as 'project_id'. Format: lowercase alphanumeric with hyphens (e.g., 'my-project-123').
            private_key_id (str): REQUIRED. Unique identifier for the private key. Found in the JSON key file as
                'private_key_id'. Format: 40-character hexadecimal string.
            private_key (str): REQUIRED. PEM-encoded RSA private key for authentication. Found in the JSON key file as
                'private_key'. SECURITY: This field is encrypted at rest. Never log or expose this value. Format: Must include
                BEGIN/END PRIVATE KEY markers.
            client_email (str): REQUIRED. Service account email address. Found in the JSON key file as 'client_email'. Share
                Drive files/folders with this email to grant access. Format: {account-name}@{project-id}.iam.gserviceaccount.com
            client_id (str): REQUIRED. Numeric service account identifier. Found in the JSON key file as 'client_id'.
                Format: 21-digit numeric string.
            type_ (Literal['service_account'] | Unset):  Default: 'service_account'.
    """

    project_id: str
    private_key_id: str
    private_key: str
    client_email: str
    client_id: str
    type_: Literal["service_account"] | Unset = "service_account"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_id = self.project_id

        private_key_id = self.private_key_id

        private_key = self.private_key

        client_email = self.client_email

        client_id = self.client_id

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "project_id": project_id,
                "private_key_id": private_key_id,
                "private_key": private_key,
                "client_email": client_email,
                "client_id": client_id,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        project_id = d.pop("project_id")

        private_key_id = d.pop("private_key_id")

        private_key = d.pop("private_key")

        client_email = d.pop("client_email")

        client_id = d.pop("client_id")

        type_ = cast(Literal["service_account"] | Unset, d.pop("type", UNSET))
        if type_ != "service_account" and not isinstance(type_, Unset):
            raise ValueError(f"type must match const 'service_account', got '{type_}'")

        google_drive_service_account_credentials = cls(
            project_id=project_id,
            private_key_id=private_key_id,
            private_key=private_key,
            client_email=client_email,
            client_id=client_id,
            type_=type_,
        )

        google_drive_service_account_credentials.additional_properties = d
        return google_drive_service_account_credentials

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
