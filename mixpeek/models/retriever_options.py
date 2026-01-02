from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RetrieverOptions")


@_attrs_define
class RetrieverOptions:
    """Options for retriever migration.

    Attributes:
        preserve_retriever_ids (bool | Unset): Keep same retriever IDs (avoid conflicts) Default: False.
        migrate_interactions (bool | Unset): Migrate user interaction data Default: False.
        migrate_execution_history (bool | Unset): Migrate past execution history Default: False.
        validate_references (bool | Unset): Pre-flight check all references exist Default: True.
    """

    preserve_retriever_ids: bool | Unset = False
    migrate_interactions: bool | Unset = False
    migrate_execution_history: bool | Unset = False
    validate_references: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        preserve_retriever_ids = self.preserve_retriever_ids

        migrate_interactions = self.migrate_interactions

        migrate_execution_history = self.migrate_execution_history

        validate_references = self.validate_references

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if preserve_retriever_ids is not UNSET:
            field_dict["preserve_retriever_ids"] = preserve_retriever_ids
        if migrate_interactions is not UNSET:
            field_dict["migrate_interactions"] = migrate_interactions
        if migrate_execution_history is not UNSET:
            field_dict["migrate_execution_history"] = migrate_execution_history
        if validate_references is not UNSET:
            field_dict["validate_references"] = validate_references

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        preserve_retriever_ids = d.pop("preserve_retriever_ids", UNSET)

        migrate_interactions = d.pop("migrate_interactions", UNSET)

        migrate_execution_history = d.pop("migrate_execution_history", UNSET)

        validate_references = d.pop("validate_references", UNSET)

        retriever_options = cls(
            preserve_retriever_ids=preserve_retriever_ids,
            migrate_interactions=migrate_interactions,
            migrate_execution_history=migrate_execution_history,
            validate_references=validate_references,
        )

        retriever_options.additional_properties = d
        return retriever_options

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
