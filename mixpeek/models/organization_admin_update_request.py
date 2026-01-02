from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.account_tier import AccountTier
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base_rate_limits import BaseRateLimits
    from ..models.organization_infrastructure import OrganizationInfrastructure


T = TypeVar("T", bound="OrganizationAdminUpdateRequest")


@_attrs_define
class OrganizationAdminUpdateRequest:
    """Admin-only update payload for organization.

    Security: This model is ONLY used by private admin endpoints that require
    MIXPEEK_PRIVATE_TOKEN authentication. Regular users cannot access or modify
    these fields, especially infrastructure configuration.

        Attributes:
            account_type (AccountTier | None | Unset): Update organization billing tier.
            rate_limits (BaseRateLimits | None | Unset): Override rate limits for the organization.
            infrastructure (None | OrganizationInfrastructure | Unset): 🔒 ADMIN ONLY: Configure dedicated infrastructure
                (Qdrant/Ray). This field is ONLY accessible via private admin endpoints with MIXPEEK_PRIVATE_TOKEN. NOT exposed
                in public API responses. NOT modifiable by organization users. Used for ENTERPRISE customers with dedicated
                infrastructure.
    """

    account_type: AccountTier | None | Unset = UNSET
    rate_limits: BaseRateLimits | None | Unset = UNSET
    infrastructure: None | OrganizationInfrastructure | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.base_rate_limits import BaseRateLimits
        from ..models.organization_infrastructure import OrganizationInfrastructure

        account_type: None | str | Unset
        if isinstance(self.account_type, Unset):
            account_type = UNSET
        elif isinstance(self.account_type, AccountTier):
            account_type = self.account_type.value
        else:
            account_type = self.account_type

        rate_limits: dict[str, Any] | None | Unset
        if isinstance(self.rate_limits, Unset):
            rate_limits = UNSET
        elif isinstance(self.rate_limits, BaseRateLimits):
            rate_limits = self.rate_limits.to_dict()
        else:
            rate_limits = self.rate_limits

        infrastructure: dict[str, Any] | None | Unset
        if isinstance(self.infrastructure, Unset):
            infrastructure = UNSET
        elif isinstance(self.infrastructure, OrganizationInfrastructure):
            infrastructure = self.infrastructure.to_dict()
        else:
            infrastructure = self.infrastructure

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_type is not UNSET:
            field_dict["account_type"] = account_type
        if rate_limits is not UNSET:
            field_dict["rate_limits"] = rate_limits
        if infrastructure is not UNSET:
            field_dict["infrastructure"] = infrastructure

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.base_rate_limits import BaseRateLimits
        from ..models.organization_infrastructure import OrganizationInfrastructure

        d = dict(src_dict)

        def _parse_account_type(data: object) -> AccountTier | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                account_type_type_0 = AccountTier(data)

                return account_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AccountTier | None | Unset, data)

        account_type = _parse_account_type(d.pop("account_type", UNSET))

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

        def _parse_infrastructure(data: object) -> None | OrganizationInfrastructure | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                infrastructure_type_0 = OrganizationInfrastructure.from_dict(data)

                return infrastructure_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OrganizationInfrastructure | Unset, data)

        infrastructure = _parse_infrastructure(d.pop("infrastructure", UNSET))

        organization_admin_update_request = cls(
            account_type=account_type,
            rate_limits=rate_limits,
            infrastructure=infrastructure,
        )

        organization_admin_update_request.additional_properties = d
        return organization_admin_update_request

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
