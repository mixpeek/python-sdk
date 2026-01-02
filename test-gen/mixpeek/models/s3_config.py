from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.s3_access_key_credentials import S3AccessKeyCredentials
    from ..models.s3_role_credentials import S3RoleCredentials


T = TypeVar("T", bound="S3Config")


@_attrs_define
class S3Config:
    """Amazon S3 and S3-compatible storage provider configuration.

    This configuration enables Mixpeek to connect to Amazon S3 or S3-compatible
    storage services (MinIO, DigitalOcean Spaces, Wasabi, Backblaze B2, etc.)
    for automated object ingestion and synchronization.

    Authentication Methods:
        1. IAM Role Assumption (RECOMMENDED for production):
            - Most secure option with automatic credential rotation
            - No long-lived credentials shared
            - Ideal for customer-owned S3 buckets

        2. Access Keys:
            - Simpler setup for development and testing
            - Works with S3-compatible services
            - Requires manual credential rotation

    Requirements:
        - Valid AWS credentials or IAM role configuration
        - S3 bucket with appropriate permissions (s3:GetObject, s3:ListBucket)
        - Network connectivity to S3 endpoint
        - Correct region configuration

    Supported Services:
        - Amazon S3 (all regions)
        - MinIO (self-hosted or cloud)
        - DigitalOcean Spaces
        - Wasabi Cloud Storage
        - Backblaze B2
        - Any S3-compatible storage with compatible API

    Use Cases:
        - Ingest videos from data lakes
        - Sync images from marketing asset buckets
        - Process documents from archive storage
        - Monitor and index uploaded files
        - Backup and disaster recovery workflows

        Attributes:
            credentials (S3AccessKeyCredentials | S3RoleCredentials): REQUIRED. AWS authentication credentials
                configuration. Choose 'iam_role' for production deployments (recommended) or 'access_key' for development,
                testing, or S3-compatible services. The 'type' field determines which credential mechanism is used.
            region (str): REQUIRED. AWS region where the S3 bucket is located. Must match the bucket's actual region to
                avoid routing errors. For S3-compatible services, use their documented region value or 'us-east-1' as a default
                if regions are not applicable. Format: AWS region code (e.g., us-east-1, eu-west-1)
            provider_type (Literal['s3'] | Unset):  Default: 's3'.
            endpoint_url (None | str | Unset): NOT REQUIRED for AWS S3 (uses default AWS endpoints). REQUIRED for
                S3-compatible services to specify custom endpoint URL. Must be a valid HTTPS or HTTP URL without trailing slash.
                Examples: - MinIO: https://minio.example.com - DigitalOcean Spaces: https://nyc3.digitaloceanspaces.com -
                Wasabi: https://s3.wasabisys.com
            use_ssl (bool | Unset): Whether to use TLS/SSL encryption for connections to S3. RECOMMENDED: Always True for
                production environments. Set to False only for local development with unencrypted endpoints. Default: True
                Default: True.
            verify_ssl (bool | Unset): Whether to verify TLS/SSL certificates when connecting. RECOMMENDED: Always True for
                production to prevent MITM attacks. Set to False only for development with self-signed certificates. Requires
                use_ssl=True to have any effect. Default: True Default: True.
    """

    credentials: S3AccessKeyCredentials | S3RoleCredentials
    region: str
    provider_type: Literal["s3"] | Unset = "s3"
    endpoint_url: None | str | Unset = UNSET
    use_ssl: bool | Unset = True
    verify_ssl: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.s3_access_key_credentials import S3AccessKeyCredentials

        credentials: dict[str, Any]
        if isinstance(self.credentials, S3AccessKeyCredentials):
            credentials = self.credentials.to_dict()
        else:
            credentials = self.credentials.to_dict()

        region = self.region

        provider_type = self.provider_type

        endpoint_url: None | str | Unset
        if isinstance(self.endpoint_url, Unset):
            endpoint_url = UNSET
        else:
            endpoint_url = self.endpoint_url

        use_ssl = self.use_ssl

        verify_ssl = self.verify_ssl

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "credentials": credentials,
                "region": region,
            }
        )
        if provider_type is not UNSET:
            field_dict["provider_type"] = provider_type
        if endpoint_url is not UNSET:
            field_dict["endpoint_url"] = endpoint_url
        if use_ssl is not UNSET:
            field_dict["use_ssl"] = use_ssl
        if verify_ssl is not UNSET:
            field_dict["verify_ssl"] = verify_ssl

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.s3_access_key_credentials import S3AccessKeyCredentials
        from ..models.s3_role_credentials import S3RoleCredentials

        d = dict(src_dict)

        def _parse_credentials(data: object) -> S3AccessKeyCredentials | S3RoleCredentials:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                credentials_type_0 = S3AccessKeyCredentials.from_dict(data)

                return credentials_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            credentials_type_1 = S3RoleCredentials.from_dict(data)

            return credentials_type_1

        credentials = _parse_credentials(d.pop("credentials"))

        region = d.pop("region")

        provider_type = cast(Literal["s3"] | Unset, d.pop("provider_type", UNSET))
        if provider_type != "s3" and not isinstance(provider_type, Unset):
            raise ValueError(f"provider_type must match const 's3', got '{provider_type}'")

        def _parse_endpoint_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        endpoint_url = _parse_endpoint_url(d.pop("endpoint_url", UNSET))

        use_ssl = d.pop("use_ssl", UNSET)

        verify_ssl = d.pop("verify_ssl", UNSET)

        s3_config = cls(
            credentials=credentials,
            region=region,
            provider_type=provider_type,
            endpoint_url=endpoint_url,
            use_ssl=use_ssl,
            verify_ssl=verify_ssl,
        )

        s3_config.additional_properties = d
        return s3_config

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
