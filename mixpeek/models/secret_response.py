from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SecretResponse")


@_attrs_define
class SecretResponse:
    """Response for secret operations (NEVER includes actual decrypted value).

    This response is returned after creating, updating, or deleting a secret.
    For security, the actual secret value is NEVER included in API responses.
    Only the secret name and operation status are returned.

    **Security**:
    - Decrypted secret values are NEVER included
    - Only secret name and operation status returned
    - Actual value only accessible by internal services

    **Fields**:
    - secret_name: Name of the secret that was operated on
    - created: True if secret was created (null for other operations)
    - updated: True if secret was updated (null for other operations)
    - deleted: True if secret was deleted (null for other operations)

        Attributes:
            secret_name (str): Name of the secret that was operated on. This is the same name provided in the request. Use
                this name to reference the secret in api_call stage configuration.
            created (bool | None | Unset): True if this secret was created, null otherwise. Only set for POST /secrets
                operations.
            updated (bool | None | Unset): True if this secret was updated, null otherwise. Only set for PUT /secrets/{name}
                operations.
            deleted (bool | None | Unset): True if this secret was deleted, null otherwise. Only set for DELETE
                /secrets/{name} operations.
    """

    secret_name: str
    created: bool | None | Unset = UNSET
    updated: bool | None | Unset = UNSET
    deleted: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        secret_name = self.secret_name

        created: bool | None | Unset
        if isinstance(self.created, Unset):
            created = UNSET
        else:
            created = self.created

        updated: bool | None | Unset
        if isinstance(self.updated, Unset):
            updated = UNSET
        else:
            updated = self.updated

        deleted: bool | None | Unset
        if isinstance(self.deleted, Unset):
            deleted = UNSET
        else:
            deleted = self.deleted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "secret_name": secret_name,
            }
        )
        if created is not UNSET:
            field_dict["created"] = created
        if updated is not UNSET:
            field_dict["updated"] = updated
        if deleted is not UNSET:
            field_dict["deleted"] = deleted

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        secret_name = d.pop("secret_name")

        def _parse_created(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        created = _parse_created(d.pop("created", UNSET))

        def _parse_updated(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        updated = _parse_updated(d.pop("updated", UNSET))

        def _parse_deleted(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        deleted = _parse_deleted(d.pop("deleted", UNSET))

        secret_response = cls(
            secret_name=secret_name,
            created=created,
            updated=updated,
            deleted=deleted,
        )

        secret_response.additional_properties = d
        return secret_response

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
