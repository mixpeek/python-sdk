from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.account_tier import AccountTier
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base_rate_limits import BaseRateLimits
    from ..models.organization_model_response_metadata import OrganizationModelResponseMetadata
    from ..models.organization_model_response_users_type_0_item import OrganizationModelResponseUsersType0Item


T = TypeVar("T", bound="OrganizationModelResponse")


@_attrs_define
class OrganizationModelResponse:
    """Response model for organization endpoints.

    SECURITY: Does NOT expose internal_id to prevent leakage of high-entropy secrets.
    Only organization_id (public identifier) is included in API responses.

        Attributes:
            organization_id (str):
            organization_name (str):
            account_type (AccountTier): Account tier with monthly credit allocations.

                Tiers:
                    FREE: 1,000 credits/month - Limited modalities, shared compute
                    PRO: 100,000 credits/month - All modalities, dedicated namespace
                    TEAM: 1,000,000 credits/month - Shared buckets, retrieval DAGs
                    ENTERPRISE: Custom credits - Dedicated Ray cluster, SLA
            credit_count (int):
            rate_limits (BaseRateLimits): Rate limits by operation type (requests per minute).

                The rate limiting system uses 5 categories aligned with actual resource consumption:

                Categories:
                    metadata: Infrastructure and configuration operations (namespaces, collections,
                             retrievers, taxonomies, clusters CRUD). Zero-credit operations with
                             highest rate limits.

                    data: Data operations (objects, documents CRUD). Low-credit operations with
                          high rate limits.

                    search: Search and retrieval operations (retriever/taxonomy execution).
                            Medium-credit operations with moderate rate limits.

                    upload: File upload operations (credit-intensive: 1 credit/MB). Variable-credit
                            operations with lower rate limits.

                    compute: Compute operations (cluster execution, batch processing). High-credit
                             operations (10 credits/min video) with lowest rate limits.

                Rate Limit Strategy:
                    Higher limits for low-cost operations (metadata, data)
                    Lower limits for high-cost operations (upload, compute)
                    This aligns API throttling with actual infrastructure costs

                Examples:
                    - Creating a namespace: Uses 'metadata' category (fast, cheap)
                    - Uploading a file: Uses 'upload' category (slow, expensive per MB)
                    - Executing a retriever: Uses 'search' category (moderate cost)
                    - Running batch processing: Uses 'compute' category (very expensive)
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
            logo_url (None | str | Unset):
            metadata (OrganizationModelResponseMetadata | Unset):
            billing_email (None | str | Unset):
            users (list[OrganizationModelResponseUsersType0Item] | None | Unset):
    """

    organization_id: str
    organization_name: str
    account_type: AccountTier
    credit_count: int
    rate_limits: BaseRateLimits
    created_at: datetime.datetime
    updated_at: datetime.datetime
    logo_url: None | str | Unset = UNSET
    metadata: OrganizationModelResponseMetadata | Unset = UNSET
    billing_email: None | str | Unset = UNSET
    users: list[OrganizationModelResponseUsersType0Item] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        organization_id = self.organization_id

        organization_name = self.organization_name

        account_type = self.account_type.value

        credit_count = self.credit_count

        rate_limits = self.rate_limits.to_dict()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        logo_url: None | str | Unset
        if isinstance(self.logo_url, Unset):
            logo_url = UNSET
        else:
            logo_url = self.logo_url

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        billing_email: None | str | Unset
        if isinstance(self.billing_email, Unset):
            billing_email = UNSET
        else:
            billing_email = self.billing_email

        users: list[dict[str, Any]] | None | Unset
        if isinstance(self.users, Unset):
            users = UNSET
        elif isinstance(self.users, list):
            users = []
            for users_type_0_item_data in self.users:
                users_type_0_item = users_type_0_item_data.to_dict()
                users.append(users_type_0_item)

        else:
            users = self.users

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "organization_id": organization_id,
                "organization_name": organization_name,
                "account_type": account_type,
                "credit_count": credit_count,
                "rate_limits": rate_limits,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if logo_url is not UNSET:
            field_dict["logo_url"] = logo_url
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if billing_email is not UNSET:
            field_dict["billing_email"] = billing_email
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.base_rate_limits import BaseRateLimits
        from ..models.organization_model_response_metadata import OrganizationModelResponseMetadata
        from ..models.organization_model_response_users_type_0_item import OrganizationModelResponseUsersType0Item

        d = dict(src_dict)
        organization_id = d.pop("organization_id")

        organization_name = d.pop("organization_name")

        account_type = AccountTier(d.pop("account_type"))

        credit_count = d.pop("credit_count")

        rate_limits = BaseRateLimits.from_dict(d.pop("rate_limits"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        def _parse_logo_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        logo_url = _parse_logo_url(d.pop("logo_url", UNSET))

        _metadata = d.pop("metadata", UNSET)
        metadata: OrganizationModelResponseMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = OrganizationModelResponseMetadata.from_dict(_metadata)

        def _parse_billing_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        billing_email = _parse_billing_email(d.pop("billing_email", UNSET))

        def _parse_users(data: object) -> list[OrganizationModelResponseUsersType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                users_type_0 = []
                _users_type_0 = data
                for users_type_0_item_data in _users_type_0:
                    users_type_0_item = OrganizationModelResponseUsersType0Item.from_dict(users_type_0_item_data)

                    users_type_0.append(users_type_0_item)

                return users_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OrganizationModelResponseUsersType0Item] | None | Unset, data)

        users = _parse_users(d.pop("users", UNSET))

        organization_model_response = cls(
            organization_id=organization_id,
            organization_name=organization_name,
            account_type=account_type,
            credit_count=credit_count,
            rate_limits=rate_limits,
            created_at=created_at,
            updated_at=updated_at,
            logo_url=logo_url,
            metadata=metadata,
            billing_email=billing_email,
            users=users,
        )

        organization_model_response.additional_properties = d
        return organization_model_response

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
