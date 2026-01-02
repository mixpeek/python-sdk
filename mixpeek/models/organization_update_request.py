from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base_rate_limits import BaseRateLimits
    from ..models.organization_update_request_metadata_type_0 import OrganizationUpdateRequestMetadataType0


T = TypeVar("T", bound="OrganizationUpdateRequest")


@_attrs_define
class OrganizationUpdateRequest:
    """Partial update payload for organization metadata.

    Attributes:
        organization_name (None | str | Unset): Updated display name for the organization.
        logo_url (None | str | Unset): Updated organization logo URL (e.g., custom logo to override auto-generated
            logo).
        billing_email (None | str | Unset): Updated billing contact email.
        metadata (None | OrganizationUpdateRequestMetadataType0 | Unset): Replace metadata with provided dictionary when
            set.
        rate_limits (BaseRateLimits | None | Unset): Override the computed rate limits for the organization.
    """

    organization_name: None | str | Unset = UNSET
    logo_url: None | str | Unset = UNSET
    billing_email: None | str | Unset = UNSET
    metadata: None | OrganizationUpdateRequestMetadataType0 | Unset = UNSET
    rate_limits: BaseRateLimits | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.base_rate_limits import BaseRateLimits
        from ..models.organization_update_request_metadata_type_0 import OrganizationUpdateRequestMetadataType0

        organization_name: None | str | Unset
        if isinstance(self.organization_name, Unset):
            organization_name = UNSET
        else:
            organization_name = self.organization_name

        logo_url: None | str | Unset
        if isinstance(self.logo_url, Unset):
            logo_url = UNSET
        else:
            logo_url = self.logo_url

        billing_email: None | str | Unset
        if isinstance(self.billing_email, Unset):
            billing_email = UNSET
        else:
            billing_email = self.billing_email

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, OrganizationUpdateRequestMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        rate_limits: dict[str, Any] | None | Unset
        if isinstance(self.rate_limits, Unset):
            rate_limits = UNSET
        elif isinstance(self.rate_limits, BaseRateLimits):
            rate_limits = self.rate_limits.to_dict()
        else:
            rate_limits = self.rate_limits

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if organization_name is not UNSET:
            field_dict["organization_name"] = organization_name
        if logo_url is not UNSET:
            field_dict["logo_url"] = logo_url
        if billing_email is not UNSET:
            field_dict["billing_email"] = billing_email
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if rate_limits is not UNSET:
            field_dict["rate_limits"] = rate_limits

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.base_rate_limits import BaseRateLimits
        from ..models.organization_update_request_metadata_type_0 import OrganizationUpdateRequestMetadataType0

        d = dict(src_dict)

        def _parse_organization_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        organization_name = _parse_organization_name(d.pop("organization_name", UNSET))

        def _parse_logo_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        logo_url = _parse_logo_url(d.pop("logo_url", UNSET))

        def _parse_billing_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        billing_email = _parse_billing_email(d.pop("billing_email", UNSET))

        def _parse_metadata(data: object) -> None | OrganizationUpdateRequestMetadataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = OrganizationUpdateRequestMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OrganizationUpdateRequestMetadataType0 | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        def _parse_rate_limits(data: object) -> BaseRateLimits | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                rate_limits_type_0 = BaseRateLimits.from_dict(data)

                return rate_limits_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BaseRateLimits | None | Unset, data)

        rate_limits = _parse_rate_limits(d.pop("rate_limits", UNSET))

        organization_update_request = cls(
            organization_name=organization_name,
            logo_url=logo_url,
            billing_email=billing_email,
            metadata=metadata,
            rate_limits=rate_limits,
        )

        organization_update_request.additional_properties = d
        return organization_update_request

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
