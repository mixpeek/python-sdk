from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SchemaSyncResponse")


@_attrs_define
class SchemaSyncResponse:
    """Response from schema sync operation.

    Attributes:
        success (bool): Whether schema sync succeeded
        collection_id (str): Collection that was synced
        schema_version (int): New schema version
        previous_version (int): Previous schema version
        fields_total (int): Total fields in output_schema
        documents_sampled (int): Number of documents sampled
        fields_added (list[str] | Unset): List of new fields discovered
        downstream_collections_updated (list[str] | Unset): Downstream collections that were updated
        message (None | str | Unset): Additional message or error
    """

    success: bool
    collection_id: str
    schema_version: int
    previous_version: int
    fields_total: int
    documents_sampled: int
    fields_added: list[str] | Unset = UNSET
    downstream_collections_updated: list[str] | Unset = UNSET
    message: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        collection_id = self.collection_id

        schema_version = self.schema_version

        previous_version = self.previous_version

        fields_total = self.fields_total

        documents_sampled = self.documents_sampled

        fields_added: list[str] | Unset = UNSET
        if not isinstance(self.fields_added, Unset):
            fields_added = self.fields_added

        downstream_collections_updated: list[str] | Unset = UNSET
        if not isinstance(self.downstream_collections_updated, Unset):
            downstream_collections_updated = self.downstream_collections_updated

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "collection_id": collection_id,
                "schema_version": schema_version,
                "previous_version": previous_version,
                "fields_total": fields_total,
                "documents_sampled": documents_sampled,
            }
        )
        if fields_added is not UNSET:
            field_dict["fields_added"] = fields_added
        if downstream_collections_updated is not UNSET:
            field_dict["downstream_collections_updated"] = downstream_collections_updated
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success")

        collection_id = d.pop("collection_id")

        schema_version = d.pop("schema_version")

        previous_version = d.pop("previous_version")

        fields_total = d.pop("fields_total")

        documents_sampled = d.pop("documents_sampled")

        fields_added = cast(list[str], d.pop("fields_added", UNSET))

        downstream_collections_updated = cast(list[str], d.pop("downstream_collections_updated", UNSET))

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        schema_sync_response = cls(
            success=success,
            collection_id=collection_id,
            schema_version=schema_version,
            previous_version=previous_version,
            fields_total=fields_total,
            documents_sampled=documents_sampled,
            fields_added=fields_added,
            downstream_collections_updated=downstream_collections_updated,
            message=message,
        )

        schema_sync_response.additional_properties = d
        return schema_sync_response

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
