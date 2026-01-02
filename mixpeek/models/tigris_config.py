from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tigris_access_key_credentials import TigrisAccessKeyCredentials


T = TypeVar("T", bound="TigrisConfig")


@_attrs_define
class TigrisConfig:
    """Tigris Data globally distributed object storage configuration.

    Tigris is an S3-compatible object storage service with automatic global
    distribution, zero egress fees, and built-in CDN capabilities. It uses
    the AWS S3 API, making integration straightforward.

    Key Features:
        - S3-compatible API (drop-in replacement)
        - Automatic global data distribution
        - Zero egress fees
        - Built-in CDN and caching
        - Strong consistency guarantees

    Authentication:
        - Access keys only (similar to S3 access keys)
        - No IAM role assumption (Tigris is not AWS)

    Requirements:
        - Tigris account with access keys
        - Bucket created in Tigris console
        - Network connectivity to fly.storage.tigris.dev

    Use Cases:
        - Globally distributed media assets
        - Low-latency content delivery worldwide
        - Cost-effective storage with no egress fees
        - S3-compatible workflows outside AWS

        Attributes:
            credentials (TigrisAccessKeyCredentials): Tigris Data access key credentials.

                Tigris uses S3-compatible authentication with access keys.
                Credentials can be obtained from the Tigris dashboard at https://console.tigris.dev.

                Prerequisites:
                    - Create a Tigris account at https://www.tigrisdata.com
                    - Create a bucket in the Tigris console
                    - Generate access keys from the dashboard

                Security:
                    - secret_access_key is encrypted at rest using MongoDB CSFLE
                    - Rotate keys regularly via the Tigris dashboard
                    - Use bucket-scoped keys when possible for least privilege

                Use Cases:
                    - Globally distributed object storage
                    - Low-latency content delivery
                    - S3-compatible workflows with zero egress fees
            provider_type (Literal['tigris'] | Unset):  Default: 'tigris'.
            region (str | Unset): Region for Tigris. Typically 'auto' for automatic global distribution. Tigris
                automatically distributes data globally, so region is usually 'auto'. Default: auto Default: 'auto'.
            endpoint_url (str | Unset): Tigris S3-compatible endpoint URL. Default: https://fly.storage.tigris.dev This is
                the standard Tigris endpoint and usually doesn't need to be changed. Default: 'https://fly.storage.tigris.dev'.
    """

    credentials: TigrisAccessKeyCredentials
    provider_type: Literal["tigris"] | Unset = "tigris"
    region: str | Unset = "auto"
    endpoint_url: str | Unset = "https://fly.storage.tigris.dev"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        credentials = self.credentials.to_dict()

        provider_type = self.provider_type

        region = self.region

        endpoint_url = self.endpoint_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "credentials": credentials,
            }
        )
        if provider_type is not UNSET:
            field_dict["provider_type"] = provider_type
        if region is not UNSET:
            field_dict["region"] = region
        if endpoint_url is not UNSET:
            field_dict["endpoint_url"] = endpoint_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tigris_access_key_credentials import TigrisAccessKeyCredentials

        d = dict(src_dict)
        credentials = TigrisAccessKeyCredentials.from_dict(d.pop("credentials"))

        provider_type = cast(Literal["tigris"] | Unset, d.pop("provider_type", UNSET))
        if provider_type != "tigris" and not isinstance(provider_type, Unset):
            raise ValueError(f"provider_type must match const 'tigris', got '{provider_type}'")

        region = d.pop("region", UNSET)

        endpoint_url = d.pop("endpoint_url", UNSET)

        tigris_config = cls(
            credentials=credentials,
            provider_type=provider_type,
            region=region,
            endpoint_url=endpoint_url,
        )

        tigris_config.additional_properties = d
        return tigris_config

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
