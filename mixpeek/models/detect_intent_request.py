from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DetectIntentRequest")


@_attrs_define
class DetectIntentRequest:
    """Request to detect intent from user input.

    Attributes:
        user_request: The user's natural language request to analyze
        include_collection_analysis: Whether to analyze existing collections

        Attributes:
            user_request (str): User's natural language request
            include_collection_analysis (bool | Unset): Whether to check existing collections Default: True.
    """

    user_request: str
    include_collection_analysis: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_request = self.user_request

        include_collection_analysis = self.include_collection_analysis

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user_request": user_request,
            }
        )
        if include_collection_analysis is not UNSET:
            field_dict["include_collection_analysis"] = include_collection_analysis

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_request = d.pop("user_request")

        include_collection_analysis = d.pop("include_collection_analysis", UNSET)

        detect_intent_request = cls(
            user_request=user_request,
            include_collection_analysis=include_collection_analysis,
        )

        detect_intent_request.additional_properties = d
        return detect_intent_request

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
