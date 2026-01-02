from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OrganizationPublishStatsResponse")


@_attrs_define
class OrganizationPublishStatsResponse:
    """Response for organization publish quota stats.

    Attributes:
        current_count (int): Number of currently published retrievers
        max_allowed (int): Maximum number of allowed published retrievers
        remaining (int): Number of remaining publish slots
        at_limit (bool): Whether the organization has reached the publish limit
    """

    current_count: int
    max_allowed: int
    remaining: int
    at_limit: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_count = self.current_count

        max_allowed = self.max_allowed

        remaining = self.remaining

        at_limit = self.at_limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "current_count": current_count,
                "max_allowed": max_allowed,
                "remaining": remaining,
                "at_limit": at_limit,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        current_count = d.pop("current_count")

        max_allowed = d.pop("max_allowed")

        remaining = d.pop("remaining")

        at_limit = d.pop("at_limit")

        organization_publish_stats_response = cls(
            current_count=current_count,
            max_allowed=max_allowed,
            remaining=remaining,
            at_limit=at_limit,
        )

        organization_publish_stats_response.additional_properties = d
        return organization_publish_stats_response

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
