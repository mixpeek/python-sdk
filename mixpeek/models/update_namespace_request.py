from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.payload_index_config import PayloadIndexConfig


T = TypeVar("T", bound="UpdateNamespaceRequest")


@_attrs_define
class UpdateNamespaceRequest:
    """Request schema for updating a namespace's payload indexes.

    Attributes:
        namespace_name (None | str | Unset): Name of the namespace to update Example: spotify_playlists_dev.
        payload_indexes (list[PayloadIndexConfig] | None | Unset): Updated list of payload index configurations Example:
            [{'field_name': 'metadata.title', 'field_schema': {'lowercase': True, 'max_token_len': 15, 'min_token_len': 2,
            'tokenizer': 'word', 'type': 'text'}, 'is_protected': False, 'type': 'text'}, {'field_name':
            'metadata.description', 'field_schema': {'is_tenant': False, 'type': 'keyword'}, 'is_protected': False, 'type':
            'keyword'}].
    """

    namespace_name: None | str | Unset = UNSET
    payload_indexes: list[PayloadIndexConfig] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        namespace_name: None | str | Unset
        if isinstance(self.namespace_name, Unset):
            namespace_name = UNSET
        else:
            namespace_name = self.namespace_name

        payload_indexes: list[dict[str, Any]] | None | Unset
        if isinstance(self.payload_indexes, Unset):
            payload_indexes = UNSET
        elif isinstance(self.payload_indexes, list):
            payload_indexes = []
            for payload_indexes_type_0_item_data in self.payload_indexes:
                payload_indexes_type_0_item = payload_indexes_type_0_item_data.to_dict()
                payload_indexes.append(payload_indexes_type_0_item)

        else:
            payload_indexes = self.payload_indexes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if namespace_name is not UNSET:
            field_dict["namespace_name"] = namespace_name
        if payload_indexes is not UNSET:
            field_dict["payload_indexes"] = payload_indexes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.payload_index_config import PayloadIndexConfig

        d = dict(src_dict)

        def _parse_namespace_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        namespace_name = _parse_namespace_name(d.pop("namespace_name", UNSET))

        def _parse_payload_indexes(data: object) -> list[PayloadIndexConfig] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                payload_indexes_type_0 = []
                _payload_indexes_type_0 = data
                for payload_indexes_type_0_item_data in _payload_indexes_type_0:
                    payload_indexes_type_0_item = PayloadIndexConfig.from_dict(payload_indexes_type_0_item_data)

                    payload_indexes_type_0.append(payload_indexes_type_0_item)

                return payload_indexes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PayloadIndexConfig] | None | Unset, data)

        payload_indexes = _parse_payload_indexes(d.pop("payload_indexes", UNSET))

        update_namespace_request = cls(
            namespace_name=namespace_name,
            payload_indexes=payload_indexes,
        )

        update_namespace_request.additional_properties = d
        return update_namespace_request

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
