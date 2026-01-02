from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.account_tier import AccountTier

T = TypeVar("T", bound="AddCreditsResponse")


@_attrs_define
class AddCreditsResponse:
    """Response after adding credits.

    Attributes:
        previous_balance (int): Credit balance before addition
        credits_added (int): Number of credits added
        new_balance (int): Credit balance after addition
        previous_tier (AccountTier): Account tier with monthly credit allocations.

            Tiers:
                FREE: 1,000 credits/month - Limited modalities, shared compute
                PRO: 100,000 credits/month - All modalities, dedicated namespace
                TEAM: 1,000,000 credits/month - Shared buckets, retrieval DAGs
                ENTERPRISE: Custom credits - Dedicated Ray cluster, SLA
        new_tier (AccountTier): Account tier with monthly credit allocations.

            Tiers:
                FREE: 1,000 credits/month - Limited modalities, shared compute
                PRO: 100,000 credits/month - All modalities, dedicated namespace
                TEAM: 1,000,000 credits/month - Shared buckets, retrieval DAGs
                ENTERPRISE: Custom credits - Dedicated Ray cluster, SLA
        tier_upgraded (bool): Whether tier was automatically upgraded
    """

    previous_balance: int
    credits_added: int
    new_balance: int
    previous_tier: AccountTier
    new_tier: AccountTier
    tier_upgraded: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        previous_balance = self.previous_balance

        credits_added = self.credits_added

        new_balance = self.new_balance

        previous_tier = self.previous_tier.value

        new_tier = self.new_tier.value

        tier_upgraded = self.tier_upgraded

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "previous_balance": previous_balance,
                "credits_added": credits_added,
                "new_balance": new_balance,
                "previous_tier": previous_tier,
                "new_tier": new_tier,
                "tier_upgraded": tier_upgraded,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        previous_balance = d.pop("previous_balance")

        credits_added = d.pop("credits_added")

        new_balance = d.pop("new_balance")

        previous_tier = AccountTier(d.pop("previous_tier"))

        new_tier = AccountTier(d.pop("new_tier"))

        tier_upgraded = d.pop("tier_upgraded")

        add_credits_response = cls(
            previous_balance=previous_balance,
            credits_added=credits_added,
            new_balance=new_balance,
            previous_tier=previous_tier,
            new_tier=new_tier,
            tier_upgraded=tier_upgraded,
        )

        add_credits_response.additional_properties = d
        return add_credits_response

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
