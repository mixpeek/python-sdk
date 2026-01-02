from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar(
    "T", bound="ListPublishedRetrieversV1RetrieversPublishedGetResponseListPublishedRetrieversV1RetrieversPublishedGet"
)


@_attrs_define
class ListPublishedRetrieversV1RetrieversPublishedGetResponseListPublishedRetrieversV1RetrieversPublishedGet:
    """ """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        list_published_retrievers_v1_retrievers_published_get_response_list_published_retrievers_v1_retrievers_published_get = cls()

        list_published_retrievers_v1_retrievers_published_get_response_list_published_retrievers_v1_retrievers_published_get.additional_properties = d
        return list_published_retrievers_v1_retrievers_published_get_response_list_published_retrievers_v1_retrievers_published_get

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
