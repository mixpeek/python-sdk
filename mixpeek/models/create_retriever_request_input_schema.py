from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.retriever_input_schema_field import RetrieverInputSchemaField


T = TypeVar("T", bound="CreateRetrieverRequestInputSchema")


@_attrs_define
class CreateRetrieverRequestInputSchema:
    """Input schema properties keyed by field name (OPTIONAL). Can be empty for static retrievers with hardcoded stage
    parameters. Each field can include: type, description, required, default, and examples. The 'examples' field (list)
    provides sample values that will be shown to users when the retriever is published with include_metadata=true.

    """

    additional_properties: dict[str, RetrieverInputSchemaField] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.retriever_input_schema_field import RetrieverInputSchemaField

        d = dict(src_dict)
        create_retriever_request_input_schema = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = RetrieverInputSchemaField.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        create_retriever_request_input_schema.additional_properties = additional_properties
        return create_retriever_request_input_schema

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> RetrieverInputSchemaField:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: RetrieverInputSchemaField) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
