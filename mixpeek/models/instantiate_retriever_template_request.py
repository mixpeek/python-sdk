from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InstantiateRetrieverTemplateRequest")


@_attrs_define
class InstantiateRetrieverTemplateRequest:
    """Request to instantiate a retriever from a template.

    Attributes:
        retriever_name (str): Name for the new retriever
        collection_identifiers (list[str]): Collection identifiers to use for the retriever
        description (None | str | Unset): Optional description override for the retriever
        tags (list[str] | Unset): Optional tags for the retriever
    """

    retriever_name: str
    collection_identifiers: list[str]
    description: None | str | Unset = UNSET
    tags: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        retriever_name = self.retriever_name

        collection_identifiers = self.collection_identifiers

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "retriever_name": retriever_name,
                "collection_identifiers": collection_identifiers,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        retriever_name = d.pop("retriever_name")

        collection_identifiers = cast(list[str], d.pop("collection_identifiers"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        tags = cast(list[str], d.pop("tags", UNSET))

        instantiate_retriever_template_request = cls(
            retriever_name=retriever_name,
            collection_identifiers=collection_identifiers,
            description=description,
            tags=tags,
        )

        instantiate_retriever_template_request.additional_properties = d
        return instantiate_retriever_template_request

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
